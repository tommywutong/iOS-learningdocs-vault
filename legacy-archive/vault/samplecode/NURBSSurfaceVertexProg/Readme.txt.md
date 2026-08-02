---
title: NURBSSurfaceVertexProg
apple_id: DTS10000535
resource_type: Sample Code
platform: macOS
topic: Graphics & Animation
technology: OpenGL
published: '2003-07-07'
source_url: https://developer.apple.com/library/archive/samplecode/NURBSSurfaceVertexProg/Listings/Readme_txt.html
archived_at: '2026-07-18T03:16:50.553310Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [NURBSSurfaceVertexProg](NURBSSurfaceVertexProg.md)


[Next](main.m.md)[Previous](NURBSSurfaceVertexProg.md)

# Readme.txt

```
Press mouse button to select and rotate
Press control mouse button to select and translate
Press shift / mouse button to select a control point 

This demonstrates the use of vertex programs for NURBS using a 4x4 NURB.

Nurbs Surface Demo

    This demo uses a vertex program to compute the vertex position for a NURB surface. The example uses
    a 4x4 control mesh to define a NURBS surface.

    The host CPU generates a UV surface with the the u and v basis functions in the vertex position and
    and color. The routine that builds the UV surface is CreateNURBSUVSurface which is called once, NURB
    basis functions are generated in CreateBSpliineBasis which is a recursive routine that computes the
    basis function from n to 1.

    Once the basis functions have been computed and inserted into the UV mesh a the control points are
    loaded to the GPU using glProgramLocalParameter4fvARB(GL_VERTEX_PROGRAM_ARB, ...) then drawn to using
    a glDrawElements command.

    The UV mesh is then evaluated on the GPU using the vertex program NURBSSurface.vsh (in Resources).
```

[Next](main.m.md)[Previous](NURBSSurfaceVertexProg.md)

