---
title: surface
framework: Core Image
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.12+, tvOS 10.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coreimage/ciimageprocessorinput/surface
source_url: 'https://developer.apple.com/documentation/coreimage/ciimageprocessorinput/surface'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/ciimageprocessorinput/surface.json'
content_hash: 'sha256:8bb264cb24cff69e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIImageProcessorInput](../ciimageprocessorinput.md)

# surface

<sub>Instance Property</sub>

An input surface object that your Core Image Processor Kernel can read from.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var surface: IOSurfaceRef { get }
```

## Discussion

> [!warning] Warning
> This surface must not be modified by the [CIImageProcessorKernel](../ciimageprocessorkernel.md).

## See Also

### Accessing Input Image Data

- [baseAddress](baseaddress.md) — The base address of CPU memory that your Core Image Processor Kernel can read pixels from.
- [metalTexture](metaltexture.md) — A MTLTexture object that can be bound for input using Metal.
- [pixelBuffer](pixelbuffer.md) — An input pixel buffer object that your Core Image Processor Kernel can read from.
