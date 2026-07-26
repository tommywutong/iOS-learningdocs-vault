---
title: NSTextCheckingResult.CheckingType
framework: Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nstextcheckingresult/checkingtype
source_url: 'https://developer.apple.com/documentation/foundation/nstextcheckingresult/checkingtype'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nstextcheckingresult/checkingtype.json'
content_hash: 'sha256:015d1fe1a539dd58'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSTextCheckingResult](../nstextcheckingresult.md)

# NSTextCheckingResult.CheckingType

<sub>Structure</sub>

These constants specify the type of checking the methods should do. They are returned by [resultType](resulttype.md).

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct CheckingType
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [ExpressibleByArrayLiteral](../../swift/expressiblebyarrayliteral.md), [OptionSet](../../swift/optionset.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md), [SetAlgebra](../../swift/setalgebra.md)

## Topics

### Constants

- [NSTextCheckingTypeOrthography](checkingtype/orthography.md) — Attempts to identify the language
- [NSTextCheckingTypeSpelling](checkingtype/spelling.md) — Checks spelling.
- [NSTextCheckingTypeGrammar](checkingtype/grammar.md) — Checks grammar.
- [NSTextCheckingTypeDate](checkingtype/date.md) — Attempts to locate dates.
- [NSTextCheckingTypeAddress](checkingtype/address.md) — Attempts to locate addresses.
- [NSTextCheckingTypeLink](checkingtype/link.md) — Attempts to locate URL links.
- [NSTextCheckingTypeQuote](checkingtype/quote.md) — Replaces quotes with smart quotes.
- [NSTextCheckingTypeDash](checkingtype/dash.md) — Replaces dashes with em-dashes.
- [NSTextCheckingTypeReplacement](checkingtype/replacement.md) — Replaces characters such as (c) with the appropriate symbol (in this case ©).
- [NSTextCheckingTypeCorrection](checkingtype/correction.md) — Performs autocorrection on misspelled words.
- [NSTextCheckingTypeRegularExpression](checkingtype/regularexpression.md) — Matches a regular expression.
- [NSTextCheckingTypePhoneNumber](checkingtype/phonenumber.md) — Matches a phone number.
- [NSTextCheckingTypeTransitInformation](checkingtype/transitinformation.md) — Matches a transit information, for example, flight information.

### Initializers

- [init(rawValue:)](<checkingtype/init(rawvalue_).md>)

### Type Properties

- [allCustomTypes](checkingtype/allcustomtypes.md)
- [allSystemTypes](checkingtype/allsystemtypes.md)
- [allTypes](checkingtype/alltypes.md)

## See Also

### Constants

- [Keys for Transit Components](../keys-for-transit-components.md) — The following constants identify the possible keys returned in the components dictionary.
- [Keys for Address Components](../keys-for-address-components.md) — The following constants identify the possible keys returned in the [addressComponents](addresscomponents.md) dictionary.
- [NSTextCheckingTypes](../nstextcheckingtypes.md) — Defines the types of checking that are available. These values can be combined using the C-bitwise OR operator. The system supports its own internal types, and the user can extend those types by subclassing `NSTextCheckingResult` and adding their own custom types.
- [NSTextCheckingKey](../nstextcheckingkey.md)
- [Anonymous](../1476845-anonymous.md)
