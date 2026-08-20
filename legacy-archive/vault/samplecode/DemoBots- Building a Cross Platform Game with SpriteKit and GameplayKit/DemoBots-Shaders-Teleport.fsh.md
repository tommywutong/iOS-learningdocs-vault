---
title: 'DemoBots: Building a Cross Platform Game with SpriteKit and GameplayKit'
apple_id: TP40015179
resource_type: Sample Code
platform: tvOS|iOS|macOS
topic: Graphics & Animation
technology: SpriteKit
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/samplecode/DemoBots/Listings/DemoBots_Shaders_Teleport_fsh.html
archived_at: '2026-07-18T03:06:21.754083Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [DemoBots: Building a Cross Platform Game with SpriteKit and GameplayKit](DemoBots-%20Building%20a%20Cross%20Platform%20Game%20with%20SpriteKit%20and%20GameplayKit.md)


[Next](DemoBots-LevelSceneSuccessState.swift.md)[Previous](DemoBots-SceneLoaderResourcesAvailableState.swift.md)

# DemoBots/Shaders/Teleport.fsh

```
// Mixes color with luma-coefficient grayscale
vec3 colorMix(vec3 color, float time) {
    float gray = dot(color, vec3(0.2126, 0.7152, 0.0722));
    return mix(vec3(gray), color, time);
}

// Main
void main(void) {
    float time = fract(u_time/u_duration);

    vec4 texture = texture2D(u_texture, v_tex_coord);

    // Mixed color
    vec3 color = colorMix(texture.rgb, time);

    float num = sin(360.0*(1.0-time))*256.0;
    float line = floor(num*v_tex_coord.y);
    float bin = mod(line, 2.0);

    vec4 almost = mix(vec4(color, texture.a)*time, texture*vec4(bin), bin);

    if (almost.a <= 0.2) {
        almost.a = 0.0;
    }

    gl_FragColor = vec4(almost.rgb + vec3(0,(1.0-time)*0.25,(1.0-time)*0.5) * almost.a, almost.a);
}
```

[Next](DemoBots-LevelSceneSuccessState.swift.md)[Previous](DemoBots-SceneLoaderResourcesAvailableState.swift.md)

