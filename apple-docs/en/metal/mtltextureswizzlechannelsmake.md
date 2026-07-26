---
title: MTLTextureSwizzleChannelsMake
framework: Metal
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtltextureswizzlechannelsmake
source_url: 'https://developer.apple.com/documentation/metal/mtltextureswizzlechannelsmake'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtltextureswizzlechannelsmake.json'
content_hash: 'sha256:1619b55e120f62ed'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTLTextureSwizzleChannelsMake

<sub>Function</sub>

Creates a new swizzle pattern.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```objc
static MTLTextureSwizzleChannels MTLTextureSwizzleChannelsMake(MTLTextureSwizzle r, MTLTextureSwizzle g, MTLTextureSwizzle b, MTLTextureSwizzle a);
```

## Parameters

- `r` — The data you want to copy to the first output channel

- `g` — The data you want to copy to the second output channel

- `b` — The data you want to copy to the third output channel

- `a` — The data you want to copy to the fourth output channel

## Return Value

A texture swizzle pattern.

## See Also

### Specifying texture attributes

- [textureType](mtltexturedescriptor/texturetype.md) — The dimension and arrangement of texture image data.
- [pixelFormat](mtltexturedescriptor/pixelformat.md) — The size and bit layout of all pixels in the texture.
- [width](mtltexturedescriptor/width.md) — The width of the texture image for the base level mipmap, in pixels.
- [height](mtltexturedescriptor/height.md) — The height of the texture image for the base level mipmap, in pixels.
- [depth](mtltexturedescriptor/depth.md) — The depth of the texture image for the base level mipmap, in pixels.
- [mipmapLevelCount](mtltexturedescriptor/mipmaplevelcount.md) — The number of mipmap levels for this texture.
- [sampleCount](mtltexturedescriptor/samplecount.md) — The number of samples in each fragment.
- [arrayLength](mtltexturedescriptor/arraylength.md) — The number of array elements for this texture.
- [resourceOptions](mtltexturedescriptor/resourceoptions.md) — The behavior of a new memory allocation.
- [cpuCacheMode](mtltexturedescriptor/cpucachemode.md) — The CPU cache mode used for the CPU mapping of the texture.
- [storageMode](mtltexturedescriptor/storagemode.md) — The location and access permissions of the texture.
- [hazardTrackingMode](mtltexturedescriptor/hazardtrackingmode.md) — The texture’s hazard tracking mode.
- [allowGPUOptimizedContents](mtltexturedescriptor/allowgpuoptimizedcontents.md) — A Boolean value indicating whether the GPU is allowed to adjust the texture’s contents to improve GPU performance.
- [usage](mtltexturedescriptor/usage.md) — Options that determine how you can use the texture.
- [swizzle](mtltexturedescriptor/swizzle.md) — The pattern you want the GPU to apply to pixels when you read or sample pixels from the texture.
