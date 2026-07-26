---
title: AttributeScopes.FoundationAttributes.AgreementConceptAttribute
framework: Foundation
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/attributescopes/foundationattributes/agreementconceptattribute
source_url: 'https://developer.apple.com/documentation/foundation/attributescopes/foundationattributes/agreementconceptattribute'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/attributescopes/foundationattributes/agreementconceptattribute.json'
content_hash: 'sha256:ef686c2e6ee579d2'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [AttributeScopes](../../attributescopes.md) · [FoundationAttributes](../foundationattributes.md)

# AttributeScopes.FoundationAttributes.AgreementConceptAttribute

<sub>Enumeration</sub>

An attribute that represents grammatical agreement for objects that aren’t part of the inflected text.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@frozen enum AgreementConceptAttribute
```

## Overview

Use this formatting attribute for cases where you need to inflect text based on a term of address or phrase that’s not part of the inflected text.

### Agree with a term of address

In languages that rely on gender, the words and phrases in a sentence need to grammatically agree. For example, suppose you need to translate the following sentence into Spanish: _Anne is busy._

The challenge is that the system doesn’t know the preferred term of address for the person named _Anne_. Additionally, most often, the localization file only contains masculine forms of translated words. This means the system can’t correctly inflect other words in the sentence, such as _busy_, to agree with Anne’s feminine name. So the resulting translation is: _Anne está occupado_. _Ocupado_ is masculine, which isn’t the correct gender agreement for the sentence.

This is where the `agreeWithConcept` attribute can help. By wrapping the word you want to seek agreement on, _ocupado_, in an `agreeWithConcept` attribute pointing to an inflection concept of type [InflectionConcept.termsOfAddress(_:)](<../../inflectionconcept/termsofaddress(__).md>), the system makes the masculine word _ocupado_ agree with the [feminine](../../termofaddress/feminine.md) term of address _Anne_. You don’t need to include masculine and feminine forms of the translated words in your localization files. The system makes the terms agree for you.

The following steps ensure proper gender agreement in the translation:

1. Create a type associating the name _Anne_ with a [feminine](../../termofaddress/feminine.md) term of address. For example, create a `Contact` structure containing two properties — one property representing Anne’s name and another (an array) representing Anne’s preferred terms of address.
2. Create a [LocalizedStringResource](../../localizedstringresource.md) containing the English key phrase from the Spanish localization file to translate, along with the name _Anne_ as a placeholder variable representing the word to agree with.
3. Create an instance of [LocalizationOptions](../../attributedstring/localizationoptions.md) and pass an inflection concept of type [InflectionConcept.termsOfAddress(_:)](<../../inflectionconcept/termsofaddress(__).md>) containing the term of address associated with the name _Anne_ into its [concepts](../../attributedstring/localizationoptions/concepts.md) property
4. In the Spanish localization file, wrap the Spanish term, _ocupado_, in the `agreeWithConcept` attribute, with the index pointing to the first inflection concept instance in the [concepts](../../attributedstring/localizationoptions/concepts.md) property.
5. Then inflect the masculine word _ocupado_ into its feminine form _ocupada_ by passing the resource and options to a new [AttributedString](../../attributedstring.md).

```swift
struct Contact {
    let name: String
    let termsOfAddress: [TermOfAddress]
}

let contact = Contact(name: "Anne", termsOfAddress: [.feminine])

// Define the resource you want to apply grammatical agreement to.
let resource = LocalizedStringResource("\(contact.name) is busy.")
        
// Set the inflection concept to use a term of address.
var options = AttributedString.LocalizationOptions()
options.concepts = [.termsOfAddress(contact.termsOfAddress)]

// ____________
// In the Spanish localization file:
// "%@ is busy." = "%@ está ^[ocupado](agreeWithConcept: 1)."
// ____________

