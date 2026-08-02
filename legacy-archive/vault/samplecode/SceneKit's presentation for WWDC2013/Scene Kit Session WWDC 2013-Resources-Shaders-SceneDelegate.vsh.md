---
title: SceneKit's presentation for WWDC2013
apple_id: DTS40013423
resource_type: Sample Code
platform: macOS
topic: Graphics & Animation
technology: SceneKit
published: '2014-01-07'
source_url: https://developer.apple.com/library/archive/samplecode/SceneKit_Slides_WWDC2013/Listings/Scene_Kit_Session_WWDC_2013_Resources_Shaders_SceneDelegate_vsh.html
archived_at: '2026-07-18T03:23:19.865682Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [SceneKit's presentation for WWDC2013](Scene%20Kit%27s%20presentation%20for%20WWDC2013.md)


[Next](Scene%20Kit%20Session%20WWDC%202013-Sources-ASCPresentationViewController.h.md)[Previous](Scene%20Kit%20Session%20WWDC%202013-Resources-Shaders-SceneDelegate.fsh.md)

# Scene Kit Session WWDC 2013/Resources/Shaders/SceneDelegate.vsh

```
attribute vec4 position;
attribute vec2 texcoord0;

varying vec2 v_uv;

void main(void) {
    gl_Position = position;
    v_uv = texcoord0;
}
```

[Next](Scene%20Kit%20Session%20WWDC%202013-Sources-ASCPresentationViewController.h.md)[Previous](Scene%20Kit%20Session%20WWDC%202013-Resources-Shaders-SceneDelegate.fsh.md)

