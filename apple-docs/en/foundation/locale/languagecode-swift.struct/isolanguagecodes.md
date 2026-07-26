---
title: isoLanguageCodes
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/locale/languagecode-swift.struct/isolanguagecodes
source_url: 'https://developer.apple.com/documentation/foundation/locale/languagecode-swift.struct/isolanguagecodes'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/locale/languagecode-swift.struct/isolanguagecodes.json'
content_hash: 'sha256:0506cedd3975a548'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [Locale](../../locale.md) · [LanguageCode](../languagecode-swift.struct.md)

# isoLanguageCodes

<sub>Type Property</sub>

Returns an array of ISO-defined language codes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var isoLanguageCodes: [Locale.LanguageCode] { get }
```

## Discussion

The returned array contains two-letter codes defined by ISO 639, as well as three-letter codes without a two-letter equivalent.
