---
title: allowGPUOptimizedContents
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 13.1+, macOS 10.14+, tvOS 12.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtltexturedescriptor/allowgpuoptimizedcontents
source_url: 'https://developer.apple.com/documentation/metal/mtltexturedescriptor/allowgpuoptimizedcontents'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtltexturedescriptor/allowgpuoptimizedcontents.json'
content_hash: 'sha256:78da5653c3f88128'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLTextureDescriptor](../mtltexturedescriptor.md)

# allowGPUOptimizedContents

<sub>Instance Property</sub>

A Boolean value indicating whether the GPU is allowed to adjust the texture’s contents to improve GPU performance.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var allowGPUOptimizedContents: Bool { get set }
```

## Discussion

The default value is `true`, which means that the Metal device is allowed to adjust the private layout of the texture in memory to improve GPU performance. For a shared or managed texture, this optimization can cause slower performance when accessing the texture from the CPU. Setting this property to `false` improves CPU performance at the cost of some GPU performance.

## See Also

### Specifying texture attributes

- [textureType](texturetype.md) — The dimension and arrangement of texture image data.
- [pixelFormat](pixelformat.md) — The size and bit layout of all pixels in the texture.
- [width](width.md) — The width of the texture image for the base level mipmap, in pixels.
- [height](height.md) — The height of the texture image for the base level mipmap, in pixels.
- [depth](depth.md) — The depth of the texture image for the base level mipmap, in pixels.
- [mipmapLevelCount](mipmaplevelcount.md) — The number of mipmap levels for this texture.
- [sampleCount](samplecount.md) — The number of samples in each fragment.
- [arrayLength](arraylength.md) — The number of array elements for this texture.
- [resourceOptions](resourceoptions.md) — The behavior of a new memory allocation.
- [cpuCacheMode](cpucachemode.md) — The CPU cache mode used for the CPU mapping of the texture.
- [storageMode](storagemode.md) — The location and access permissions of the texture.
- [hazardTrackingMode](hazardtrackingmode.md) — The texture’s hazard tracking mode.
- [usage](usage.md) — Options that determine how you can use the texture.
- [swizzle](swizzle.md) — The pattern you want the GPU to apply to pixels when you read or sample pixels from the texture.
- [MTLTextureSwizzleChannels](../mtltextureswizzlechannels.md) — A pattern that modifies the data read or sampled from a texture by rearranging or duplicating the elements of a vector.
