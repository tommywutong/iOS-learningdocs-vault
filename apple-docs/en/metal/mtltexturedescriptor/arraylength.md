---
title: arrayLength
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtltexturedescriptor/arraylength
source_url: 'https://developer.apple.com/documentation/metal/mtltexturedescriptor/arraylength'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtltexturedescriptor/arraylength.json'
content_hash: 'sha256:a5eb20e0c15c3f82'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLTextureDescriptor](../mtltexturedescriptor.md)

# arrayLength

<sub>Instance Property</sub>

The number of array elements for this texture.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var arrayLength: Int { get set }
```

## Discussion

The value of this property needs to be between `1` and `2048`, inclusive. The default value is `1`.

This value is `1` if the texture type is not an array.

This value can be between `1` and `2048` if the texture type is one of the following array types:

- [MTLTextureType1DArray](../mtltexturetype/type1darray.md)
- [MTLTextureType2DArray](../mtltexturetype/type2darray.md)
- [MTLTextureType2DMultisampleArray](../mtltexturetype/type2dmultisamplearray.md)
- [MTLTextureTypeCubeArray](../mtltexturetype/typecubearray.md)

## See Also

### Specifying texture attributes

- [textureType](texturetype.md) — The dimension and arrangement of texture image data.
- [pixelFormat](pixelformat.md) — The size and bit layout of all pixels in the texture.
- [width](width.md) — The width of the texture image for the base level mipmap, in pixels.
- [height](height.md) — The height of the texture image for the base level mipmap, in pixels.
- [depth](depth.md) — The depth of the texture image for the base level mipmap, in pixels.
- [mipmapLevelCount](mipmaplevelcount.md) — The number of mipmap levels for this texture.
- [sampleCount](samplecount.md) — The number of samples in each fragment.
- [resourceOptions](resourceoptions.md) — The behavior of a new memory allocation.
- [cpuCacheMode](cpucachemode.md) — The CPU cache mode used for the CPU mapping of the texture.
- [storageMode](storagemode.md) — The location and access permissions of the texture.
- [hazardTrackingMode](hazardtrackingmode.md) — The texture’s hazard tracking mode.
- [allowGPUOptimizedContents](allowgpuoptimizedcontents.md) — A Boolean value indicating whether the GPU is allowed to adjust the texture’s contents to improve GPU performance.
- [usage](usage.md) — Options that determine how you can use the texture.
- [swizzle](swizzle.md) — The pattern you want the GPU to apply to pixels when you read or sample pixels from the texture.
- [MTLTextureSwizzleChannels](../mtltextureswizzlechannels.md) — A pattern that modifies the data read or sampled from a texture by rearranging or duplicating the elements of a vector.
