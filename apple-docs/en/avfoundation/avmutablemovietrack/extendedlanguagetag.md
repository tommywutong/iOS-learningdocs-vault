---
title: extendedLanguageTag
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.11+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avmutablemovietrack/extendedlanguagetag
source_url: 'https://developer.apple.com/documentation/avfoundation/avmutablemovietrack/extendedlanguagetag'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avmutablemovietrack/extendedlanguagetag.json'
content_hash: 'sha256:04afd04a42e84402'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVMutableMovieTrack](../avmutablemovietrack.md)

# extendedLanguageTag

<sub>Instance Property</sub>

The language tag of the track.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
var extendedLanguageTag: String? { get set }
```

## Discussion

The value is a [BCP-47](https://tools.ietf.org/html/bcp47) language tag, or `nil` if the track doesn’t specify a language tag.

## See Also

### Accessing language support

- [languageCode](languagecode.md) — The language code of the track.