// Make a new string imposing grammatical agreement on the resource from the term of address.
let result = AttributedString(localized: resource, options: options)
// result == "Anne está ocupada."
```

### Agree with a localized phrase

Using a localized phrase for grammatical agreement is the same as using a term of address except you inflect on an [InflectionConcept.localizedPhrase(_:)](<../../inflectionconcept/localizedphrase(__).md>) instead of a term of address.

For example, suppose you need to translate the following sentence for a food order into Spanish: _Last time you ordered the small._

In English, the word _small_ can appear on its own. But in Spanish, that translated word needs to agree with the masculine or feminine noun it’s describing, which, in this case (_ensalada_), isn’t part of the sentence.

To achieve agreement, wrap the masculine word for _small_, _pequeño_, with the `agreeWithConcept` attribute. Then set it to point to the [InflectionConcept.localizedPhrase(_:)](<../../inflectionconcept/localizedphrase(__).md>) that matches its associated food item.

The following steps ensure proper gender agreement in the translation:

- Create a type associating the food order item to its size. For example, create an `Order` structure containing two localizable string properties for `item` and `size`.
- Add the necessary translations for the food items and the sizes to the Spanish localization file.
- Create a [LocalizedStringResource](../../localizedstringresource.md) containing the English key phrase from the Spanish localization file to translate, along with the placeholder variable representing the phrase to inflect (`order.size`).
- Create an instance of [LocalizationOptions](../../attributedstring/localizationoptions.md) and pass into its [concepts](../../attributedstring/localizationoptions/concepts.md) property an inflection concept of type [InflectionConcept.localizedPhrase(_:)](<../../inflectionconcept/localizedphrase(__).md>) passing in the placeholder variable representing the phrase to inflect for that translation (`order.item`).
- In the Spanish localization file, add `%@` placeholders for the word you want to substitute for the size. Wrap the Spanish phrase for the size with the `agreeWithConcept` attribute, with the index pointing to the first inflection concept instance in the [concepts](../../attributedstring/localizationoptions/concepts.md) property.
- Then inflect the masculine word _pequeño_ into its feminine form _pequeña_ by passing the resource and options to a new [AttributedString](../../attributedstring.md).

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
let resource = LocalizedStringResource("Last time you ordered the \(order.size).")

// ____________
// In the Spanish localization file:
// "Last time you ordered the %@." = "La última vez ordenaste ^[el %@](agreeWithConcept:1)."
// ____________

// Set the inflection concept to a feminine localized phrase.
var options = AttributedString.LocalizationOptions()
options.concepts = [.localizedPhrase(order.item)]

// Make a new string imposing grammatical agreement on the resource from the localized phrase.
let result = AttributedString(localized: resource, options: options)
// result == "La última vez ordenaste la pequeña."
```

## Relationships

- **Conforms To**: [AttributedStringKey](../../attributedstringkey.md), [BitwiseCopyable](../../../swift/bitwisecopyable.md), [Copyable](../../../swift/copyable.md), [DecodableAttributedStringKey](../../decodableattributedstringkey.md), [EncodableAttributedStringKey](../../encodableattributedstringkey.md), [MarkdownDecodableAttributedStringKey](../../markdowndecodableattributedstringkey.md), [SendableMetatype](../../../swift/sendablemetatype.md)

## See Also

### Using automatic grammar agreement attributes

- [inflect](inflect.md) — A scope for accessing an inflection rule attribute.
- [InflectionRuleAttribute](inflectionruleattribute.md) — A type for using an inflection rule as an attribute.
- [agreementArgument](agreementargument.md) — A scope for accessing an agreement argument attribute.
- [AgreementArgumentAttribute](agreementargumentattribute.md) — An attribute that represents grammatical agreement with an argument in a localized string.
- [agreementConcept](agreementconcept.md) — A scope for accessing an agreement concept attribute.
- [morphology](morphology.md) — A scope for accessing a morphology attribute.
- [MorphologyAttribute](morphologyattribute.md) — A type for using a morphology as an attribute.
- [referentConcept](referentconcept.md) — A scope for accessing a referent concept attribute.
- [ReferentConceptAttribute](referentconceptattribute.md) — An attribute that specifies a grammatical agreement concept for substituting pronouns in localized text.
- [inflectionAlternative](inflectionalternative.md) — A scope for accessing an inflection alternative attribute.
- [InflectionAlternativeAttribute](inflectionalternativeattribute.md) — An attribute that provides an alternative inflection phrase when the system can’t achieve grammatical agreement.
