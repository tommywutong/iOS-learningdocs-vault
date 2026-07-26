---
title: pronouns
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/termofaddress/pronouns
source_url: 'https://developer.apple.com/documentation/foundation/termofaddress/pronouns'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/termofaddress/pronouns.json'
content_hash: 'sha256:5e03a4d9cc827045'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [TermOfAddress](../termofaddress.md)

# pronouns

<sub>Instance Property</sub>

The pronouns associated with a term of address.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var pronouns: [Morphology.Pronoun] { get }
```

## Discussion

This property is only set for terms of address created through the [localized(language:pronouns:)](<localized(language_pronouns_).md>) function. Calling this property returns an empty array otherwise.

## See Also

### Defining your own terms of address

- [localized(language:pronouns:)](<localized(language_pronouns_).md>) — Returns a term of address restricted to a specific language for a group of pronouns.
- [language](language.md) — The specific language associated with a term of address.
