---
title: PyGTK迷宮生成器mazer
source: MaskRay (宋方睿)
source_key: maskray
source_url: 'https://maskray.me/blog/2010-01-15-maze-generator-with-pygtk'
original_language: en
published: 2010-01-15
status: active
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:c6eeaf8f19730f16'
translated: false
---

> 原文：[PyGTK迷宮生成器mazer](https://maskray.me/blog/2010-01-15-maze-generator-with-pygtk)　·　MaskRay (宋方睿)

[2010-01-15](https://maskray.me/blog/2010-01-15-maze-generator-with-pygtk)

# PyGTK迷宮生成器mazer

```e-content
#!/usr/bin/env python

from sys import stdout
from random import randrange, shuffle
import gtk

BORDER = 10
LENGTH = 24

class mazer():
    def __init__(self, maxw, maxh):
        self.maxw, self.maxh = maxw, maxh
        self.map = [[False for c in xrange(self.maxw*2+1)] for r in xrange(self.maxh*2+1)]
        self.map[randrange(1, self.maxh*2, 2)][0] = True
        self.map[randrange(1, self.maxh*2, 2)][self.maxw*2] = True
        self.DFS(randrange(1, self.maxw*2, 2), randrange(1, self.maxh*2, 2))

    def run(self):
        window = gtk.Window()
        window.set_title('mazer')
        window.connect('destroy', gtk.main_quit)

        darea = gtk.DrawingArea()
        darea.size(LENGTH*self.maxw+BORDER*2, LENGTH*self.maxh+BORDER*2)
        darea.connect('expose_event', self.expose)
        window.add(darea)

        window.show_all()
        gtk.main()

    def DFS(self, x, y):
        self.map[y][x] = True
        ds = [(1,0),(0,1),(-1,0),(0,-1)]
        shuffle(ds)
        for d in ds:
            if 0 <= x+d[0]*2 < self.maxw*2 and 0 <= y+d[1]*2 < self.maxh*2 and not self.map[y+d[1]*2][x+d[0]*2]:
                self.map[y+d[1]][x+d[0]] = True
                self.DFS(x+d[0]*2, y+d[1]*2)

    def expose(self, widget, data):
        for y in xrange(self.maxh+1):
```
