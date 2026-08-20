---
title: GLUT
apple_id: DTS10000528
resource_type: Sample Code
platform: macOS
topic: Graphics & Animation
technology: OpenGL
published: '2008-02-08'
source_url: https://developer.apple.com/library/archive/samplecode/glut/Listings/glsmap_smap_destroy_c.html
archived_at: '2026-07-18T03:29:18.415509Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [GLUT](GLUT.md)


[Next](glsmap-smapdrawmesh.c.md)[Previous](glsmap-smapcreate.c.md)

# glsmap/smap_destroy.c

```c

/* Copyright (c) Mark J. Kilgard, 1998.  */

/* This program is freely distributable without licensing fees
   and is provided without guarantee or warrantee expressed or
   implied. This program is -not- in the public domain. */

#include <assert.h>
#include <stdlib.h>

#include "glsmapint.h"

static void
derefSphereMapMesh(SphereMapMesh *mesh)
{
    assert(mesh->refcnt > 0);
    mesh->refcnt--;
    if (mesh->refcnt == 0) {
        if (mesh->face) {
            assert(mesh->back ==
                &(mesh->face[5*mesh->steps*mesh->steps]));
            free(mesh->face);
        }
        free(mesh);
    }
}

void
smapDestroySphereMap(SphereMap *smap)
{
    derefSphereMapMesh(smap->mesh);
    free(smap);
}
```

[Next](glsmap-smapdrawmesh.c.md)[Previous](glsmap-smapcreate.c.md)

