---
title: GLUT
apple_id: DTS10000528
resource_type: Sample Code
platform: macOS
topic: Graphics & Animation
technology: OpenGL
published: '2008-02-08'
source_url: https://developer.apple.com/library/archive/samplecode/glut/Listings/glsmap_smap_texdim_c.html
archived_at: '2026-07-18T03:29:19.089264Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [GLUT](GLUT.md)


[Next](glsmap-smaptexobj.c.md)[Previous](glsmap-smapsetvec.c.md)

# glsmap/smap_texdim.c

```c

/* Copyright (c) Mark J. Kilgard, 1998.  */

/* This program is freely distributable without licensing fees
   and is provided without guarantee or warrantee expressed or
   implied. This program is -not- in the public domain. */

#include "glsmapint.h"

void
smapSetSphereMapTexDim(SphereMap *smap, GLsizei texdim)
{
    smap->smapTexDim = texdim;
}

void
smapSetViewTexDim(SphereMap *smap, GLsizei texdim)
{
    smap->viewTexDim = texdim;
}
```

[Next](glsmap-smaptexobj.c.md)[Previous](glsmap-smapsetvec.c.md)

