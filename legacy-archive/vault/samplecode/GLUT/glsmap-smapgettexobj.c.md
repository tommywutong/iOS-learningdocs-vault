---
title: GLUT
apple_id: DTS10000528
resource_type: Sample Code
platform: macOS
topic: Graphics & Animation
technology: OpenGL
published: '2008-02-08'
source_url: https://developer.apple.com/library/archive/samplecode/glut/Listings/glsmap_smap_gettexobj_c.html
archived_at: '2026-07-18T03:29:18.683591Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [GLUT](GLUT.md)


[Next](glsmap-smapgetvec.c.md)[Previous](glsmap-smapgettexdim.c.md)

# glsmap/smap_gettexobj.c

```c

/* Copyright (c) Mark J. Kilgard, 1998.  */

/* This program is freely distributable without licensing fees
   and is provided without guarantee or warrantee expressed or
   implied. This program is -not- in the public domain. */

#include "glsmapint.h"

void
smapGetSphereMapTexObj(SphereMap *smap, GLuint *texobj)
{
    *texobj = smap->smapTexObj;
}

void
smapGetViewTexObj(SphereMap *smap, GLuint *texobj)
{
    *texobj = smap->viewTexObj;
}

void
smapGetViewTexObjs(SphereMap *smap, GLuint texobjs[6])
{
    int i;

    for (i=0; i<6; i++) {
        texobjs[i] = smap->viewTexObjs[i];
    }
}
```

[Next](glsmap-smapgetvec.c.md)[Previous](glsmap-smapgettexdim.c.md)

