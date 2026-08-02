---
title: ConditionalRendering
apple_id: DTS40010087
resource_type: Sample Code
platform: macOS
topic: Graphics & Animation
technology: OpenGL
published: '2014-06-17'
source_url: https://developer.apple.com/library/archive/samplecode/ConditionalRendering/Listings/ConditionalRender_fs.html
archived_at: '2026-07-18T03:04:13.539335Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [ConditionalRendering](ConditionalRendering.md)


[Next](ConditionalRender.vs.md)[Previous](color.vs.md)

# ConditionalRender.fs

```
#version 150

flat in vec3 normal;
in vec4 eyePos;
in vec4 primaryColor;

uniform vec3 lightPos;
uniform vec3 lightColor;

out vec4 fragColor;

void main()
{
    vec3 view = normalize(-eyePos.xyz);
    vec3 L = normalize(lightPos-eyePos.xyz);
    float attenuation = max(0.0, dot(L, normal));
    vec3 reflectvec = normalize(reflect(-L, normal));
    float spec = max(dot(reflectvec, view),0.0);
    fragColor = primaryColor + vec4(min(pow(spec, 32.0)+attenuation*lightColor, 1.0), 1);
}
```

[Next](ConditionalRender.vs.md)[Previous](color.vs.md)

