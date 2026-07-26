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
doc_path: /documentation/coreimage/ciimageprocessorinput/baseaddress
source_url: 'https://developer.apple.com/documentation/coreimage/ciimageprocessorinput/baseaddress'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/ciimageprocessorinput/baseaddress.json'
content_hash: 'sha256:1af09a29bcf511b9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIImageProcessorInput](../ciimageprocessorinput.md)

# baseAddress

<sub>Instance Property</sub>

The base address of CPU memory that your Core Image Processor Kernel can read pixels from.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var baseAddress: UnsafeRawPointer { get }
```

## Discussion

> [!warning] Warning
> This memory must not be modified by the [CIImageProcessorKernel](../ciimageprocessorkernel.md).

## See Also

### Accessing Input Image Data

- [metalTexture](metaltexture.md) — A MTLTexture object that can be bound for input using Metal.
- [pixelBuffer](pixelbuffer.md) — An input pixel buffer object that your Core Image Processor Kernel can read from.
- [surface](surface.md) — An input surface object that your Core Image Processor Kernel can read from.
