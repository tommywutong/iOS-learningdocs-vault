---
title: Passing IOSurfaces from one process to another via Mach RPC
apple_id: DTS40010132
resource_type: Sample Code
platform: macOS
topic: Graphics & Animation
technology: OpenGL
published: '2014-10-13'
source_url: https://developer.apple.com/library/archive/samplecode/MultiGPUIOSurface/Listings/Shaders_lighting_vsh.html
archived_at: '2026-07-18T03:16:26.460843Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Passing IOSurfaces from one process to another via Mach RPC](Passing%20IOSurfaces%20from%20one%20process%20to%20another%20via%20Mach%20RPC.md)


[Next](Shaders-texture.vsh.md)[Previous](Shaders-color.vsh.md)

# Shaders/lighting.vsh

```
#version 150

in vec4 inVertex, inColor;
in vec3 inNormal;

out vec4 color;

uniform mat4 MVP, ModelView;
uniform mat3 ModelViewIT;
uniform vec3 lightDir;
uniform vec4 ambient, diffuse, specular;
uniform float shininess;

void main()
{
    // transform position to clip space
    gl_Position = MVP * inVertex;

    // transform position to eye space
    vec3 eyePosition = vec3(ModelView * inVertex);

    // transform normal to eye space (normalization skipped here: inNormal already normalized, matrix not scaled)
    vec3 eyeNormal = ModelViewIT * inNormal;

    // directional light ambient and diffuse contribution (lightDir alreay normalized)
    float NdotL = max(dot(eyeNormal, lightDir), 0.0);
    vec4 lightColor = ambient + diffuse * NdotL;

    if (NdotL > 0.0)
    {
        // half angle
        vec3 H = normalize(lightDir - normalize(eyePosition));

        // specular contribution
        float NdotH = max(dot(eyeNormal, H), 0.0);
        lightColor += specular * pow(NdotH, shininess);
    }

    // apply directional light color and saturate result
    // to match fixed function behavior
    color = min(inColor * lightColor, 1.0);
}
```

[Next](Shaders-texture.vsh.md)[Previous](Shaders-color.vsh.md)

