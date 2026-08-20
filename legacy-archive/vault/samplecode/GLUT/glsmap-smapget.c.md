---
title: GLUT
apple_id: DTS10000528
resource_type: Sample Code
platform: macOS
topic: Graphics & Animation
technology: OpenGL
published: '2008-02-08'
source_url: https://developer.apple.com/library/archive/samplecode/glut/Listings/glsmap_smap_get_c.html
archived_at: '2026-07-18T03:29:18.513883Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [GLUT](GLUT.md)


[Next](glsmap-smapgetfunc.c.md)[Previous](glsmap-smapflag.c.md)

# glsmap/smap_get.c

```c

/* Copyright (c) Mark J. Kilgard, 1998.  */

/* This program is freely distributable without licensing fees
   and is provided without guarantee or warrantee expressed or
   implied. This program is -not- in the public domain. */

#include "glsmapint.h"

void smapGetEye(SphereMap *smap,
    GLfloat *eyex, GLfloat *eyey, GLfloat *eyez)
{
    *eyex = smap->eye[X];
    *eyey = smap->eye[Y];
    *eyez = smap->eye[Z];
}

void smapGetUp(SphereMap *smap,
    GLfloat *upx, GLfloat *upy, GLfloat *upz)
{
    *upx = smap->up[X];
    *upy = smap->up[Y];
    *upz = smap->up[Z];
}

void smapGetObject(SphereMap *smap,
    GLfloat *objx, GLfloat *objy, GLfloat *objz)
{
    *objx = smap->obj[X];
    *objy = smap->obj[Y];
    *objz = smap->obj[Z];
}
```

[Next](glsmap-smapgetfunc.c.md)[Previous](glsmap-smapflag.c.md)

