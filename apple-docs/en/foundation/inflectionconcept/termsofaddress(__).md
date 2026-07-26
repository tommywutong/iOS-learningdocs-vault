---
title: 'InflectionConcept.termsOfAddress(_:)'
framework: Foundation
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/inflectionconcept/termsofaddress(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/inflectionconcept/termsofaddress(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/inflectionconcept/termsofaddress%28_%3A%29.json'
content_hash: 'sha256:3a7edaba31f6451d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [InflectionConcept](../inflectionconcept.md)

# InflectionConcept.termsOfAddress(_:)

<sub>Case</sub>

Indicates that the system uses the associated terms of address for grammatical agreement when localizing text.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case termsOfAddress([TermOfAddress])
```

## Parameters

- `[TermOfAddress]` — A list of preferred terms of address for localizing text.

## Discussion

When inflecting text the first term of address which can be used in the target language is the one used for pronoun substitution and grammar agreement.

## See Also

### Using inflection concepts

- [InflectionConcept.localizedPhrase(_:)](<localizedphrase(__).md>) — Indicates that the system uses the associated string for grammatical agreement when localizing text.
