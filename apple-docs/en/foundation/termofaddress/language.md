---
title: language
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/termofaddress/language
source_url: 'https://developer.apple.com/documentation/foundation/termofaddress/language'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/termofaddress/language.json'
content_hash: 'sha256:c2395fe05da40fd0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [TermOfAddress](../termofaddress.md)

# language

<sub>Instance Property</sub>

The specific language associated with a term of address.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var language: Locale.Language? { get }
```

## Discussion

This property is only set for terms of address created through the [localized(language:pronouns:)](<localized(language_pronouns_).md>) function. This property is `nil` otherwise.

## See Also

### Defining your own terms of address

- [localized(language:pronouns:)](<localized(language_pronouns_).md>) — Returns a term of address restricted to a specific language for a group of pronouns.
- [pronouns](pronouns.md) — The pronouns associated with a term of address.
