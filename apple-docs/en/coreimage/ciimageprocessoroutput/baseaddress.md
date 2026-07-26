---
title: baseAddress
framework: Core Image
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.12+, tvOS 10.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coreimage/ciimageprocessoroutput/baseaddress
source_url: 'https://developer.apple.com/documentation/coreimage/ciimageprocessoroutput/baseaddress'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/ciimageprocessoroutput/baseaddress.json'
content_hash: 'sha256:88b4b0e38e5b7ed2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIImageProcessorOutput](../ciimageprocessoroutput.md)

# baseAddress

<sub>Instance Property</sub>

The base address of CPU memory that your Core Image Processor Kernel can write pixels to.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var baseAddress: UnsafeMutableRawPointer { get }
```

## See Also

### Providing Output Image Data

- [metalTexture](metaltexture.md) — A Metal texture object that can be bound for output using Metal.
- [pixelBuffer](pixelbuffer.md) — An output pixelBuffer object that your Core Image Processor Kernel can write to.
- [surface](surface.md) — An output surface object that your Core Image Processor Kernel can write to.
