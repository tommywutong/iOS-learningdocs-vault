---
title: extendedLanguageTag
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcompositiontrack/extendedlanguagetag
source_url: 'https://developer.apple.com/documentation/avfoundation/avcompositiontrack/extendedlanguagetag'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcompositiontrack/extendedlanguagetag.json'
content_hash: 'sha256:2a8a4279188cbc67'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCompositionTrack](../avcompositiontrack.md)

# extendedLanguageTag

<sub>Instance Property</sub>

The language tag of the track.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var extendedLanguageTag: String? { get }
```

## Discussion

The value is a [BCP-47](https://tools.ietf.org/html/bcp47) language tag, or `nil` if the track doesn’t specify a language tag.

## See Also

### Accessing language support

- [languageCode](languagecode.md) — The language code of the track.
