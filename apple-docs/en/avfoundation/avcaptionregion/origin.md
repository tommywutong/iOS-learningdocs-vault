---
title: origin
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 15.0+, macOS 12.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcaptionregion/origin
source_url: 'https://developer.apple.com/documentation/avfoundation/avcaptionregion/origin'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcaptionregion/origin.json'
content_hash: 'sha256:8a163677da21e458'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptionRegion](../avcaptionregion.md)

# origin

<sub>Instance Property</sub>

The region’s top-left position.

<sub>iOS, iPadOS, Mac Catalyst, macOS</sub>

```swift
var origin: AVCaptionPoint { get }
```

## Discussion

The caption’s origin may not provide undefined [x](../avcaptionpoint/x.md) and [y](../avcaptionpoint/y.md) values, which indicates the region doesn’t have positioning information for that dimension.

## See Also

### Accessing the location

- [AVCaptionPoint](../avcaptionpoint.md) — A structure that defines the origin point for a caption.
