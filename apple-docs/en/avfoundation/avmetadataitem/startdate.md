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
doc_path: /documentation/avfoundation/avmetadataitem/startdate
source_url: 'https://developer.apple.com/documentation/avfoundation/avmetadataitem/startdate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avmetadataitem/startdate.json'
content_hash: 'sha256:1878a7e4b12fa136'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVMetadataItem](../avmetadataitem.md)

# startDate

<sub>Instance Property</sub>

The start date of the timed metadata.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var startDate: Date? { get }
```

## Discussion

The value is `nil` if the metadata item doesn’t provide a start date.

## See Also

### Accessing timing

- [time](time.md) — The timestamp of the metadata item.
- [duration](duration.md) — The duration of the metadata item.
