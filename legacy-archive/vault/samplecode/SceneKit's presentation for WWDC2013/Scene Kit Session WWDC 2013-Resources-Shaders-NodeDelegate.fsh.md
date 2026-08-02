---
title: SceneKit's presentation for WWDC2013
apple_id: DTS40013423
resource_type: Sample Code
platform: macOS
topic: Graphics & Animation
technology: SceneKit
published: '2014-01-07'
source_url: https://developer.apple.com/library/archive/samplecode/SceneKit_Slides_WWDC2013/Listings/Scene_Kit_Session_WWDC_2013_Resources_Shaders_NodeDelegate_fsh.html
archived_at: '2026-07-18T03:23:19.646596Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [SceneKit's presentation for WWDC2013](Scene%20Kit%27s%20presentation%20for%20WWDC2013.md)


[Next](Scene%20Kit%20Session%20WWDC%202013-Resources-Shaders-NodeDelegate.vsh.md)[Previous](Scene%20Kit%20Session%20WWDC%202013-Resources-Shaders-CustomProgram.vsh.md)

# Scene Kit Session WWDC 2013/Resources/Shaders/NodeDelegate.fsh

```
varying vec2 v_angleAndLife;

void main(void) {
    float alpha = pow(v_angleAndLife.x, 1.5);
    gl_FragColor = vec4(1.0, 1.0, 1.0, alpha);
}
```

[Next](Scene%20Kit%20Session%20WWDC%202013-Resources-Shaders-NodeDelegate.vsh.md)[Previous](Scene%20Kit%20Session%20WWDC%202013-Resources-Shaders-CustomProgram.vsh.md)

