---
title: metalCommandBuffer
framework: Core Image
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.12+, tvOS 10.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coreimage/ciimageprocessoroutput/metalcommandbuffer
source_url: 'https://developer.apple.com/documentation/coreimage/ciimageprocessoroutput/metalcommandbuffer'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/ciimageprocessoroutput/metalcommandbuffer.json'
content_hash: 'sha256:cb5282e6383816f3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIImageProcessorOutput](../ciimageprocessoroutput.md)

# metalCommandBuffer

<sub>Instance Property</sub>

Returns a Metal command buffer object that can be used for encoding commands.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var metalCommandBuffer: (any MTLCommandBuffer)? { get }
```

## See Also

### Getting Supplemental Information for Image Processing

- [region](region.md) — The rectangular region of the output image that your Core Image Processor Kernel must provide.
- [bytesPerRow](bytesperrow.md) — The bytes per row of the CPU memory that your Core Image Processor Kernel can write pixels to.
- [format](format.md) — The pixel format of the CPU memory that your Core Image Processor Kernel can write pixels to.
