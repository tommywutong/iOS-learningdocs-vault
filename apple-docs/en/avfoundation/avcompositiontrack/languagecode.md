---
title: languageCode
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcompositiontrack/languagecode
source_url: 'https://developer.apple.com/documentation/avfoundation/avcompositiontrack/languagecode'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcompositiontrack/languagecode.json'
content_hash: 'sha256:d666be03845ae992'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCompositionTrack](../avcompositiontrack.md)

# languageCode

<sub>Instance Property</sub>

The language code of the track.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var languageCode: String? { get }
```

## Discussion

The value is an ISO 639-2/T language code, or `nil` if the track doesn’t specify a language code.

## See Also

### Accessing language support

- [extendedLanguageTag](extendedlanguagetag.md) — The language tag of the track.
