---
title: startDate
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avmutablemetadataitem/startdate
source_url: 'https://developer.apple.com/documentation/avfoundation/avmutablemetadataitem/startdate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avmutablemetadataitem/startdate.json'
content_hash: 'sha256:f15903f095aca85c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVMutableMetadataItem](../avmutablemetadataitem.md)

# startDate

<sub>Instance Property</sub>

The start date of the timed metadata.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var startDate: Date? { get set }
```

## Discussion

The value is `nil` if the metadata item doesn’t provide a start date.

## See Also

### Accessing timing

- [time](time.md) — The timestamp for a mutable metadata item.
- [duration](duration.md) — The duration of a mutable metadata item.
