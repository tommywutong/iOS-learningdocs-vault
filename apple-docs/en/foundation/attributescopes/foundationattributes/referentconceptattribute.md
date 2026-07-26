---
title: AttributeScopes.FoundationAttributes.ReferentConceptAttribute
framework: Foundation
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/attributescopes/foundationattributes/referentconceptattribute
source_url: 'https://developer.apple.com/documentation/foundation/attributescopes/foundationattributes/referentconceptattribute'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/attributescopes/foundationattributes/referentconceptattribute.json'
content_hash: 'sha256:a79130e3ac78b22b'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [AttributeScopes](../../attributescopes.md) · [FoundationAttributes](../foundationattributes.md)

# AttributeScopes.FoundationAttributes.ReferentConceptAttribute

<sub>Enumeration</sub>

An attribute that specifies a grammatical agreement concept for substituting pronouns in localized text.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@frozen enum ReferentConceptAttribute
```

## Overview

Use the [referentConcept](referentconcept.md) formatting attribute for cases where you need to refer to a person using their preferred pronoun in a string.

For an example of how to use a `referentConcept`, see [TermOfAddress](../../termofaddress.md).

## Relationships

- **Conforms To**: [AttributedStringKey](../../attributedstringkey.md), [BitwiseCopyable](../../../swift/bitwisecopyable.md), [Copyable](../../../swift/copyable.md), [DecodableAttributedStringKey](../../decodableattributedstringkey.md), [EncodableAttributedStringKey](../../encodableattributedstringkey.md), [MarkdownDecodableAttributedStringKey](../../markdowndecodableattributedstringkey.md), [SendableMetatype](../../../swift/sendablemetatype.md)

## See Also

### Using automatic grammar agreement attributes

- [inflect](inflect.md) — A scope for accessing an inflection rule attribute.
- [InflectionRuleAttribute](inflectionruleattribute.md) — A type for using an inflection rule as an attribute.
- [agreementArgument](agreementargument.md) — A scope for accessing an agreement argument attribute.
- [AgreementArgumentAttribute](agreementargumentattribute.md) — An attribute that represents grammatical agreement with an argument in a localized string.
- [agreementConcept](agreementconcept.md) — A scope for accessing an agreement concept attribute.
- [AgreementConceptAttribute](agreementconceptattribute.md) — An attribute that represents grammatical agreement for objects that aren’t part of the inflected text.
- [morphology](morphology.md) — A scope for accessing a morphology attribute.
- [MorphologyAttribute](morphologyattribute.md) — A type for using a morphology as an attribute.
- [referentConcept](referentconcept.md) — A scope for accessing a referent concept attribute.
- [inflectionAlternative](inflectionalternative.md) — A scope for accessing an inflection alternative attribute.
- [InflectionAlternativeAttribute](inflectionalternativeattribute.md) — An attribute that provides an alternative inflection phrase when the system can’t achieve grammatical agreement.
