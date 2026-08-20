---
title: GLUT
apple_id: DTS10000528
resource_type: Sample Code
platform: macOS
topic: Graphics & Animation
technology: OpenGL
published: '2008-02-08'
source_url: https://developer.apple.com/library/archive/samplecode/glut/Listings/glsmap_smap_create_c.html
archived_at: '2026-07-18T03:29:18.362347Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [GLUT](GLUT.md)


[Next](glsmap-smapdestroy.c.md)[Previous](glsmap-smapcontext.c.md)

# glsmap/smap_create.c

```c

/* Copyright (c) Mark J. Kilgard, 1998.  */

/* This program is freely distributable without licensing fees
   and is provided without guarantee or warrantee expressed or
   implied. This program is -not- in the public domain. */

#include <glsmap.h>
#include <stdlib.h>

#include "glsmapint.h"

static SphereMapMesh *
createSphereMapMesh(void)
{
    SphereMapMesh *mesh;

    mesh = (SphereMapMesh*) malloc(sizeof(SphereMapMesh));

    mesh->steps = 8;
    mesh->rings = 3;
    mesh->edgeExtend = 1;

    mesh->face = NULL;
    mesh->back = NULL;

    mesh->refcnt = 0;

    return mesh;
}

static void
refSphereMapMesh(SphereMapMesh *mesh)
{
    mesh->refcnt++;
}

SphereMap *
smapCreateSphereMap(SphereMap *shareSmap)
{
    SphereMap *smap;
    int i;

    smap = (SphereMap*) malloc(sizeof(SphereMap));

    if (shareSmap) {
        smap->mesh = shareSmap->mesh;
    } else {
        smap->mesh = createSphereMapMesh();
    }
    refSphereMapMesh(smap->mesh);

    /* Default texture objects. */
    smap->smapTexObj = 1001;
    for (i=0; i<6; i++) {
        smap->viewTexObjs[i] = i+1002;
    }
    smap->viewTexObj = 1008;

    /* Default texture dimensions 64x64 */
    smap->viewTexDim = 64;
    smap->smapTexDim = 64;

    /* Default origin at lower left. */
    smap->viewOrigin[X] = 0;
    smap->viewOrigin[Y] = 0;
    smap->smapOrigin[X] = 0;
    smap->smapOrigin[Y] = 0;

        /* Flags. */
        smap->flags = (SphereMapFlags) 0;

    /* Default eye vector. */
    smap->eye[X] = 0.0;
    smap->eye[Y] = 0.0;
    smap->eye[Z] = -10.0;

    /* Default up vector. */
    smap->up[X] = 0.0;
    smap->up[Y] = 0.1;
    smap->up[Z] = 0.0;

    /* Default object location vector. */
    smap->obj[X] = 0.0;
    smap->obj[Y] = 0.0;
    smap->obj[Z] = 0.0;

    /* Default near and far clip planes. */
    smap->viewNear = 0.1;
    smap->viewFar = 20.0;

    smap->positionLights = NULL;
    smap->drawView = NULL;

    smap->context = NULL;

    return smap;
}
```

[Next](glsmap-smapdestroy.c.md)[Previous](glsmap-smapcontext.c.md)

