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
doc_path: /documentation/avfoundation/avmutabletimedmetadatagroup/items
source_url: 'https://developer.apple.com/documentation/avfoundation/avmutabletimedmetadatagroup/items'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avmutabletimedmetadatagroup/items.json'
content_hash: 'sha256:f1c8261d95293a3a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVMutableTimedMetadataGroup](../avmutabletimedmetadatagroup.md)

# items

<sub>Instance Property</sub>

An array of metadata items in the timed metadata group.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var items: [AVMetadataItem] { get set }
```

## Discussion

The array contains instances of [AVMetadataItem](../avmetadataitem.md).

## See Also

### Configuring the group

- [timeRange](timerange.md) — The time range of the timed metadata.
