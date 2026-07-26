---
title: supports32BitFloatFiltering
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtldevice/supports32bitfloatfiltering
source_url: 'https://developer.apple.com/documentation/metal/mtldevice/supports32bitfloatfiltering'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtldevice/supports32bitfloatfiltering.json'
content_hash: 'sha256:dff4a2a55f4c6202'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLDevice](../mtldevice.md)

# supports32BitFloatFiltering

<sub>Instance Property</sub>

A Boolean value that indicates whether the GPU can filter a texture with a 32-bit floating-point format.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var supports32BitFloatFiltering: Bool { get }
```

## See Also

### Checking texture and sampler support

- [supportsBCTextureCompression](supportsbctexturecompression.md) — A Boolean value that indicates whether you can use textures that use BC compression.
- [depth24Stencil8PixelFormatSupported](isdepth24stencil8pixelformatsupported.md) — A Boolean value that indicates whether a device supports a packed depth-and-stencil pixel format. _(deprecated)_
- [supportsQueryTextureLOD](supportsquerytexturelod.md) — A Boolean value that indicates whether you can query the texture level of detail from within a shader.
- [readWriteTextureSupport](readwritetexturesupport.md) — The GPU device’s texture support tier.
