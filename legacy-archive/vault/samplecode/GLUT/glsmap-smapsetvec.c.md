---
title: GLUT
apple_id: DTS10000528
resource_type: Sample Code
platform: macOS
topic: Graphics & Animation
technology: OpenGL
published: '2008-02-08'
source_url: https://developer.apple.com/library/archive/samplecode/glut/Listings/glsmap_smap_setvec_c.html
archived_at: '2026-07-18T03:29:19.055835Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [GLUT](GLUT.md)


[Next](glsmap-smaptexdim.c.md)[Previous](glsmap-smapsetfunc.c.md)

# glsmap/smap_setvec.c

```c

/* Copyright (c) Mark J. Kilgard, 1998.  */

/* This program is freely distributable without licensing fees
   and is provided without guarantee or warrantee expressed or
   implied. This program is -not- in the public domain. */

#include "glsmapint.h"

void
smapSetEyeVector(SphereMap *smap, GLfloat *eye)
{
    smap->eye[X] = eye[X];
    smap->eye[Y] = eye[Y];
    smap->eye[Z] = eye[Z];
}

void
smapSetUpVector(SphereMap *smap, GLfloat *up)
{
    smap->up[X] = up[X];
    smap->up[Y] = up[Y];
    smap->up[Z] = up[Z];
}

void
smapSetObjectVector(SphereMap *smap, GLfloat *obj)
{
    smap->obj[X] = obj[X];
    smap->obj[Y] = obj[Y];
    smap->obj[Z] = obj[Z];
}
```

[Next](glsmap-smaptexdim.c.md)[Previous](glsmap-smapsetfunc.c.md)

