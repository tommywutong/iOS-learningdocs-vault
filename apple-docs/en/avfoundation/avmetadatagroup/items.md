---
title: items
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avmetadatagroup/items
source_url: 'https://developer.apple.com/documentation/avfoundation/avmetadatagroup/items'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avmetadatagroup/items.json'
content_hash: 'sha256:6b52f364be4dc634'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVMetadataGroup](../avmetadatagroup.md)

# items

<sub>Instance Property</sub>

The array of metadata items associated with the metadata group.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var items: [AVMetadataItem] { get }
```

## Discussion

The `items` array may be empty if no metadata items are associated with this group.

## See Also

### Inspecting the metadata group

- [uniqueID](uniqueid.md) — The unique identifier for the metadata group.
- [classifyingLabel](classifyinglabel.md) — The classifying label associated with the metadata group.
