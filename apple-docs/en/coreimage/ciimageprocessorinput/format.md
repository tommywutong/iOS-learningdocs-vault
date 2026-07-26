---
title: format
framework: Core Image
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.12+, tvOS 10.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coreimage/ciimageprocessorinput/format
source_url: 'https://developer.apple.com/documentation/coreimage/ciimageprocessorinput/format'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/ciimageprocessorinput/format.json'
content_hash: 'sha256:bb46475b61107748'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIImageProcessorInput](../ciimageprocessorinput.md)

# format

<sub>Instance Property</sub>

The pixel format of the CPU memory that your Core Image Processor Kernel can read pixels from.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var format: CIFormat { get }
```

## See Also

### Getting Supplemental Information for Image Processing

- [region](region.md) — The rectangular region of the input image that your Core Image Processor Kernel can use to provide the output.
- [bytesPerRow](bytesperrow.md) — The bytes per row of the CPU memory that your Core Image Processor Kernel can read pixelsfrom.
