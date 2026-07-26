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
doc_path: /documentation/coreimage/ciimageprocessorinput/pixelbuffer
source_url: 'https://developer.apple.com/documentation/coreimage/ciimageprocessorinput/pixelbuffer'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/ciimageprocessorinput/pixelbuffer.json'
content_hash: 'sha256:a2b16867df62dc47'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIImageProcessorInput](../ciimageprocessorinput.md)

# pixelBuffer

<sub>Instance Property</sub>

An input pixel buffer object that your Core Image Processor Kernel can read from.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var pixelBuffer: CVPixelBuffer? { get }
```

## Discussion

> [!warning] Warning
> This buffer must not be modified by the [CIImageProcessorKernel](../ciimageprocessorkernel.md).

## See Also

### Accessing Input Image Data

- [baseAddress](baseaddress.md) — The base address of CPU memory that your Core Image Processor Kernel can read pixels from.
- [metalTexture](metaltexture.md) — A MTLTexture object that can be bound for input using Metal.
- [surface](surface.md) — An input surface object that your Core Image Processor Kernel can read from.
