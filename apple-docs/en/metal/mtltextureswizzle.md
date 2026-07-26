---
title: MTLTextureSwizzle
framework: Metal
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtltextureswizzle
source_url: 'https://developer.apple.com/documentation/metal/mtltextureswizzle'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtltextureswizzle.json'
content_hash: 'sha256:205c94d5378ca72b'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTLTextureSwizzle

<sub>Enumeration</sub>

A set of options to choose from when creating a texture swizzle pattern.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
enum MTLTextureSwizzle
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Specifying swizzle channels

- [MTLTextureSwizzleAlpha](mtltextureswizzle/alpha.md) — The alpha channel of the source pixel is copied to the destination channel.
- [MTLTextureSwizzleBlue](mtltextureswizzle/blue.md) — The blue channel of the source pixel is copied to the destination channel.
- [MTLTextureSwizzleGreen](mtltextureswizzle/green.md) — The green channel of the source pixel is copied to the destination channel.
- [MTLTextureSwizzleRed](mtltextureswizzle/red.md) — The red channel of the source pixel is copied to the destination channel.
- [MTLTextureSwizzleOne](mtltextureswizzle/one.md) — A value of `1.0` is copied to the destination channel.
- [MTLTextureSwizzleZero](mtltextureswizzle/zero.md) — A value of `0.0` is copied to the destination channel.

### Initializers

- [init(rawValue:)](<mtltextureswizzle/init(rawvalue_).md>)

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
