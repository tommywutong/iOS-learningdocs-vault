---
title: OpenCL N-Body Simulation
apple_id: TP40016610
resource_type: Sample Code
platform: macOS
topic: Graphics & Animation
technology: OpenCL
published: '2015-12-10'
source_url: https://developer.apple.com/library/archive/samplecode/OpenCL_NBody_Simulation/Listings/Sources_Shaders_NBody_nbody_fsh.html
archived_at: '2026-07-18T03:17:43.630231Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [OpenCL N-Body Simulation](OpenCL%20N-Body%20Simulation.md)


[Next](Sources-View-OpenGLView.mm.md)[Previous](Sources-Shaders-NBody-nbody.vsh.md)

# Sources/Shaders/NBody/nbody.fsh

```
/*
 <codex>
 <abstract>
 Fragment shader for display splat texture.
 </abstract>
 </codex>
 */

uniform sampler2D splatTexture;

void main()
{
    gl_FragColor = texture2D(splatTexture, gl_TexCoord[0].st) * gl_Color;
}
```

[Next](Sources-View-OpenGLView.mm.md)[Previous](Sources-Shaders-NBody-nbody.vsh.md)

