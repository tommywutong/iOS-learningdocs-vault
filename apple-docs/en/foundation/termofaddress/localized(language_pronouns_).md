---
title: 'localized(language:pronouns:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/termofaddress/localized(language:pronouns:)'
source_url: 'https://developer.apple.com/documentation/foundation/termofaddress/localized(language:pronouns:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/termofaddress/localized%28language%3Apronouns%3A%29.json'
content_hash: 'sha256:017ba124567ad193'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [TermOfAddress](../termofaddress.md)

# localized(language:pronouns:)

<sub>Type Method</sub>

Returns a term of address restricted to a specific language for a group of pronouns.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func localized(language: Locale.Language, pronouns: [Morphology.Pronoun]) -> TermOfAddress
```

## Parameters

- `language` — The language locale to use for the term of address.

- `pronouns` — The pronouns for representing the terms of address.

## Return Value

A term of address associating a group of pronouns  to a specific language.

## See Also

### Defining your own terms of address

- [language](language.md) — The specific language associated with a term of address.
- [pronouns](pronouns.md) — The pronouns associated with a term of address.
