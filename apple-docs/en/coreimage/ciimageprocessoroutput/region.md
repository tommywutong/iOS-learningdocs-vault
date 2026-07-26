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
doc_path: /documentation/coreimage/ciimageprocessoroutput/region
source_url: 'https://developer.apple.com/documentation/coreimage/ciimageprocessoroutput/region'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/ciimageprocessoroutput/region.json'
content_hash: 'sha256:61687ff99654e8b3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIImageProcessorOutput](../ciimageprocessoroutput.md)

# region

<sub>Instance Property</sub>

The rectangular region of the output image that your Core Image Processor Kernel must provide.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var region: CGRect { get }
```

## Discussion

> [!note] Note
> This may be different (larger or smaller) than the `extent` that was passed to `/CIImageProcessorKernel/applyWithExtent:inputs:arguments:error:`.

## See Also

### Getting Supplemental Information for Image Processing

- [metalCommandBuffer](metalcommandbuffer.md) — Returns a Metal command buffer object that can be used for encoding commands.
- [bytesPerRow](bytesperrow.md) — The bytes per row of the CPU memory that your Core Image Processor Kernel can write pixels to.
- [format](format.md) — The pixel format of the CPU memory that your Core Image Processor Kernel can write pixels to.
