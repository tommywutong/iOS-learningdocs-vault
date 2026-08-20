---
title: GLUT
apple_id: DTS10000528
resource_type: Sample Code
platform: macOS
topic: Graphics & Animation
technology: OpenGL
published: '2008-02-08'
source_url: https://developer.apple.com/library/archive/samplecode/glut/Listings/glsmap_smap_getvec_c.html
archived_at: '2026-07-18T03:29:18.721663Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [GLUT](GLUT.md)


[Next](glsmap-smapmakemesh.c.md)[Previous](glsmap-smapgettexobj.c.md)

# glsmap/smap_getvec.c

```c

/* Copyright (c) Mark J. Kilgard, 1998.  */

/* This program is freely distributable without licensing fees
   and is provided without guarantee or warrantee expressed or
   implied. This program is -not- in the public domain. */

#include "glsmapint.h"

void
smapGetEyeVector(SphereMap *smap, GLfloat *eye)
{
    eye[X] = smap->eye[X];
    eye[Y] = smap->eye[Y];
    eye[Z] = smap->eye[Z];
}

void
smapGetUpVector(SphereMap *smap, GLfloat *up)
{
    up[X] = smap->up[X];
    up[Y] = smap->up[Y];
    up[Z] = smap->up[Z];
}

void
smapGetObjectVector(SphereMap *smap, GLfloat *obj)
{
    obj[X] = smap->obj[X];
    obj[Y] = smap->obj[Y];
    obj[Z] = smap->obj[Z];
}
```

[Next](glsmap-smapmakemesh.c.md)[Previous](glsmap-smapgettexobj.c.md)

