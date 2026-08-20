---
title: SceneKit's presentation for WWDC2013
apple_id: DTS40013423
resource_type: Sample Code
platform: macOS
topic: Graphics & Animation
technology: SceneKit
published: '2014-01-07'
source_url: https://developer.apple.com/library/archive/samplecode/SceneKit_Slides_WWDC2013/Listings/Scene_Kit_Session_WWDC_2013_Resources_Shaders_SceneDelegate_fsh.html
archived_at: '2026-07-18T03:23:19.825905Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [SceneKit's presentation for WWDC2013](Scene%20Kit%27s%20presentation%20for%20WWDC2013.md)


[Next](Scene%20Kit%20Session%20WWDC%202013-Resources-Shaders-SceneDelegate.vsh.md)[Previous](Scene%20Kit%20Session%20WWDC%202013-Resources-Shaders-ParticleSystem.vsh.md)

# Scene Kit Session WWDC 2013/Resources/Shaders/SceneDelegate.fsh

```
uniform vec2 resolution;
uniform float time;
uniform float factor;

const float lineCount = 10.;
const float bias = 0.5;
const float sharpness = 4.0;
const float smoothness = 0.05;

float sharpen(float v, float dist) {
    float d = smoothness + pow(abs(1. - dist),4.) * 0.5;
    return smoothstep(0.5 - d,.5 + d, v);
}

void main(void) {
    vec2 position = (( gl_FragCoord.xy / resolution.xy ) - vec2(0.5));
    vec4 color = vec4(1.0);
    vec2 abspos = abs(position * 2.);
    float depth = clamp(sqrt(abspos.y*abspos.y + abspos.x*abspos.x), 0., 2.);
    float lc = mix(lineCount*2., lineCount, depth);
    vec2 pos = mod((abspos*.5-.75) * lc - time*2.0, 1.);

    float mx = 0.5;
    float ao = 1.0;

    if (abs(position.x) > abs(position.y)) {
        mx = abs(1.-sharpen(abs(pos.x*2. - 1.), depth) - sharpen(abs(mod(abspos.y / abspos.x * lineCount * 0.5, 2.)-1.), abspos.x));
        ao = 1. - abspos.y / abspos.x;
        ao *= clamp(abspos.x*abspos.x, 0., 1.);
    } else {
        mx = abs(1.-sharpen(abs(pos.y*2. - 1.), depth) - sharpen(abs(mod(abspos.x / abspos.y * lineCount * 0.5, 2.)-1.), abspos.y));
        ao = 1. - abspos.x / abspos.y;
        ao *= clamp(abspos.y*abspos.y, 0., 1.);
    }
    color.rgb = mix(vec3(0.1, 0.3, 0.1), vec3( .9, .3, 0.1 ), mx);
    color.rgb *= 0.5 * depth * factor * pow(ao, 0.35);
    gl_FragColor = color;
}
```

[Next](Scene%20Kit%20Session%20WWDC%202013-Resources-Shaders-SceneDelegate.vsh.md)[Previous](Scene%20Kit%20Session%20WWDC%202013-Resources-Shaders-ParticleSystem.vsh.md)

