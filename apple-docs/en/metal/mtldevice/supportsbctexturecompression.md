---
title: supportsBCTextureCompression
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 16.4+, iPadOS 16.4+, Mac Catalyst 16.4+, macOS 11.0+, tvOS 16.4+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtldevice/supportsbctexturecompression
source_url: 'https://developer.apple.com/documentation/metal/mtldevice/supportsbctexturecompression'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtldevice/supportsbctexturecompression.json'
content_hash: 'sha256:a03c1f1523d1ce7e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLDevice](../mtldevice.md)

# supportsBCTextureCompression

<sub>Instance Property</sub>

A Boolean value that indicates whether you can use textures that use BC compression.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var supportsBCTextureCompression: Bool { get }
```

## See Also

### Checking texture and sampler support

- [supports32BitFloatFiltering](supports32bitfloatfiltering.md) — A Boolean value that indicates whether the GPU can filter a texture with a 32-bit floating-point format.
- [depth24Stencil8PixelFormatSupported](isdepth24stencil8pixelformatsupported.md) — A Boolean value that indicates whether a device supports a packed depth-and-stencil pixel format. _(deprecated)_
- [supportsQueryTextureLOD](supportsquerytexturelod.md) — A Boolean value that indicates whether you can query the texture level of detail from within a shader.
- [readWriteTextureSupport](readwritetexturesupport.md) — The GPU device’s texture support tier.
