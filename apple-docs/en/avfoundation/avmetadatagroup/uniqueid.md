---
title: uniqueID
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 9.3+, iPadOS 9.3+, Mac Catalyst 13.1+, macOS 10.11.3+, tvOS 9.2+, visionOS 1.0+, watchOS 2.3+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avmetadatagroup/uniqueid
source_url: 'https://developer.apple.com/documentation/avfoundation/avmetadatagroup/uniqueid'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avmetadatagroup/uniqueid.json'
content_hash: 'sha256:45f6574bb5c99db6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVMetadataGroup](../avmetadatagroup.md)

# uniqueID

<sub>Instance Property</sub>

The unique identifier for the metadata group.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var uniqueID: String? { get }
```

## Discussion

The value of this property may be `nil` if no unique identifier is defined for this group.

## See Also

### Inspecting the metadata group

- [items](items.md) — The array of metadata items associated with the metadata group.
- [classifyingLabel](classifyinglabel.md) — The classifying label associated with the metadata group.
