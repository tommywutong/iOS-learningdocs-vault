---
title: ZAM
apple_id: DTS10000063
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/ZAM/Listings/GameSource_FixGraf_c.html
archived_at: '2026-07-18T03:28:33.017957Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [ZAM](ZAM.md)


[Next](GameSource-GameAEvents.c.md)[Previous](GameSource-ExplosionSprites.c.md)

# GameSource/FixGraf.c

```c
#include "FixGraf.h"


void    FixRectToRect(fixRect *fr, Rect *r)
{
    r->top = FixToInt(fr->top);
    r->left = FixToInt(fr->left);
    r->bottom = FixToInt(fr->bottom);
    r->right = FixToInt(fr->right);
}

void    RectToFixRect( Rect *r, fixRect *fr)
{
    fr->top = ff(r->top);
    fr->left = ff(r->left);
    fr->bottom = ff(r->bottom);
    fr->right = ff(r->right);
}


void    PointToFixPoint( Point *p, fixPt *fp)
{
    fp->h = ff(p->h);
    fp->v = ff(p->v);
}


void    FixPointToPoint(  fixPt *fp, Point *p)
{
    p->h = FixToInt(fp->h);
    p->v = FixToInt(fp->v);
}

void    OffsetFixRect(fixRect *fr, fixPt *fp)
{
    fr->top += fp->v;
    fr->left += fp->h;
    fr->bottom += fp->v;
    fr->right += fp->h;
}
```

[Next](GameSource-GameAEvents.c.md)[Previous](GameSource-ExplosionSprites.c.md)

