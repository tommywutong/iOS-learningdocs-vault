---
title: isPlayable
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 10.8+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avmediaselectionoption/isplayable
source_url: 'https://developer.apple.com/documentation/avfoundation/avmediaselectionoption/isplayable'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avmediaselectionoption/isplayable.json'
content_hash: 'sha256:354db202e4df901d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVMediaSelectionOption](../avmediaselectionoption.md)

# isPlayable

<sub>Instance Property</sub>

A Boolean value that indicates whether the media selection option is playable.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var isPlayable: Bool { get }
```

## Discussion

If the media data associated with the option cannot be decoded or otherwise rendered, the value of this property is [false](../../swift/false.md).
