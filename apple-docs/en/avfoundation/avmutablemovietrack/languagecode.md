---
title: languageCode
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.11+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avmutablemovietrack/languagecode
source_url: 'https://developer.apple.com/documentation/avfoundation/avmutablemovietrack/languagecode'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avmutablemovietrack/languagecode.json'
content_hash: 'sha256:26d4372aff61cce7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVMutableMovieTrack](../avmutablemovietrack.md)

# languageCode

<sub>Instance Property</sub>

The language code of the track.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
var languageCode: String? { get set }
```

## Discussion

The value is an ISO 639-2/T language code, or `nil` if the track doesn’t specify a language code.

## See Also

### Accessing language support

- [extendedLanguageTag](extendedlanguagetag.md) — The language tag of the track.
