---
title: GLUT
apple_id: DTS10000528
resource_type: Sample Code
platform: macOS
topic: Graphics & Animation
technology: OpenGL
published: '2008-02-08'
source_url: https://developer.apple.com/library/archive/samplecode/glut/Listings/glsmap_smap_drawmesh_c.html
archived_at: '2026-07-18T03:29:18.446379Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [GLUT](GLUT.md)


[Next](glsmap-smapflag.c.md)[Previous](glsmap-smapdestroy.c.md)

# glsmap/smap_drawmesh.c

```c

/* Copyright (c) Mark J. Kilgard, 1998.  */

/* This program is freely distributable without licensing fees
   and is provided without guarantee or warrantee expressed or
   implied. This program is -not- in the public domain. */

#include <glsmap.h>

#include "glsmapint.h"

void
__smapDrawSphereMapMeshSide(SphereMapMesh *mesh, int side)
{
    INITFACE(mesh);
    int i, j;

    for (i=0; i<mesh->steps-1; i++) {
        glBegin(GL_QUAD_STRIP);
        for (j=0; j<mesh->steps; j++) {
            glTexCoord2fv (FACEst(side,i,j));
            glVertex2fv   (FACExy(side,i,j));
            glTexCoord2fv (FACEst(side,i+1,j));
            glVertex2fv   (FACExy(side,i+1,j));
        }
        glEnd();
    }
}

/* Back face specially rendered for its singularity! */
void
__smapDrawSphereMapMeshBack(SphereMapMesh *mesh)
{
    INITBACK(mesh);
    int side, i, j;

    for (side=0; side<4; side++) {
        for (j=0; j<mesh->rings-1+mesh->edgeExtend; j++) {
            glBegin(GL_QUAD_STRIP);
            for (i=0; i<mesh->steps; i++) {
                glTexCoord2fv (BACKst(side,j,i));
                glVertex2fv   (BACKxy(side,j,i));
                glTexCoord2fv (BACKst(side,j+1,i));
                glVertex2fv   (BACKxy(side,j+1,i));
            }
            glEnd();
        }
    }
}
```

[Next](glsmap-smapflag.c.md)[Previous](glsmap-smapdestroy.c.md)

