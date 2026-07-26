---
title: isDepth24Stencil8PixelFormatSupported
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [Mac Catalyst 13.0+（27.0 起废弃）, macOS 10.11+（27.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/metal/mtldevice/isdepth24stencil8pixelformatsupported
source_url: 'https://developer.apple.com/documentation/metal/mtldevice/isdepth24stencil8pixelformatsupported'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtldevice/isdepth24stencil8pixelformatsupported.json'
content_hash: 'sha256:ef552679e6b4d753'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLDevice](../mtldevice.md)

# isDepth24Stencil8PixelFormatSupported

<sub>Instance Property</sub>

A Boolean value that indicates whether a device supports a packed depth-and-stencil pixel format.

> [!warning] Deprecated
> Never supported on Apple Silicon

<sub>Mac Catalyst, macOS</sub>

```swift
var isDepth24Stencil8PixelFormatSupported: Bool { get }
```

## Discussion

If the value is [true](../../swift/true.md), the device supports the [MTLPixelFormatDepth24Unorm_Stencil8](../mtlpixelformat/depth24unorm_stencil8.md) pixel format.

## See Also

### Related Documentation

- [Metal Shading Language Guide](https://developer.apple.com/library/archive/documentation/Metal/Reference/MetalShadingLanguageGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40014364)
- [Metal Programming Guide](https://developer.apple.com/library/archive/documentation/Miscellaneous/Conceptual/MetalProgrammingGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40014221)

### Checking texture and sampler support

- [supports32BitFloatFiltering](supports32bitfloatfiltering.md) — A Boolean value that indicates whether the GPU can filter a texture with a 32-bit floating-point format.
- [supportsBCTextureCompression](supportsbctexturecompression.md) — A Boolean value that indicates whether you can use textures that use BC compression.
- [supportsQueryTextureLOD](supportsquerytexturelod.md) — A Boolean value that indicates whether you can query the texture level of detail from within a shader.
- [readWriteTextureSupport](readwritetexturesupport.md) — The GPU device’s texture support tier.
