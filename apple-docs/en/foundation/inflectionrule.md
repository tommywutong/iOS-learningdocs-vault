---
title: InflectionRule
framework: Foundation
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/inflectionrule
source_url: 'https://developer.apple.com/documentation/foundation/inflectionrule'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/inflectionrule.json'
content_hash: 'sha256:baab26416159cad6'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# InflectionRule

<sub>Enumeration</sub>

A rule that affects how an attributed string performs automatic grammatical agreement.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
enum InflectionRule
```

## Overview

Most apps can rely on loading localized strings to perform automatic grammar agreement. Typically, strings in your app’s strings files use the Markdown extension syntax to indicate portions of the string that may require inflection to agree grammatically. This transformation occurs when you load the attributed string with methods like `init(localized:options:table:bundle:locale:comment:)`.

However, if the system lacks information about the words in the string, you may need to apply an inflection rule programmatically. For example, a social networking app may have gender information about other users that you want to apply at runtime. When performing manual inflection at runtime, you use an inflection rule to indicate to the system what portions of a string should be automatically edited, and what to match. Apply the [inflect](attributescopes/foundationattributes/inflect.md) attribute to set an [InflectionRule](inflectionrule.md) on an [AttributedString](attributedstring.md), then call [inflected()](<attributedstring/inflected().md>) to perform the grammar agreement and produce an edited string.

```swift
var string = AttributedString(localized: "They liked your post.")
// The user who liked the post uses feminine pronouns.
var morphology = Morphology()
morphology.grammaticalGender = .feminine
string.inflect = InflectionRule(morphology: morphology)
let result = string.inflected()
// result == "She liked your post."
```

## Relationships

- **Conforms To**: [Copyable](../swift/copyable.md), [Decodable](../swift/decodable.md), [Encodable](../swift/encodable.md), [Equatable](../swift/equatable.md), [Escapable](../swift/escapable.md), [Hashable](../swift/hashable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Creating an Inflection Rule from a Morphology

- [init(morphology:)](<inflectionrule/init(morphology_).md>) — Creates an inflection rule with the given morphology.
- [Morphology](morphology.md) — A description of the grammatical properties of a string.

### Inflection Rule Behaviors

- [InflectionRule.automatic](inflectionrule/automatic.md) — An inflection rule that performs automatic grammar agreement with default transformations.
- [InflectionRule.explicit(_:)](<inflectionrule/explicit(__).md>) — An inflection rule that uses a morphology instance to determine how to inflect attribued strings.

### Determining Availability

- [canInflect(language:)](<inflectionrule/caninflect(language_).md>) — Returns a Boolean value that indicates whether the rule can inflect a given language.
- [canInflectPreferredLocalization](inflectionrule/caninflectpreferredlocalization.md) — A Boolean value that indicates whether the rule can inflect the user’s current preferred localization.

## See Also

### Automatic grammar agreement

- [Morphology](morphology.md) — A description of the grammatical properties of a string.
- [TermOfAddress](termofaddress.md) — The type for representing grammatical gender in localized text.
- [InflectionConcept](inflectionconcept.md) — An inflection method to use when localizing text.
- [Pronoun](morphology/pronoun.md) — A custom pronoun for referring to a third person.
