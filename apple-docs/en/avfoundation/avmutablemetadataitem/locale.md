---
title: locale
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avmutablemetadataitem/locale
source_url: 'https://developer.apple.com/documentation/avfoundation/avmutablemetadataitem/locale'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avmutablemetadataitem/locale.json'
content_hash: 'sha256:88a2ac834973af23'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVMutableMetadataItem](../avmutablemetadataitem.md)

# locale

<sub>Instance Property</sub>

The locale for a mutable metadata item.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var locale: Locale? { get set }
```

## Discussion

The locale may be `nil` if no locale information is available for the item.

## See Also

### Accessing language support

- [extendedLanguageTag](extendedlanguagetag.md) — The IETF BCP 47 (RFC 4646) language identifier of the metadata item.
