---
title: items
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 4.3+, iPadOS 4.3+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avtimedmetadatagroup/items
source_url: 'https://developer.apple.com/documentation/avfoundation/avtimedmetadatagroup/items'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avtimedmetadatagroup/items.json'
content_hash: 'sha256:5509c0c246ea985b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVTimedMetadataGroup](../avtimedmetadatagroup.md)

# items

<sub>Instance Property</sub>

An array of metadata items in the timed metadata group.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var items: [AVMetadataItem] { get }
```

## Discussion

The array contains instances of [AVMetadataItem](../avmetadataitem.md).

## See Also

### Accessing group attributes

- [timeRange](timerange.md) — The time range for the timed metadata.
