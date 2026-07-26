---
title: languageCode
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avpartialasyncproperty/languagecode
source_url: 'https://developer.apple.com/documentation/avfoundation/avpartialasyncproperty/languagecode'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avpartialasyncproperty/languagecode.json'
content_hash: 'sha256:3f9e715d62160a9d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPartialAsyncProperty](../avpartialasyncproperty.md)

# languageCode

<sub>Type Property</sub>

The language code of the track.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var languageCode: AVAsyncProperty<Root, String?> { get }
```

## Discussion

Use the [load(_:isolation:)](<../avasynchronouskeyvalueloading/load(__isolation_).md>) method to retrieve the property value.

The value is an ISO 639-2/T language code, or `nil` if the track doesn’t specify a language code.

## See Also

### Loading language support

- [extendedLanguageTag](extendedlanguagetag.md) — The language tag of the track.
