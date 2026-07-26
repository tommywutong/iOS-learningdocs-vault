---
title: NSMorphologyPronoun
framework: Foundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsmorphologypronoun
source_url: 'https://developer.apple.com/documentation/foundation/nsmorphologypronoun'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsmorphologypronoun.json'
content_hash: 'sha256:1ea6cae5b327e45a'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSMorphologyPronoun

<sub>Class</sub>

A custom pronoun for referring to a third person.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
@interface NSMorphologyPronoun : NSObject
```

## Overview

Create instances of [NSMorphologyPronoun](nsmorphologypronoun.md) when you need to define custom pronouns for a localized term of address.

For examples of how to create custom pronouns, see [TermOfAddress](termofaddress.md).

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [NSCopying](nscopying.md), [NSSecureCoding](nssecurecoding.md)

## Topics

### Using pronouns

- [pronoun](nsmorphologypronoun/pronoun.md)
- [morphology](nsmorphologypronoun/morphology.md)
- [dependentMorphology](nsmorphologypronoun/dependentmorphology.md)

### Instance Methods

- [initWithPronoun:morphology:dependentMorphology:](nsmorphologypronoun/initwithpronoun_morphology_dependentmorphology_.md)

## See Also

### Automatic grammar agreement

- [NSInflectionRule](nsinflectionrule.md) — A rule that affects how an attributed string performs automatic grammatical agreement.
- [NSInflectionRuleExplicit](nsinflectionruleexplicit.md) — An inflection rule that uses a morphology instance to determine how to inflect attribued strings.
- [NSMorphology](nsmorphology.md) — A description of the grammatical properties of a string.
- [NSTermOfAddress](nstermofaddress.md) — The type for representing grammatical gender in localized text.
