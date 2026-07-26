---
title: Morphology.Pronoun
framework: Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift, swift, swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/morphology/pronoun
source_url: 'https://developer.apple.com/documentation/foundation/morphology/pronoun'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/morphology/pronoun.json'
content_hash: 'sha256:14fb155fc5eddf49'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Morphology](../morphology.md)

# Morphology.Pronoun

<sub>Structure</sub>

A custom pronoun for referring to a third person.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct Pronoun
```

## Overview

Create instances of [Pronoun](pronoun.md) when you need to define custom pronouns for a localized term of address.

For examples of how to create custom pronouns, see [TermOfAddress](../termofaddress.md).

## Relationships

- **Conforms To**: [Copyable](../../swift/copyable.md), [Decodable](../../swift/decodable.md), [Encodable](../../swift/encodable.md), [Equatable](../../swift/equatable.md), [Escapable](../../swift/escapable.md), [Hashable](../../swift/hashable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Creating pronouns

- [init(pronoun:morphology:dependentMorphology:)](<pronoun/init(pronoun_morphology_dependentmorphology_).md>) — Creates a pronoun with the specified name, morphology, and dependent morphology.

### Using pronouns

- [pronoun](pronoun/pronoun.md) — The string representation of the pronoun.
- [morphology](pronoun/morphology.md) — The morphology of the pronoun form.
- [dependentMorphology](pronoun/dependentmorphology.md) — The dependent morphology of the pronoun form.

## See Also

### Automatic grammar agreement

- [InflectionRule](../inflectionrule.md) — A rule that affects how an attributed string performs automatic grammatical agreement.
- [Morphology](../morphology.md) — A description of the grammatical properties of a string.
- [TermOfAddress](../termofaddress.md) — The type for representing grammatical gender in localized text.
- [InflectionConcept](../inflectionconcept.md) — An inflection method to use when localizing text.
