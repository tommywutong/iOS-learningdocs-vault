import os,re,sys,json
def norm(s): return re.sub(r'[^0-9a-z]','',s.lower())
def build(vault):
    """(top, 分类目录名) -> 分类id，由 _indexes/<top>/<id>.md 文件名与 <top>/ 下真实目录名归一化匹配。"""
    out={}
    base=os.path.join(vault,'_indexes')
    for top in os.listdir(base):
        d=os.path.join(base,top)
        if not os.path.isdir(d) or top.startswith('by-'): continue
        ids=[f[:-3] for f in os.listdir(d) if f.endswith('.md')]
        dirs=[x for x in os.listdir(os.path.join(vault,top))
              if os.path.isdir(os.path.join(vault,top,x))]
        byn={}
        for i in ids: byn.setdefault(norm(i),[]).append(i)
        for dn in dirs:
            c=byn.get(norm(dn))
            if c:
                assert len(c)==1,(top,dn,c)
                out[(top,dn)]=c[0]
        # 未匹配的 id
        matched={out[k] for k in out if k[0]==top}
        un=[i for i in ids if i not in matched]
        if un: print('  [%s] 未匹配的分类 id:'%top, un, file=sys.stderr)
    return out

def labels(vault):
    """(top, 真实分类目录名) -> 当前索引展示名，保留已经完成的中文翻译。"""
    mapping = build(vault)
    by_id = {(top, cid): dirname for (top, dirname), cid in mapping.items()}
    out = {}
    base = os.path.join(vault, '_indexes')
    rx = re.compile(r'^## \[(.*)\]\(([^/]+)/([^/)]+)\.md\)（\d+ 份）$')
    for fn in os.listdir(base):
        if not fn.endswith('.md'):
            continue
        top = fn[:-3]
        for line in open(os.path.join(base, fn), encoding='utf-8'):
            m = rx.match(line.rstrip('\n'))
            if not m or m.group(2) != top:
                continue
            dirname = by_id.get((top, m.group(3)))
            if dirname:
                out[(top, dirname)] = m.group(1)
    return out
if __name__=='__main__':
    m=build(sys.argv[1])
    print(len(m))
    for k,v in sorted(m.items()): print(k,'->',v)
