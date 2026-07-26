---
title: correction
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nstextcheckingresult/checkingtype/correction
source_url: 'https://developer.apple.com/documentation/foundation/nstextcheckingresult/checkingtype/correction'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nstextcheckingresult/checkingtype/correction.json'
content_hash: 'sha256:00c10d555d539406'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [NSTextCheckingResult](../../nstextcheckingresult.md) · [CheckingType](../checkingtype.md)

# correction

<sub>Type Property</sub>

Performs autocorrection on misspelled words.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var correction: NSTextCheckingResult.CheckingType { get }
```

## See Also

### Constants

- [NSTextCheckingTypeOrthography](orthography.md) — Attempts to identify the language
- [NSTextCheckingTypeSpelling](spelling.md) — Checks spelling.
- [NSTextCheckingTypeGrammar](grammar.md) — Checks grammar.
- [NSTextCheckingTypeDate](date.md) — Attempts to locate dates.
- [NSTextCheckingTypeAddress](address.md) — Attempts to locate addresses.
- [NSTextCheckingTypeLink](link.md) — Attempts to locate URL links.
- [NSTextCheckingTypeQuote](quote.md) — Replaces quotes with smart quotes.
- [NSTextCheckingTypeDash](dash.md) — Replaces dashes with em-dashes.
- [NSTextCheckingTypeReplacement](replacement.md) — Replaces characters such as (c) with the appropriate symbol (in this case ©).
- [NSTextCheckingTypeRegularExpression](regularexpression.md) — Matches a regular expression.
- [NSTextCheckingTypePhoneNumber](phonenumber.md) — Matches a phone number.
- [NSTextCheckingTypeTransitInformation](transitinformation.md) — Matches a transit information, for example, flight information.
