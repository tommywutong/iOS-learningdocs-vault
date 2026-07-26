---
title: extendedLanguageTag
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avassetwriterinput/extendedlanguagetag
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetwriterinput/extendedlanguagetag'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetwriterinput/extendedlanguagetag.json'
content_hash: 'sha256:a6ae61ee36d74de5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetWriterInput](../avassetwriterinput.md)

# extendedLanguageTag

<sub>Instance Property</sub>

The extended language for the input’s track.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var extendedLanguageTag: String? { get set }
```

## Discussion

Extended language tags are normally set only when an ISO 639-2/T language code alone is ambiguous. For example, you may use an extended language tag to distinguish media by the regional dialect in use or the writing system employed.

Specify the value as an RFC 4646 language tag, or `nil` to prevent the writer from writing an extended language tag.

## See Also

### Configuring language support

- [languageCode](languagecode.md) — The language code of the input’s track.
