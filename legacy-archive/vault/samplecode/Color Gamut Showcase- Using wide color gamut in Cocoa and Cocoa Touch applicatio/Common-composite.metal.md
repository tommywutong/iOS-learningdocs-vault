---
title: 'Color Gamut Showcase: Using wide color gamut in Cocoa and Cocoa Touch applications
  with SceneKit'
apple_id: TP40017308
resource_type: Sample Code
platform: iOS|macOS
topic: null
technology: SceneKit
published: '2016-09-28'
source_url: https://developer.apple.com/library/archive/samplecode/ColorGamutShowcase/Listings/Common_composite_metal.html
archived_at: '2026-07-18T03:03:56.270699Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Color Gamut Showcase: Using wide color gamut in Cocoa and Cocoa Touch applications with SceneKit](Color%20Gamut%20Showcase-%20Using%20wide%20color%20gamut%20in%20Cocoa%20and%20Cocoa%20Touch%20applicatio.md)


[Next](iOS-ViewController.swift.md)[Previous](Common-Controller.swift.md)

# Common/composite.metal

```c

#include <metal_stdlib>
using namespace metal;

enum visualization_type { gamutClamp = 0, wideGamutHighlight };
struct uniforms_t {
    float splitFraction;
    float2 imageSize;
    int visualizationType;
};

struct draw_quad_io_t {
    float4 position [[ position ]];
    float2 uv;
};

/// Letterboxing
static float4 letterboxedColor(float2 uv, float2 imageSize, texture2d<float> texture) {
    constexpr sampler nearest_sampler;

    // Adjust texture coordinates according to the screen and image aspect ratios
    float2 scale = float2(1.0);

    float imageAspectRatio = imageSize.x / imageSize.y;
    float screenAspectRatio = float(texture.get_width()) / float(texture.get_height());

    if (imageAspectRatio > screenAspectRatio) {
        scale.y = imageAspectRatio / screenAspectRatio;
    }
    else {
        scale.x = screenAspectRatio / imageAspectRatio;
    }

    uv = 0.5 + scale * (uv - 0.5);

    // Black bars for texture coordinates that are not in the [0, 1] range
    if (uv.x < 0 || uv.x > 1 || uv.y < 0 || uv.y > 1) {
        return float4(0, 0, 0, 1);
    }

    return texture.sample(nearest_sampler, uv);
}

static bool isWideGamut(float value) {
    return value > 1.0 || value < 0.0;
}

/// Computes the final color according to the position of the split handle
static float4 finalColor(float2 uv, float splitFraction, float4 wideGamutColor, int visualizationType) {
    float lineItensity = smoothstep(0.0, 0.001, abs(uv.x - splitFraction));
    float4 lineColor = float4(lineItensity, lineItensity, lineItensity, 1);

    float4 color;

    if (uv.x < splitFraction) {
        switch (visualizationType) {
            case gamutClamp:
                // Clamp the color to 0.0 to 1.0, removing wide gamut colors
                color = saturate(wideGamutColor);
                break;
            case wideGamutHighlight:
                if (isWideGamut(wideGamutColor[0]) || isWideGamut(wideGamutColor[1]) || isWideGamut(wideGamutColor[2])) {
                    // If the color is wide gamut, fully display it.
                    color = wideGamutColor;
                } else {
                    // Otherwise grayscale the non-wide gamut colors.
                    float luminance = dot(float3(0.3, 0.59, 0.11), wideGamutColor.rgb);
                    color = float4(luminance, luminance, luminance, 1.);
                }
                break;
        }
    } else {
        color = wideGamutColor;
    }

    return color * lineColor;
}

/// The fragment shader that draws the final result
fragment float4 composite_frag(draw_quad_io_t       in                [[ stage_in   ]],
                               texture2d<float>     wideGamutTexture  [[ texture(0) ]],
                               constant uniforms_t& uniforms          [[ buffer(0)  ]])
{
    float4 wideGamutColor = letterboxedColor(in.uv, uniforms.imageSize, wideGamutTexture);
    return finalColor(in.uv, uniforms.splitFraction, wideGamutColor, uniforms.visualizationType);
}

/// The vertex shader that draws a fullscreen quad by deriving
/// a vertex's position and texture coordinates from its ID
vertex draw_quad_io_t composite_vert(uint v_id [[ vertex_id ]])
{
    draw_quad_io_t out;

    out.position = float4((v_id / 2) * 2.0 - 1.0,
                          (v_id % 2) * 2.0 - 1.0,
                          0.0,
                          1.0);

    out.uv = float2(v_id / 2,
                    1 - v_id % 2);

    return out;
}
```

[Next](iOS-ViewController.swift.md)[Previous](Common-Controller.swift.md)

