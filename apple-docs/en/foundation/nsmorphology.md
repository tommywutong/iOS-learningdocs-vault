---
title: NSMorphology
framework: Foundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsmorphology
source_url: 'https://developer.apple.com/documentation/foundation/nsmorphology'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsmorphology.json'
content_hash: 'sha256:b1e2fd3ae4481e2a'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSMorphology

<sub>Class</sub>

A description of the grammatical properties of a string.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
@interface NSMorphology : NSObject
```

## Overview

Use a morphology with an [NSInflectionRule](nsinflectionrule.md) to specify how to interpret a specific word when inflecting an [NSAttributedString](nsattributedstring.md). This affects grammatical agreement with traits like number and gender, as well as declaring the word’s part of speech.

The [NSMorphology](nsmorphology.md) type’s design is language-independent; the concepts it can specify encompass the spectrum of what languages can do. Even for languages that don’t have one or more of those properties benefit the system as hints to make appropriate choices even when an exact inflection isn’t possible. Examples of properties absent from languages include Spanish’s lack of a grammatical gender of neuter, or the nonexistence of a paucal (plural few) pronoun in English.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [NSCopying](nscopying.md), [NSSecureCoding](nssecurecoding.md)

## Topics

### Accessing the User’s Morphology

- [userMorphology](nsmorphology/usermorphology.md) — The addressing preferences of the current user.

### Accessing Grammatical Properties

- [unspecified](nsmorphology/unspecified.md) — A Boolean value that indicates whether this instance specifies no particular grammar.
- [grammaticalGender](nsmorphology/grammaticalgender.md) — The grammatical gender used for inflecting strings with this morphology.
- [NSGrammaticalGender](nsgrammaticalgender.md) — A representation of grammatical gender, used for inflecting strings.
- [number](nsmorphology/number.md) — The grammatical number used for inflecting strings with this morphology.
- [NSGrammaticalNumber](nsgrammaticalnumber.md) — A representation of grammatical number, used for inflecting strings.
- [partOfSpeech](nsmorphology/partofspeech.md) — The grammatical part of speech used for inflecting strings with this morphology.
- [NSGrammaticalPartOfSpeech](nsgrammaticalpartofspeech.md) — A representation of grammatical parts of speech, used for inflecting strings.

### Accessing Per-Language Features

- [setCustomPronoun:forLanguage:error:](nsmorphology/setcustompronoun_forlanguage_error_.md) — Sets a custom pronoun behavior for this morphology to apply to the given language. _(deprecated)_
- [customPronounForLanguage:](nsmorphology/custompronounforlanguage_.md) — Returns any custom pronoun behavior this morphology applies to the given language. _(deprecated)_
- [NSMorphologyCustomPronoun](nsmorphologycustompronoun.md) — A custom pronoun behavior for use in a specific langauge. _(deprecated)_

### Instance Properties

- [definiteness](nsmorphology/definiteness.md)
- [determination](nsmorphology/determination.md)
- [grammaticalCase](nsmorphology/grammaticalcase.md)
- [grammaticalPerson](nsmorphology/grammaticalperson.md)
- [pronounType](nsmorphology/pronountype.md)

## See Also

### Automatic grammar agreement

- [NSInflectionRule](nsinflectionrule.md) — A rule that affects how an attributed string performs automatic grammatical agreement.
- [NSInflectionRuleExplicit](nsinflectionruleexplicit.md) — An inflection rule that uses a morphology instance to determine how to inflect attribued strings.
- [NSTermOfAddress](nstermofaddress.md) — The type for representing grammatical gender in localized text.
- [NSMorphologyPronoun](nsmorphologypronoun.md) — A custom pronoun for referring to a third person.
