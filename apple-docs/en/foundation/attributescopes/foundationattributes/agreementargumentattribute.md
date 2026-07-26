---
title: AttributeScopes.FoundationAttributes.AgreementArgumentAttribute
framework: Foundation
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/attributescopes/foundationattributes/agreementargumentattribute
source_url: 'https://developer.apple.com/documentation/foundation/attributescopes/foundationattributes/agreementargumentattribute'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/attributescopes/foundationattributes/agreementargumentattribute.json'
content_hash: 'sha256:65b1d7aa26cf24c1'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [AttributeScopes](../../attributescopes.md) · [FoundationAttributes](../foundationattributes.md)

# AttributeScopes.FoundationAttributes.AgreementArgumentAttribute

<sub>Enumeration</sub>

An attribute that represents grammatical agreement with an argument in a localized string.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@frozen enum AgreementArgumentAttribute
```

## Overview

Many languages require grammatical agreement in their sentences. In Spanish, for example, the adjectives and verbs need to agree with the gender of the subject they refer to in the sentence. For example, suppose you need to translate the following sentence into Spanish: _Your small salad is ready._ The correct translation is: _Tu ensalada pequeña está lista._

The challenge is that, most often, the localization file only contains masculine forms of translated words. So, in this sentence, the masculine words for _small_ and _ready_, _pequeño_ and _listo_, need to inflect and become _pequeña_ and _lista_ to agree with the feminine subject of the sentence (_ensalada_).

You can make the first part of the sentence grammatically agree by inflecting the words _ensalada_ and _pequeño_ together using the `inflect` attribute. Because _ensalada_ is the feminine subject of the sentence, masculine _pequeño_ inflects to feminine _pequeña_.

The second part of the sentence, however, requires the `agreeWithArgument` attribute. Although _listo_ is at the end of the sentence, it needs to inflect on the subject, _ensalada_, which is at the beginning. By wrapping _listo_ in an `agreeWithArgument` attribute and pointing it to the feminine word _ensalada_, masculine _listo_ inflects to feminine _lista_, making the entire sentence agree.

Using `agreeWithArgument` this way eliminates the need for the localization file to include both the masculine and the feminine forms of each word. By wrapping the words needing inflection, and then pointing them to the words they need to agree with, the system achieves agreement in the localized text for you.

The following steps ensure proper gender agreement in the translation:

1. Create a type containing all the words you need for translation. For example, create an `Order` structure containing two localizable string properties for `item` and `size`.
2. Add the necessary translations for the food items and the sizes into the Spanish localization file.
3. Create a [LocalizedStringResource](../../localizedstringresource.md) containing the English key phrase from the Spanish localization file to translate, along with placeholder variables representing the words to inflect (_size_ and _item_).
4. In the Spanish localization file, add `%@` placeholders for the words you want to substitute as part of the translation. Make the Spanish words for the size and the item grammatically agree using the `inflect` attribute with a value of [true](../../../swift/true.md). Then make the masculine Spanish word for _ready_ (_listo_) agree with the feminine word for _salad_ (_ensalada_) by wrapping _listo_ in an `agreeWithArgument` attribute, pointing to the second replacement in the sentence (_ensalada_). Note how the placeholder attributes for _small salad_, `%1@` and `%2@`, reverse order in the code example below when translating from English to Spanish.
5. Inflect the entire sentence by passing the [LocalizedStringResource](../../localizedstringresource.md) instance into a new instance of [AttributedString](../../attributedstring.md).

```swift
struct Order {
    let item: String
    let size: String
}

let order = Order(item: String(localized: "salad"), size: String(localized: "small"))

// ____________
// In the Spanish localization file:
// "salad" = "ensalada"
// "small" = "pequeño"
// ____________

// Define the resource you want to apply grammatical agreement to.
let resource = LocalizedStringResource("Your \(order.size) \(order.item) is ready.")

// ____________
// In the Spanish localization file:
// "Your %1@ %2@ is ready." = "Tu ^[%2$@ %1$@](inflect: true) está ^[listo](agreeWithArgument: 2)."
// ____________

// Make a new string imposing grammatical agreement on the resource from the localized phrase.
let result = AttributedString(localized: resource)
// result == "Tu ensalada pequeña está lista."

```

## Relationships

- **Conforms To**: [AttributedStringKey](../../attributedstringkey.md), [BitwiseCopyable](../../../swift/bitwisecopyable.md), [Copyable](../../../swift/copyable.md), [DecodableAttributedStringKey](../../decodableattributedstringkey.md), [EncodableAttributedStringKey](../../encodableattributedstringkey.md), [MarkdownDecodableAttributedStringKey](../../markdowndecodableattributedstringkey.md), [SendableMetatype](../../../swift/sendablemetatype.md)

## See Also

### Using automatic grammar agreement attributes

- [inflect](inflect.md) — A scope for accessing an inflection rule attribute.
- [InflectionRuleAttribute](inflectionruleattribute.md) — A type for using an inflection rule as an attribute.
- [agreementArgument](agreementargument.md) — A scope for accessing an agreement argument attribute.
- [agreementConcept](agreementconcept.md) — A scope for accessing an agreement concept attribute.
- [AgreementConceptAttribute](agreementconceptattribute.md) — An attribute that represents grammatical agreement for objects that aren’t part of the inflected text.
- [morphology](morphology.md) — A scope for accessing a morphology attribute.
- [MorphologyAttribute](morphologyattribute.md) — A type for using a morphology as an attribute.
- [referentConcept](referentconcept.md) — A scope for accessing a referent concept attribute.
- [ReferentConceptAttribute](referentconceptattribute.md) — An attribute that specifies a grammatical agreement concept for substituting pronouns in localized text.
- [inflectionAlternative](inflectionalternative.md) — A scope for accessing an inflection alternative attribute.
- [InflectionAlternativeAttribute](inflectionalternativeattribute.md) — An attribute that provides an alternative inflection phrase when the system can’t achieve grammatical agreement.
