---
title: Morphology
framework: Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/morphology
source_url: 'https://developer.apple.com/documentation/foundation/morphology'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/morphology.json'
content_hash: 'sha256:fa98808d08644381'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# Morphology

<sub>Structure</sub>

A description of the grammatical properties of a string.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct Morphology
```

## Overview

Use a morphology with an [InflectionRule](inflectionrule.md) to specify how to interpret a specific word when inflecting an [AttributedString](attributedstring.md). This affects grammatical agreement with traits like number and gender, as well as declaring the word’s part of speech.

The [Morphology](morphology.md) type’s design is language-independent; the concepts it can specify encompass the spectrum of what languages can do. Even for languages that don’t have one or more of those properties benefit the system as hints to make appropriate choices even when an exact inflection isn’t possible. Examples of properties absent from languages include Spanish’s lack of a grammatical gender of neuter, or the nonexistence of a paucal (plural few) pronoun in English.

## Relationships

- **Conforms To**: [Copyable](../swift/copyable.md), [Decodable](../swift/decodable.md), [Encodable](../swift/encodable.md), [Equatable](../swift/equatable.md), [Escapable](../swift/escapable.md), [Hashable](../swift/hashable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Creating a Morphology Instance

- [init()](<morphology/init().md>) — Creates an empty morphology instance.

### Accessing the User’s Morphology

- [user](morphology/user.md) — The addressing preferences of the current user.

### Accessing Grammatical Properties

- [isUnspecified](morphology/isunspecified.md) — A Boolean value that indicates whether this instance specifies no particular grammar.
- [grammaticalGender](morphology/grammaticalgender-swift.property.md) — The grammatical gender used for inflecting strings with this morphology.
- [GrammaticalGender](morphology/grammaticalgender-swift.enum.md) — A representation of grammatical gender, used for inflecting strings.
- [number](morphology/number.md) — The grammatical number used for inflecting strings with this morphology.
- [GrammaticalNumber](morphology/grammaticalnumber.md) — A representation of grammatical number, used for inflecting strings.
- [partOfSpeech](morphology/partofspeech-swift.property.md) — The grammatical part of speech used for inflecting strings with this morphology.
- [PartOfSpeech](morphology/partofspeech-swift.enum.md) — A representation of grammatical parts of speech, used for inflecting strings.

### Accessing Per-Language Features

- [setCustomPronoun(_:forLanguage:)](<morphology/setcustompronoun(__forlanguage_).md>) — Sets a custom pronoun behavior for this morphology to apply to the given language. _(deprecated)_
- [customPronoun(forLanguage:)](<morphology/custompronoun(forlanguage_).md>) — Returns any custom pronoun behavior this morphology applies to the given language. _(deprecated)_
- [CustomPronoun](morphology/custompronoun.md) — A custom pronoun behavior for use in a specific langauge. _(deprecated)_

### Structures

- [Pronoun](morphology/pronoun.md) — A custom pronoun for referring to a third person.

### Instance Properties

- [definiteness](morphology/definiteness-swift.property.md)
- [determination](morphology/determination-swift.property.md)
- [grammaticalCase](morphology/grammaticalcase-swift.property.md)
- [grammaticalPerson](morphology/grammaticalperson-swift.property.md)
- [pronounType](morphology/pronountype-swift.property.md)

### Enumerations

- [Definiteness](morphology/definiteness-swift.enum.md)
- [Determination](morphology/determination-swift.enum.md)
- [GrammaticalCase](morphology/grammaticalcase-swift.enum.md)
- [GrammaticalPerson](morphology/grammaticalperson-swift.enum.md)
- [PronounType](morphology/pronountype-swift.enum.md)

## See Also

### Automatic grammar agreement

- [InflectionRule](inflectionrule.md) — A rule that affects how an attributed string performs automatic grammatical agreement.
- [TermOfAddress](termofaddress.md) — The type for representing grammatical gender in localized text.
- [InflectionConcept](inflectionconcept.md) — An inflection method to use when localizing text.
- [Pronoun](morphology/pronoun.md) — A custom pronoun for referring to a third person.
