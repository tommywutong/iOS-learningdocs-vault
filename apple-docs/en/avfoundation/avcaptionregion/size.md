---
title: size
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 15.0+, macOS 12.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcaptionregion/size
source_url: 'https://developer.apple.com/documentation/avfoundation/avcaptionregion/size'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcaptionregion/size.json'
content_hash: 'sha256:13abd02ca3ab0e3a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptionRegion](../avcaptionregion.md)

# size

<sub>Instance Property</sub>

The height and width of the region.

<sub>iOS, iPadOS, Mac Catalyst, macOS</sub>

```swift
var size: AVCaptionSize { get }
```

## Discussion

CEA608 closed captions limit the [height](../avcaptionsize/height.md) property’s value to 1 cell, except when the value of its [scroll](scroll-swift.property.md) property is [AVCaptionRegionScrollRollUp](scroll-swift.enum/rollup.md). In this case, the [height](../avcaptionsize/height.md) property’s value must be 2, 3 or 4 cells.

> [!note] Note
> The caption size has an unspecified height and width when the region doesn’t have width or height information.

## See Also

### Accessing the size

- [AVCaptionSize](../avcaptionsize.md) — A structure that defines the height and width of a caption.
