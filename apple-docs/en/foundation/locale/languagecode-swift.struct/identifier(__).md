---
title: 'identifier(_:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/locale/languagecode-swift.struct/identifier(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/locale/languagecode-swift.struct/identifier(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/locale/languagecode-swift.struct/identifier%28_%3A%29.json'
content_hash: 'sha256:81dc8c5338b2fd56'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [Locale](../../locale.md) · [LanguageCode](../languagecode-swift.struct.md)

# identifier(_:)

<sub>Instance Method</sub>

Returns the ISO code of the given identifier type. Returns nil if the language isn’t a valid ISO language, or if the specified identifier type isn’t available to the language.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func identifier(_ type: Locale.LanguageCode.IdentifierType) -> String?
```
