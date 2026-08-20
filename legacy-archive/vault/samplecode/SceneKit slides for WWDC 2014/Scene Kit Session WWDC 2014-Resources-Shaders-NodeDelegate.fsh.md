---
title: SceneKit slides for WWDC 2014
apple_id: TP40014551
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2014-10-16'
source_url: https://developer.apple.com/library/archive/samplecode/SceneKitWWDC2014/Listings/Scene_Kit_Session_WWDC_2014_Resources_Shaders_NodeDelegate_fsh.html
archived_at: '2026-07-18T03:23:13.833139Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [SceneKit slides for WWDC 2014](SceneKit%20slides%20for%20WWDC%202014.md)


[Next](LICENSE.txt.md)[Previous](Scene%20Kit%20Session%20WWDC%202014-Resources-Shaders-ParticleSystem.fsh.md)

# Scene Kit Session WWDC 2014/Resources/Shaders/NodeDelegate.fsh

```
varying vec2 v_angleAndLife;

void main(void) {
    float alpha = pow(v_angleAndLife.x, 1.5);
    gl_FragColor = vec4(1.0, 1.0, 1.0, alpha);
}
```

[Next](LICENSE.txt.md)[Previous](Scene%20Kit%20Session%20WWDC%202014-Resources-Shaders-ParticleSystem.fsh.md)

