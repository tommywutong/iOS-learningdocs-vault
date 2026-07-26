---
title: AttributeScopes.FoundationAttributes.InflectionAlternativeAttribute
framework: Foundation
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/attributescopes/foundationattributes/inflectionalternativeattribute
source_url: 'https://developer.apple.com/documentation/foundation/attributescopes/foundationattributes/inflectionalternativeattribute'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/attributescopes/foundationattributes/inflectionalternativeattribute.json'
content_hash: 'sha256:9ec4ad2034ca65da'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [AttributeScopes](../../attributescopes.md) · [FoundationAttributes](../foundationattributes.md)

# AttributeScopes.FoundationAttributes.InflectionAlternativeAttribute

<sub>Enumeration</sub>

An attribute that provides an alternative inflection phrase when the system can’t achieve grammatical agreement.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@frozen enum InflectionAlternativeAttribute
```

## Overview

Use the `inflectionAlternativeAttribute` to provide an alternative phrase for cases where the system can’t achieve unambiguous grammatical agreement.

For example, suppose you want to inflect the masculine form for _welcome_ in Spanish, _bienvenido_, but the system doesn’t know the person’s preferred terms of address. Add an `inflectionAlternative` to your [LocalizedStringResource](../../localizedstringresource.md), setting the alternative word or phrase in single quotation marks. The system uses the alternative when it can’t determine proper grammatical agreement.

```swift
// Define the resource with an inflection alternative.
let resource = LocalizedStringResource("^[Bienvenido](inflect: true, inflectionAlternative: 'Te damos la bienvenida').")

// Use the inflection alternative when the system can't determine agreement.
let result = AttributedString(localized: resource)
// result == "Te damos la bienvenida."
```

## Relationships

- **Conforms To**: [AttributedStringKey](../../attributedstringkey.md), [BitwiseCopyable](../../../swift/bitwisecopyable.md), [Copyable](../../../swift/copyable.md), [DecodableAttributedStringKey](../../decodableattributedstringkey.md), [EncodableAttributedStringKey](../../encodableattributedstringkey.md), [MarkdownDecodableAttributedStringKey](../../markdowndecodableattributedstringkey.md), [ObjectiveCConvertibleAttributedStringKey](../../objectivecconvertibleattributedstringkey.md), [SendableMetatype](../../../swift/sendablemetatype.md)

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
- [ReferentConceptAttribute](referentconceptattribute.md) — An attribute that specifies a grammatical agreement concept for substituting pronouns in localized text.
- [inflectionAlternative](inflectionalternative.md) — A scope for accessing an inflection alternative attribute.
