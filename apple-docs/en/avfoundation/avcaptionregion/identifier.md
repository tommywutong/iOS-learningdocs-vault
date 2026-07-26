---
title: identifier
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 15.0+, macOS 12.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcaptionregion/identifier
source_url: 'https://developer.apple.com/documentation/avfoundation/avcaptionregion/identifier'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcaptionregion/identifier.json'
content_hash: 'sha256:728cfec8e8855ac1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptionRegion](../avcaptionregion.md)

# identifier

<sub>Instance Property</sub>

A string that identifies the region.

<sub>iOS, iPadOS, Mac Catalyst, macOS</sub>

```swift
var identifier: String? { get }
```

## Discussion

The system considers two regions the same if their region identifier is equal. Your app needs to ensure that equal caption regions have the same property values.

If this value is `nil`, the system instead treats two regions equal if their `position` and `endPosition` are the same. Captions referring to these regions belong to the same region when the system serializes them to a format like TTML.
