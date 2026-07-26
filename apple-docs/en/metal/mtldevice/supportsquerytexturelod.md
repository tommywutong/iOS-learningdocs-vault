---
title: supportsQueryTextureLOD
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtldevice/supportsquerytexturelod
source_url: 'https://developer.apple.com/documentation/metal/mtldevice/supportsquerytexturelod'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtldevice/supportsquerytexturelod.json'
content_hash: 'sha256:563c37af8fb53978'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLDevice](../mtldevice.md)

# supportsQueryTextureLOD

<sub>Instance Property</sub>

A Boolean value that indicates whether you can query the texture level of detail from within a shader.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var supportsQueryTextureLOD: Bool { get }
```

## See Also

### Checking texture and sampler support

- [supports32BitFloatFiltering](supports32bitfloatfiltering.md) — A Boolean value that indicates whether the GPU can filter a texture with a 32-bit floating-point format.
- [supportsBCTextureCompression](supportsbctexturecompression.md) — A Boolean value that indicates whether you can use textures that use BC compression.
- [depth24Stencil8PixelFormatSupported](isdepth24stencil8pixelformatsupported.md) — A Boolean value that indicates whether a device supports a packed depth-and-stencil pixel format. _(deprecated)_
- [readWriteTextureSupport](readwritetexturesupport.md) — The GPU device’s texture support tier.
