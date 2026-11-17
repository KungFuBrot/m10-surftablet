# Read-only minimal ext4 reader: list a dir or extract a file from a partition inside a raw image.
import struct, sys
img, off = sys.argv[1], int(sys.argv[2], 0)
f = open(img, 'rb')
def rd(pos, n): f.seek(off + pos); return f.read(n)
sb = rd(1024, 1024)
assert struct.unpack_from('<H', sb, 0x38)[0] == 0xEF53, 'no ext4'
bs = 1024 << struct.unpack_from('<I', sb, 0x18)[0]
ipg = struct.unpack_from('<I', sb, 0x28)[0]
isz = struct.unpack_from('<H', sb, 0x58)[0]
incompat = struct.unpack_from('<I', sb, 0x60)[0]
dsz = struct.unpack_from('<H', sb, 0xFE)[0] if incompat & 0x80 else 32
gdt = (1 if bs > 1024 else 2) * bs
def inode(n):
    g, i = divmod(n - 1, ipg)
    gd = rd(gdt + g * dsz, dsz)
    tbl = struct.unpack_from('<I', gd, 8)[0]
    if dsz >= 64: tbl |= struct.unpack_from('<I', gd, 0x28)[0] << 32
    return rd(tbl * bs + i * isz, isz)
def extents(node):
    magic, ent, _, depth = struct.unpack_from('<HHHH', node, 0)
    assert magic == 0xF30A
    for k in range(ent):
        e = node[12 + 12 * k: 24 + 12 * k]
        if depth == 0:
            lb, ln, hi, lo = struct.unpack('<IHHI', e)
            if ln > 32768: ln -= 32768
            yield lb, (hi << 32) | lo, ln
        else:
            lb, lo, hi, _ = struct.unpack('<IIHH', e)
            yield from extents(rd(((hi << 32) | lo) * bs, bs))
def data(ino):
    d = inode(ino)
    size = struct.unpack_from('<I', d, 4)[0] | (struct.unpack_from('<I', d, 0x6C)[0] << 32)
    flags = struct.unpack_from('<I', d, 0x20)[0]
    buf = bytearray(size)
    if flags & 0x80000:
        for lb, pb, ln in extents(d[0x28:0x28 + 60]):
            chunk = rd(pb * bs, ln * bs)
            s = lb * bs
            if s < size: buf[s:min(size, s + len(chunk))] = chunk[:size - s]
    else:
        ptrs = struct.unpack_from('<15I', d, 0x28)
        blocks = list(ptrs[:12])
        per = bs // 4
        if ptrs[12]: blocks += struct.unpack('<%dI' % per, rd(ptrs[12] * bs, bs))
        if ptrs[13]:
            for p in struct.unpack('<%dI' % per, rd(ptrs[13] * bs, bs)):
                if p: blocks += struct.unpack('<%dI' % per, rd(p * bs, bs))
        for k, b in enumerate(blocks):
            s = k * bs
            if s >= size: break
            if b: buf[s:min(size, s + bs)] = rd(b * bs, bs)[:size - s]
    return bytes(buf)
def listdir(ino):
    d = data(ino); p = 0; out = {}
    while p + 8 <= len(d):
        i, rl, nl = struct.unpack_from('<IHB', d, p)
        if rl == 0: break
        if i: out[d[p + 8:p + 8 + nl].decode('utf-8', 'replace')] = i
        p += rl
    return out
def lookup(path):
    ino = 2
    for part in [x for x in path.split('/') if x]: ino = listdir(ino)[part]
    return ino
cmd, path = sys.argv[3], sys.argv[4]
if cmd == 'ls':
    for n in sorted(listdir(lookup(path))): print(n)
else:
    open(sys.argv[5], 'wb').write(data(lookup(path)))
