---
title: GLUT
apple_id: DTS10000528
resource_type: Sample Code
platform: macOS
topic: Graphics & Animation
technology: OpenGL
published: '2008-02-08'
source_url: https://developer.apple.com/library/archive/samplecode/glut/Listings/glsmap_smap_origin_c.html
archived_at: '2026-07-18T03:29:18.881215Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [GLUT](GLUT.md)


[Next](glsmap-smaprender.c.md)[Previous](glsmap-smapnearfar.c.md)

# glsmap/smap_origin.c

```c

/* Copyright (c) Mark J. Kilgard, 1998.  */

/* This program is freely distributable without licensing fees
   and is provided without guarantee or warrantee expressed or
   implied. This program is -not- in the public domain. */

#include <glsmap.h>

#include "glsmapint.h"

void smapSetViewOrigin(SphereMap *smap, GLint x, GLint y)
{
        smap->viewOrigin[0] = x;
        smap->viewOrigin[1] = y;
}

void smapSetSphereMapOrigin(SphereMap *smap, GLint x, GLint y)
{
        smap->smapOrigin[0] = x;
        smap->smapOrigin[1] = y;
}

void smapGetViewOrigin(SphereMap *smap, GLint *x, GLint *y)
{
        *x = smap->viewOrigin[0];
        *y = smap->viewOrigin[1];
}

void smapGetSphereMapOrigin(SphereMap *smap, GLint *x, GLint *y)
{
        *x = smap->smapOrigin[0];
        *y = smap->smapOrigin[1];
}
```

[Next](glsmap-smaprender.c.md)[Previous](glsmap-smapnearfar.c.md)

