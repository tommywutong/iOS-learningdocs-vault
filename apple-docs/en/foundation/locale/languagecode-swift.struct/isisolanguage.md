---
title: isISOLanguage
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/locale/languagecode-swift.struct/isisolanguage
source_url: 'https://developer.apple.com/documentation/foundation/locale/languagecode-swift.struct/isisolanguage'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/locale/languagecode-swift.struct/isisolanguage.json'
content_hash: 'sha256:ec966022cbed5126'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [Locale](../../locale.md) · [LanguageCode](../languagecode-swift.struct.md)

# isISOLanguage

<sub>Instance Property</sub>

A Boolean value that indicates whether this language code is in the list of ISO-defined languages.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var isISOLanguage: Bool { get }
```

## Discussion

The following code snippet illustrates use of the [isISOLanguage](isisolanguage.md) value.

```swift
let enIsISO = Locale.LanguageCode("en").isISOLanguage // true
let gibberishIsISO = Locale.LanguageCode("gibberish").isISOLanguage // false
```

## See Also

### Examining language code properties

- [identifier](identifier.md) — The identifier used to create the language code.
