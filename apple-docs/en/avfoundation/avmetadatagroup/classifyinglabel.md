---
title: classifyingLabel
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 9.3+, iPadOS 9.3+, Mac Catalyst 13.1+, macOS 10.11.3+, tvOS 9.2+, visionOS 1.0+, watchOS 2.3+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avmetadatagroup/classifyinglabel
source_url: 'https://developer.apple.com/documentation/avfoundation/avmetadatagroup/classifyinglabel'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avmetadatagroup/classifyinglabel.json'
content_hash: 'sha256:db904c18a84cb4f1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVMetadataGroup](../avmetadatagroup.md)

# classifyingLabel

<sub>Instance Property</sub>

The classifying label associated with the metadata group.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var classifyingLabel: String? { get }
```

## Discussion

The value of this property may be `nil` if no classifying label is defined for this group.

## See Also

### Inspecting the metadata group

- [items](items.md) — The array of metadata items associated with the metadata group.
- [uniqueID](uniqueid.md) — The unique identifier for the metadata group.
