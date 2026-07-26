---
title: inflectionRule
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsattributedstring/key/inflectionrule
source_url: 'https://developer.apple.com/documentation/foundation/nsattributedstring/key/inflectionrule'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsattributedstring/key/inflectionrule.json'
content_hash: 'sha256:3b40c714abd3fc8b'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [NSAttributedString](../../nsattributedstring.md) · [Key](../key.md)

# inflectionRule

<sub>Type Property</sub>

An attribute that tells the system how to apply grammar rules and other modifiers to the range of text.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static let inflectionRule: NSAttributedString.Key
```

## Discussion

The value of this key is an [NSInflectionRule](../../nsinflectionrule.md) object.

## See Also

### Getting translation-related attribute keys

- [NSLanguageIdentifierAttributeName](languageidentifier.md) — The language identifier associated with the range of text.
- [NSMorphologyAttributeName](morphology.md) — An attribute that contains grammatical properties to apply to the text.
- [NSInflectionAlternativeAttributeName](inflectionalternative.md) — The alternative translation for a string when no suitable inflection exists.
- [NSInflectionAgreementArgumentAttributeName](agreewithargument.md) — An attribute key whose value indicates inflection agreement with a specific argument.
- [NSInflectionAgreementConceptAttributeName](agreewithconcept.md) — An attribute key whose value indicates inflection agreement with a specific concept.
- [NSInflectionReferentConceptAttributeName](referentconcept.md) — An attribute key whose value indicates the referent concept for inflection.
- [NSLocalizedNumberFormatAttributeName](localizednumberformat.md) — An attribute key whose value specifies a localized number format.
