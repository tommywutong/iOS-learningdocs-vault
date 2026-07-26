---
title: extendedLanguageTag
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avmutablemetadataitem/extendedlanguagetag
source_url: 'https://developer.apple.com/documentation/avfoundation/avmutablemetadataitem/extendedlanguagetag'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avmutablemetadataitem/extendedlanguagetag.json'
content_hash: 'sha256:26da0abbc12be435'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVMutableMetadataItem](../avmutablemetadataitem.md)

# extendedLanguageTag

<sub>Instance Property</sub>

The IETF BCP 47 (RFC 4646) language identifier of the metadata item.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var extendedLanguageTag: String? { get set }
```

## Discussion

The value may be `nil` if no language tag information is available.

## See Also

### Accessing language support

- [locale](locale.md) — The locale for a mutable metadata item.
