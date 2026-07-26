---
title: TermOfAddress
framework: Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/termofaddress
source_url: 'https://developer.apple.com/documentation/foundation/termofaddress'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/termofaddress.json'
content_hash: 'sha256:e731f127422a1b81'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# TermOfAddress

<sub>Structure</sub>

The type for representing grammatical gender in localized text.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct TermOfAddress
```

## Overview

Many languages rely on gender for their grammar. Without knowing the subject’s gender or pronoun preferences, some localized strings may have grammatical errors, resulting in a poor user experience.

`TermOfAddress` is a type that enables the system to make pronoun substitutions in localized text based on gender. You don’t create instances of this type directly. Instead, use the predefined types to specify the gender to use when referring to people in translated text. Or define your own pronoun terms for a specific language when the predefined types are insufficient.

> [!note] Note
> Not all terms of address exist in all languages.

For example, to substitute the masculine pronoun _He_, for the neutral pronoun _They_, do the following:

```swift
// Define the resource you want to apply grammatical agreement to.
let resource = LocalizedStringResource("^[They](referentConcept: 1) liked your post.")

// Set the inflection concept to use a term of address.
var options = AttributedString.LocalizationOptions()
options.concepts = [.termsOfAddress([.masculine])]

// Make a new string imposing grammatical agreement on the resource from the term of address.
let result = AttributedString(localized: resource, options: options)
// result == "He liked your post."
```

If the [masculine](termofaddress/masculine.md), [feminine](termofaddress/feminine.md), and [neutral](termofaddress/neutral.md) terms of address are insufficient, create your own term of address specifying the pronouns and language.

```swift
// Define the various morphologies.
var nominativeMorphology = Morphology()
var accusativeMorphology = Morphology()
var genitiveMorphology = Morphology()
var genetiveIndependent = Morphology()
var reflexive = Morphology()

nominativeMorphology.grammaticalCase = .nominative
accusativeMorphology.grammaticalCase = .accusative
genitiveMorphology.grammaticalCase = .genitive
genitiveMorphology.determination = .dependent
genetiveIndependent.grammaticalCase = .genitive
genetiveIndependent.determination = .independent
reflexive.pronounType = .reflexive

// Define the pronouns.
let xey  = Morphology.Pronoun(pronoun:"xey", morphology: nominativeMorphology)
let xem  = Morphology.Pronoun(pronoun:"xem", morphology: accusativeMorphology)
let xeir = Morphology.Pronoun(pronoun:"xeir", morphology: genitiveMorphology)
let xeirs = Morphology.Pronoun(pronoun: "xeirs", morphology: genetiveIndependent)
let xemself = Morphology.Pronoun(pronoun: "xemself", morphology: reflexive)
        
// Create the localized term of address.
let xemTermOfAddress = TermOfAddress.localized(language: .init(identifier: "en"), pronouns: [xey, xem, xeir, xeirs, xemself])

// Define the resources you want to apply gender agreement to.
let resources = [
    LocalizedStringResource("^[They](referentConcept: 1) liked your post."),
    LocalizedStringResource("Anne read the post to ^[them](referentConcept: 1)."),
    LocalizedStringResource("You liked ^[their](referentConcept: 1) post."),
    LocalizedStringResource("The post was ^[theirs](referentConcept: 1)."),
    LocalizedStringResource("^[They](referentConcept: 1) posted it ^[themselves](referentConcept: 1)."),
]
var options = AttributedString.LocalizationOptions()

// Set the inflection concept to use the new term of address.
options.concepts = [.termsOfAddress([xemTermOfAddress])]

let results = [
    AttributedString(localized: resources[0], options: options), // "Xey liked your post."
    AttributedString(localized: resources[1], options: options), // "Anne read the post to xem."
    AttributedString(localized: resources[2], options: options), // "You liked xeir post."
    AttributedString(localized: resources[3], options: options), // "The post was xeirs."
    AttributedString(localized: resources[4], options: options), // "Xey posted it xemself."
]
```

For examples of how to use terms of address, see:

- [ReferentConceptAttribute](attributescopes/foundationattributes/referentconceptattribute.md)
- [AgreementConceptAttribute](attributescopes/foundationattributes/agreementconceptattribute.md)

## Relationships

- **Conforms To**: [Copyable](../swift/copyable.md), [Decodable](../swift/decodable.md), [Encodable](../swift/encodable.md), [Equatable](../swift/equatable.md), [Escapable](../swift/escapable.md), [Hashable](../swift/hashable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Using predefined terms of address

- [feminine](termofaddress/feminine.md) — The term of address for representing feminine pronouns and grammatical gender.
- [masculine](termofaddress/masculine.md) — The term of address for representing masculine pronouns and grammatical gender.
- [neutral](termofaddress/neutral.md) — The term of address for representing gender-neutral pronouns and grammatical gender.

### Defining your own terms of address

- [localized(language:pronouns:)](<termofaddress/localized(language_pronouns_).md>) — Returns a term of address restricted to a specific language for a group of pronouns.
- [language](termofaddress/language.md) — The specific language associated with a term of address.
- [pronouns](termofaddress/pronouns.md) — The pronouns associated with a term of address.

### Type Properties

- [currentUser](termofaddress/currentuser.md) — The term of address that should be used for addressing the user

## See Also

### Automatic grammar agreement

- [InflectionRule](inflectionrule.md) — A rule that affects how an attributed string performs automatic grammatical agreement.
- [Morphology](morphology.md) — A description of the grammatical properties of a string.
- [InflectionConcept](inflectionconcept.md) — An inflection method to use when localizing text.
- [Pronoun](morphology/pronoun.md) — A custom pronoun for referring to a third person.
