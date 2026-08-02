---
title: OpenCL N-Body Simulation
apple_id: TP40016610
resource_type: Sample Code
platform: macOS
topic: Graphics & Animation
technology: OpenCL
published: '2015-12-10'
source_url: https://developer.apple.com/library/archive/samplecode/OpenCL_NBody_Simulation/Listings/Sources_Shaders_Star_star_vsh.html
archived_at: '2026-07-18T03:17:43.736156Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [OpenCL N-Body Simulation](OpenCL%20N-Body%20Simulation.md)


[Next](Sources-Shaders-NBody-nbody.vsh.md)[Previous](Sources-Shaders-Star-star.fsh.md)

# Sources/Shaders/Star/star.vsh

```
/*
 <codex>
 <abstract>
 Vertex shader for stars.
 </abstract>
 </codex>
 */

void main()
{
    gl_FrontColor = gl_Color;
    gl_TexCoord[0] = gl_MultiTexCoord0;
    gl_Position = ftransform();
}
```

[Next](Sources-Shaders-NBody-nbody.vsh.md)[Previous](Sources-Shaders-Star-star.fsh.md)

