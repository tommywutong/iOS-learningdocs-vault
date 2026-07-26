---
title: region
framework: Core Image
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.12+, tvOS 10.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coreimage/ciimageprocessorinput/region
source_url: 'https://developer.apple.com/documentation/coreimage/ciimageprocessorinput/region'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/ciimageprocessorinput/region.json'
content_hash: 'sha256:a65560a69d5c0ffb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIImageProcessorInput](../ciimageprocessorinput.md)

# region

<sub>Instance Property</sub>

The rectangular region of the input image that your Core Image Processor Kernel can use to provide the output.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var region: CGRect { get }
```

## Discussion

> [!note] Note
> This will contain but may be larger than the rect returned by ‘roiCallback’.

## See Also

### Getting Supplemental Information for Image Processing

- [bytesPerRow](bytesperrow.md) — The bytes per row of the CPU memory that your Core Image Processor Kernel can read pixelsfrom.
- [format](format.md) — The pixel format of the CPU memory that your Core Image Processor Kernel can read pixels from.
