---
title: DeferredShading
apple_id: DTS40010088
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2015-07-08'
source_url: https://developer.apple.com/library/archive/samplecode/DeferredShading/Listings/deferredLighting_fs.html
archived_at: '2026-07-18T03:06:11.666506Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [DeferredShading](DeferredShading.md)


[Next](bufferDisplay.fs.md)[Previous](Readme.md.md)

# deferredLighting.fs

```
/*
 Copyright (C) 2015 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 The application delegate.
 */

#version 150

uniform sampler2D normalTex, posTex, colorTex;
uniform vec3 light1Pos;
uniform vec3 light1Color;
uniform vec3 light2Pos;
uniform vec3 light2Color;
uniform vec3 light3Pos;
uniform vec3 light3Color;
uniform vec3 light4Pos;
uniform vec3 light4Color;

in vec3 texCoord;
out vec4 fragColor;

void main()
{
    vec4 color = texture(colorTex, texCoord.xy);
    //drop out early if there's nothing to draw
    if(color.a < 0.00001)
    {
        discard;
    }

    //pull normal x and y from texture
    vec2 norm = texture(normalTex, texCoord.xy).xy;
    //reconstruct the normal
    vec3 normal = vec3(norm.xy, 0.0);
    normal.z = sqrt(1.0 - norm.x*norm.x-norm.y*norm.y);

    //pull out the position
    vec3 position = texture(posTex,texCoord.xy).xyz;
    vec3 view = normalize(-position);

    //light 1
    vec3 L = normalize(light1Pos-position);
    float attenuation1 = max(0.0, dot(L, normal));
    //specular
    vec3 reflectvec = normalize(reflect(-L, normal));
    float spec = max(dot(reflectvec, view),0.0);
    //light 2
    vec3 L2 = normalize(light2Pos-position);
    float attenuation2 = max(0.0, dot(L2, normal));
    //specular
    vec3 reflectvec2 = normalize(reflect(-L2, normal));
    float spec2 = max(dot(reflectvec2, view),0.0);

    vec3 L3 = normalize(light3Pos-position);
    float attenuation3 = max(0.0, dot(L3, normal));
    //specular
    vec3 reflectvec3 = normalize(reflect(-L3, normal));
    float spec3 = max(dot(reflectvec3, view),0.0);
    //light 4
    vec3 L4 = normalize(light4Pos-position);
    float attenuation4 = max(0.0, dot(L4, normal));
    //specular
    vec3 reflectvec4 = normalize(reflect(-L4, normal));
    float spec4 = max(dot(reflectvec4, view),0.0);

    fragColor = color +
                    (vec4(min(pow(spec, 32.0)+attenuation1*light1Color, 1.0), 1)+
                    vec4(min(pow(spec2, 32.0)+attenuation2*light2Color, 1.0), 1)+
                    vec4(min(pow(spec3, 32.0)+attenuation3*light3Color, 1.0), 1)+
                    vec4(min(pow(spec4, 32.0)+attenuation4*light4Color, 1.0), 1));
}
```

[Next](bufferDisplay.fs.md)[Previous](Readme.md.md)

