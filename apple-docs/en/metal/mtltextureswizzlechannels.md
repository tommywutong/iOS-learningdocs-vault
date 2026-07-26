---
title: MTLTextureSwizzleChannels
framework: Metal
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtltextureswizzlechannels
source_url: 'https://developer.apple.com/documentation/metal/mtltextureswizzlechannels'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtltextureswizzlechannels.json'
content_hash: 'sha256:3628ecc45160d245'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTLTextureSwizzleChannels

<sub>Structure</sub>

A pattern that modifies the data read or sampled from a texture by rearranging or duplicating the elements of a vector.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
struct MTLTextureSwizzleChannels
```

## Overview

Use this structure to specify a custom swizzle pattern when creating a new texture or texture view.

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Sendable](../swift/sendable.md)

## Topics

### Creating a swizzle pattern

- [init()](<mtltextureswizzlechannels/init().md>) — Creates a default swizzle pattern.
- [init(red:green:blue:alpha:)](<mtltextureswizzlechannels/init(red_green_blue_alpha_).md>) — Creates a swizzle pattern.

### Specifying swizzle values

- [red](mtltextureswizzlechannels/red.md) — The data copied to the first output channel.
- [green](mtltextureswizzlechannels/green.md) — The data copied to the second output channel.
- [blue](mtltextureswizzlechannels/blue.md) — The data copied to the third output channel.
- [alpha](mtltextureswizzlechannels/alpha.md) — The data copied to the fourth output channel.

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
