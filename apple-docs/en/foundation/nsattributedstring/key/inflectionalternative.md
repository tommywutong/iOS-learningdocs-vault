---
title: inflectionAlternative
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsattributedstring/key/inflectionalternative
source_url: 'https://developer.apple.com/documentation/foundation/nsattributedstring/key/inflectionalternative'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsattributedstring/key/inflectionalternative.json'
content_hash: 'sha256:b816e58d79a80267'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [NSAttributedString](../../nsattributedstring.md) · [Key](../key.md)

# inflectionAlternative

<sub>Type Property</sub>

The alternative translation for a string when no suitable inflection exists.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static let inflectionAlternative: NSAttributedString.Key
```

## Discussion

In languages that change the form of words to match someone’s gender, the system can automatically change (or inflect) the gender to match someone’s personal preferences. If a suitable inflection doesn’t exist, the system uses the value of this attribute instead. Add this attribute to specify a suitable translation that applies to anyone. For example, if a language has only masculine and feminine genders, specify an appropriately neutral translation of the text.

The value of this key is an [NSString](../../nsstring.md) with the replacement phrase to use.

## See Also

### Getting translation-related attribute keys

- [NSLanguageIdentifierAttributeName](languageidentifier.md) — The language identifier associated with the range of text.
- [NSMorphologyAttributeName](morphology.md) — An attribute that contains grammatical properties to apply to the text.
- [NSInflectionRuleAttributeName](inflectionrule.md) — An attribute that tells the system how to apply grammar rules and other modifiers to the range of text.
- [NSInflectionAgreementArgumentAttributeName](agreewithargument.md) — An attribute key whose value indicates inflection agreement with a specific argument.
- [NSInflectionAgreementConceptAttributeName](agreewithconcept.md) — An attribute key whose value indicates inflection agreement with a specific concept.
- [NSInflectionReferentConceptAttributeName](referentconcept.md) — An attribute key whose value indicates the referent concept for inflection.
- [NSLocalizedNumberFormatAttributeName](localizednumberformat.md) — An attribute key whose value specifies a localized number format.
