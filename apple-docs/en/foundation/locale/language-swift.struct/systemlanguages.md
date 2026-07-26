---
title: systemLanguages
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift, swift, swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/locale/language-swift.struct/systemlanguages
source_url: 'https://developer.apple.com/documentation/foundation/locale/language-swift.struct/systemlanguages'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/locale/language-swift.struct/systemlanguages.json'
content_hash: 'sha256:7cc63ff5f43d80fa'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [Locale](../../locale.md) · [Language](../language-swift.struct.md)

# systemLanguages

<sub>Type Property</sub>

An array of the system’s supported languages.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var systemLanguages: [Locale.Language] { get }
```

## Discussion

The returned array includes the languages of all product localizations for the current platform.
