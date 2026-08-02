---
title: SceneKit slides for WWDC 2014
apple_id: TP40014551
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2014-10-16'
source_url: https://developer.apple.com/library/archive/samplecode/SceneKitWWDC2014/Listings/Scene_Kit_Session_WWDC_2014_Resources_Shaders_SceneDelegate_vsh.html
archived_at: '2026-07-18T03:23:14.035548Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [SceneKit slides for WWDC 2014](SceneKit%20slides%20for%20WWDC%202014.md)


[Next](Scene%20Kit%20Session%20WWDC%202014-Resources-Shaders-ParticleSystem.vsh.md)[Previous](Scene%20Kit%20Session%20WWDC%202014-Resources-Scenes.scnassets-earth-Credit.txt.md)

# Scene Kit Session WWDC 2014/Resources/Shaders/SceneDelegate.vsh

```
attribute vec4 position;
attribute vec2 texcoord0;

varying vec2 v_uv;

void main(void) {
    gl_Position = position;
    v_uv = texcoord0;
}
```

[Next](Scene%20Kit%20Session%20WWDC%202014-Resources-Shaders-ParticleSystem.vsh.md)[Previous](Scene%20Kit%20Session%20WWDC%202014-Resources-Scenes.scnassets-earth-Credit.txt.md)

