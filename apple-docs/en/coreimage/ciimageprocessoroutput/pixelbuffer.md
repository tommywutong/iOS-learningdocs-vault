---
title: pixelBuffer
framework: Core Image
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.12+, tvOS 10.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coreimage/ciimageprocessoroutput/pixelbuffer
source_url: 'https://developer.apple.com/documentation/coreimage/ciimageprocessoroutput/pixelbuffer'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/ciimageprocessoroutput/pixelbuffer.json'
content_hash: 'sha256:af530c79f3d5e41d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIImageProcessorOutput](../ciimageprocessoroutput.md)

# pixelBuffer

<sub>Instance Property</sub>

An output pixelBuffer object that your Core Image Processor Kernel can write to.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var pixelBuffer: CVPixelBuffer? { get }
```

## See Also

### Providing Output Image Data

- [baseAddress](baseaddress.md) — The base address of CPU memory that your Core Image Processor Kernel can write pixels to.
- [metalTexture](metaltexture.md) — A Metal texture object that can be bound for output using Metal.
- [surface](surface.md) — An output surface object that your Core Image Processor Kernel can write to.
