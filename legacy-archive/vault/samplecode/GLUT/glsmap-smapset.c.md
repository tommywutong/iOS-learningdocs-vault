---
title: GLUT
apple_id: DTS10000528
resource_type: Sample Code
platform: macOS
topic: Graphics & Animation
technology: OpenGL
published: '2008-02-08'
source_url: https://developer.apple.com/library/archive/samplecode/glut/Listings/glsmap_smap_set_c.html
archived_at: '2026-07-18T03:29:18.993366Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [GLUT](GLUT.md)


[Next](glsmap-smapsetfunc.c.md)[Previous](glsmap-smaprvec2st.c.md)

# glsmap/smap_set.c

```c

/* Copyright (c) Mark J. Kilgard, 1998.  */

/* This program is freely distributable without licensing fees
   and is provided without guarantee or warrantee expressed or
   implied. This program is -not- in the public domain. */

#include "glsmapint.h"

void smapSetEye(SphereMap *smap,
    GLfloat eyex, GLfloat eyey, GLfloat eyez)
{
    smap->eye[X] = eyex;
    smap->eye[Y] = eyey;
    smap->eye[Z] = eyez;
}

void smapSetUp(SphereMap *smap,
    GLfloat upx, GLfloat upy, GLfloat upz)
{
    smap->up[X] = upx;
    smap->up[Y] = upy;
    smap->up[Z] = upz;
}

void smapSetObject(SphereMap *smap,
    GLfloat objx, GLfloat objy, GLfloat objz)
{
    smap->obj[X] = objx;
    smap->obj[Y] = objy;
    smap->obj[Z] = objz;
}
```

[Next](glsmap-smapsetfunc.c.md)[Previous](glsmap-smaprvec2st.c.md)

