---
title: GLUT
apple_id: DTS10000528
resource_type: Sample Code
platform: macOS
topic: Graphics & Animation
technology: OpenGL
published: '2008-02-08'
source_url: https://developer.apple.com/library/archive/samplecode/glut/Listings/glsmap_smap_texobj_c.html
archived_at: '2026-07-18T03:29:19.115464Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [GLUT](GLUT.md)


[Next](glut.h.md)[Previous](glsmap-smaptexdim.c.md)

# glsmap/smap_texobj.c

```c

/* Copyright (c) Mark J. Kilgard, 1998.  */

/* This program is freely distributable without licensing fees
   and is provided without guarantee or warrantee expressed or
   implied. This program is -not- in the public domain. */

#include "glsmapint.h"

void
smapSetSphereMapTexObj(SphereMap *smap, GLuint texobj)
{
    smap->smapTexObj = texobj;
}

void
smapSetViewTexObj(SphereMap *smap, GLuint texobj)
{
    smap->viewTexObj = texobj;
}

void
smapSetViewTexObjs(SphereMap *smap, GLuint texobjs[6])
{
    int i;

    for (i=0; i<6; i++) {
        smap->viewTexObjs[i] = texobjs[i];
    }
}
```

[Next](glut.h.md)[Previous](glsmap-smaptexdim.c.md)

