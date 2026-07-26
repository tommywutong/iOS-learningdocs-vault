---
title: readWriteTextureSupport
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 11.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtldevice/readwritetexturesupport
source_url: 'https://developer.apple.com/documentation/metal/mtldevice/readwritetexturesupport'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtldevice/readwritetexturesupport.json'
content_hash: 'sha256:db3d5aa2d2a33f47'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLDevice](../mtldevice.md)

# readWriteTextureSupport

<sub>Instance Property</sub>

The GPU device’s texture support tier.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var readWriteTextureSupport: MTLReadWriteTextureTier { get }
```

## Topics

### Read-write texture tiers

- [MTLReadWriteTextureTier](../mtlreadwritetexturetier.md) — The support level for read-write texture formats.

## See Also

### Checking texture and sampler support

- [supports32BitFloatFiltering](supports32bitfloatfiltering.md) — A Boolean value that indicates whether the GPU can filter a texture with a 32-bit floating-point format.
- [supportsBCTextureCompression](supportsbctexturecompression.md) — A Boolean value that indicates whether you can use textures that use BC compression.
- [depth24Stencil8PixelFormatSupported](isdepth24stencil8pixelformatsupported.md) — A Boolean value that indicates whether a device supports a packed depth-and-stencil pixel format. _(deprecated)_
- [supportsQueryTextureLOD](supportsquerytexturelod.md) — A Boolean value that indicates whether you can query the texture level of detail from within a shader.
