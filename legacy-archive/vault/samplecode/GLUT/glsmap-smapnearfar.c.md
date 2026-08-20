---
title: GLUT
apple_id: DTS10000528
resource_type: Sample Code
platform: macOS
topic: Graphics & Animation
technology: OpenGL
published: '2008-02-08'
source_url: https://developer.apple.com/library/archive/samplecode/glut/Listings/glsmap_smap_nearfar_c.html
archived_at: '2026-07-18T03:29:18.857506Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [GLUT](GLUT.md)


[Next](glsmap-smaporigin.c.md)[Previous](glsmap-smapmakemesh.c.md)

# glsmap/smap_nearfar.c

```c

/* Copyright (c) Mark J. Kilgard, 1998.  */

/* This program is freely distributable without licensing fees
   and is provided without guarantee or warrantee expressed or
   implied. This program is -not- in the public domain. */

#include "glsmapint.h"

void
smapSetNearFar(SphereMap *smap,
               GLfloat viewNear, GLfloat viewFar)
{
    /* Curse Intel for "near" and "far" keywords. */
    smap->viewNear = viewNear;
    smap->viewFar = viewFar;
}

void
smapGetNearFar(SphereMap *smap,
               GLfloat *viewNear, GLfloat *viewFar)
{
    /* Curse Intel for "near" and "far" keywords. */
        *viewNear = smap->viewNear;
    *viewFar = smap->viewFar;
}
```

[Next](glsmap-smaporigin.c.md)[Previous](glsmap-smapmakemesh.c.md)

