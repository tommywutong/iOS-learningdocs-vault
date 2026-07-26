---
title: languageCode
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avassetwriterinput/languagecode
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetwriterinput/languagecode'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetwriterinput/languagecode.json'
content_hash: 'sha256:a4016270516433a0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetWriterInput](../avassetwriterinput.md)

# languageCode

<sub>Instance Property</sub>

The language code of the input’s track.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var languageCode: String? { get set }
```

## Discussion

Specify an ISO 639-2/T language code value, or `nil` to prevent the writer from writing a language code.

## See Also

### Configuring language support

- [extendedLanguageTag](extendedlanguagetag.md) — The extended language for the input’s track.
