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
doc_path: /documentation/avfoundation/avmetadataitem/locale
source_url: 'https://developer.apple.com/documentation/avfoundation/avmetadataitem/locale'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avmetadataitem/locale.json'
content_hash: 'sha256:fb312d74e4c58c3b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVMetadataItem](../avmetadataitem.md)

# locale

<sub>Instance Property</sub>

The locale of the metadata item.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var locale: Locale? { get }
```

## Discussion

The locale may be `nil` if no locale information is available for the metadata item.

## See Also

### Accessing language support

- [extendedLanguageTag](extendedlanguagetag.md) — The IETF BCP 47 (RFC 4646) language identifier of the metadata item.
