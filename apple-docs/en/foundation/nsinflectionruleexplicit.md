---
title: NSInflectionRuleExplicit
framework: Foundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsinflectionruleexplicit
source_url: 'https://developer.apple.com/documentation/foundation/nsinflectionruleexplicit'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsinflectionruleexplicit.json'
content_hash: 'sha256:ea710e067d787b74'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSInflectionRuleExplicit

<sub>Class</sub>

An inflection rule that uses a morphology instance to determine how to inflect attribued strings.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
@interface NSInflectionRuleExplicit : NSInflectionRule
```

## Relationships

- **Inherits From**: [NSInflectionRule](nsinflectionrule.md)

## Topics

### Creating an Explicit Inflection Rule

- [initWithMorphology:](nsinflectionruleexplicit/initwithmorphology_.md) — Creates an inflection rule with the given morphology.
- [NSMorphology](nsmorphology.md) — A description of the grammatical properties of a string.

### Accessing Rule Properties

- [morphology](nsinflectionruleexplicit/morphology.md) — The morphology used by this inflection rule.

## See Also

### Automatic grammar agreement

- [NSInflectionRule](nsinflectionrule.md) — A rule that affects how an attributed string performs automatic grammatical agreement.
- [NSMorphology](nsmorphology.md) — A description of the grammatical properties of a string.
- [NSTermOfAddress](nstermofaddress.md) — The type for representing grammatical gender in localized text.
- [NSMorphologyPronoun](nsmorphologypronoun.md) — A custom pronoun for referring to a third person.
