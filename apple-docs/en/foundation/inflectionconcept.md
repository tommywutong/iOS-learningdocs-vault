---
title: InflectionConcept
framework: Foundation
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/inflectionconcept
source_url: 'https://developer.apple.com/documentation/foundation/inflectionconcept'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/inflectionconcept.json'
content_hash: 'sha256:41e3c68012437ff7'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# InflectionConcept

<sub>Enumeration</sub>

An inflection method to use when localizing text.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
enum InflectionConcept
```

## Overview

Use `InflectionConcept` when you want to make a localizable string grammatically agree with a phrase or term of address that isn’t part of the text you’re localizing. Set [InflectionConcept](inflectionconcept.md) on the [concepts](attributedstring/localizationoptions/concepts.md) property of [LocalizationOptions](attributedstring/localizationoptions.md) to specify the inflection concepts to use while inflecting text.

For examples of how to use inflection concepts, see:

- [ReferentConceptAttribute](attributescopes/foundationattributes/referentconceptattribute.md)
- [AgreementConceptAttribute](attributescopes/foundationattributes/agreementconceptattribute.md)

## Relationships

- **Conforms To**: [Decodable](../swift/decodable.md), [Encodable](../swift/encodable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Using inflection concepts

- [InflectionConcept.termsOfAddress(_:)](<inflectionconcept/termsofaddress(__).md>) — Indicates that the system uses the associated terms of address for grammatical agreement when localizing text.
- [InflectionConcept.localizedPhrase(_:)](<inflectionconcept/localizedphrase(__).md>) — Indicates that the system uses the associated string for grammatical agreement when localizing text.

## See Also

### Automatic grammar agreement

- [InflectionRule](inflectionrule.md) — A rule that affects how an attributed string performs automatic grammatical agreement.
- [Morphology](morphology.md) — A description of the grammatical properties of a string.
- [TermOfAddress](termofaddress.md) — The type for representing grammatical gender in localized text.
- [Pronoun](morphology/pronoun.md) — A custom pronoun for referring to a third person.
