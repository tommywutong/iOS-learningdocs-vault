---
title: bytesPerRow
framework: Core Image
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.12+, tvOS 10.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coreimage/ciimageprocessoroutput/bytesperrow
source_url: 'https://developer.apple.com/documentation/coreimage/ciimageprocessoroutput/bytesperrow'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/ciimageprocessoroutput/bytesperrow.json'
content_hash: 'sha256:16ee93876224fcab'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIImageProcessorOutput](../ciimageprocessoroutput.md)

# bytesPerRow

<sub>Instance Property</sub>

The bytes per row of the CPU memory that your Core Image Processor Kernel can write pixels to.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var bytesPerRow: Int { get }
```

## See Also

### Getting Supplemental Information for Image Processing

- [region](region.md) — The rectangular region of the output image that your Core Image Processor Kernel must provide.
- [metalCommandBuffer](metalcommandbuffer.md) — Returns a Metal command buffer object that can be used for encoding commands.
- [format](format.md) — The pixel format of the CPU memory that your Core Image Processor Kernel can write pixels to.
