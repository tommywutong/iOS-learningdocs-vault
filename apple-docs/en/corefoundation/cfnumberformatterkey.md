---
title: CFNumberFormatterKey
framework: Core Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/cfnumberformatterkey
source_url: 'https://developer.apple.com/documentation/corefoundation/cfnumberformatterkey'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfnumberformatterkey.json'
content_hash: 'sha256:d0e1de8c14a9a1a9'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFNumberFormatterKey

<sub>Structure</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct CFNumberFormatterKey
```

## Relationships

- **Conforms To**: [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Type Properties

- [kCFNumberFormatterAlwaysShowDecimalSeparator](cfnumberformatterkey/alwaysshowdecimalseparator.md) — Specifies if the result of converting a value to a string should always contain the decimal separator, even if the number is an integer.
- [kCFNumberFormatterCurrencyCode](cfnumberformatterkey/currencycode.md) — Specifies the currency code, a `CFString` object.
- [kCFNumberFormatterCurrencyDecimalSeparator](cfnumberformatterkey/currencydecimalseparator.md) — Specifies the currency decimal separator, a `CFString` object.
- [kCFNumberFormatterCurrencyGroupingSeparator](cfnumberformatterkey/currencygroupingseparator.md) — Specifies the grouping symbol to use when placing a currency value within a string, a `CFString` object.
- [kCFNumberFormatterCurrencySymbol](cfnumberformatterkey/currencysymbol.md) — Specifies the symbol for the currency, a `CFString` object.
- [kCFNumberFormatterDecimalSeparator](cfnumberformatterkey/decimalseparator.md) — Specifies the decimal separator, a `CFString` object.
- [kCFNumberFormatterDefaultFormat](cfnumberformatterkey/defaultformat.md) — The original format string for the formatter (given the date and time style and locale specified at creation), a `CFString` object.
- [kCFNumberFormatterExponentSymbol](cfnumberformatterkey/exponentsymbol.md) — Specifies the exponent symbol (“E” or “e”) in the scientific notation of numbers (for example, as in `1.0e+56`), a `CFString` object.
- [kCFNumberFormatterFormatWidth](cfnumberformatterkey/formatwidth.md) — Specifies the width of a formatted number within a string that is either left justified or right justified based on the value of [kCFNumberFormatterPaddingPosition](cfnumberformatterkey/paddingposition.md), a `CFNumber` object.
- [kCFNumberFormatterGroupingSeparator](cfnumberformatterkey/groupingseparator.md) — Specifies the grouping separator, a `CFString` object.
- [kCFNumberFormatterGroupingSize](cfnumberformatterkey/groupingsize.md) — Specifies how often the “thousands” or grouping separator appears, as in “10,000,000”, a `CFNumber` object.
- [kCFNumberFormatterInfinitySymbol](cfnumberformatterkey/infinitysymbol.md) — Specifies the string that is used to represent the symbol for infinity, a `CFString` object.
- [kCFNumberFormatterInternationalCurrencySymbol](cfnumberformatterkey/internationalcurrencysymbol.md) — Specifies the international currency symbol to use when placing a formatted number within a string, a `CFString` object.
- [kCFNumberFormatterIsLenient](cfnumberformatterkey/islenient.md) — Specifies whether the formatter is lenient, a`CFBoolean` object.
- [kCFNumberFormatterMaxFractionDigits](cfnumberformatterkey/maxfractiondigits.md) — Specifies the maximum number of digits after a decimal point, a `CFNumber` object.
- [kCFNumberFormatterMaxIntegerDigits](cfnumberformatterkey/maxintegerdigits.md) — Specifies the maximum number of integer digits before a decimal point, a `CFNumber` object.
- [kCFNumberFormatterMaxSignificantDigits](cfnumberformatterkey/maxsignificantdigits.md) — Specifies the maximum number of significant digits to use, a`CFNumber` object.
- [kCFNumberFormatterMinFractionDigits](cfnumberformatterkey/minfractiondigits.md) — Specifies the minimum number of digits after a decimal point, a `CFNumber` object.
- [kCFNumberFormatterMinIntegerDigits](cfnumberformatterkey/minintegerdigits.md) — Specifies the minimum number of integer digits before a decimal point, a `CFNumber` object.
- [kCFNumberFormatterMinSignificantDigits](cfnumberformatterkey/minsignificantdigits.md) — Specifies the minimum number of significant digits to use, a`CFNumber` object.
- [kCFNumberFormatterMinusSign](cfnumberformatterkey/minussign.md) — Specifies the symbol for the minus sign, a `CFString` object.
- [kCFNumberFormatterMultiplier](cfnumberformatterkey/multiplier.md) — Specifies the multiplier to use when placing a formatted number within a string, a `CFNumber` object.
- [kCFNumberFormatterNaNSymbol](cfnumberformatterkey/nansymbol.md) — Specifies the string that is used to represent NaN (“not a number”) when values are converted to strings, a `CFString` object.
- [kCFNumberFormatterNegativePrefix](cfnumberformatterkey/negativeprefix.md) — Specifies the minus sign prefix symbol to use when placing a formatted number within a string, a `CFString` object.
- [kCFNumberFormatterNegativeSuffix](cfnumberformatterkey/negativesuffix.md) — Specifies the minus sign suffix symbol to use when placing a formatted number within a string, a `CFString` object.
- [kCFNumberFormatterPaddingCharacter](cfnumberformatterkey/paddingcharacter.md) — Specifies the padding character to use when placing a formatted number within a string, a `CFString` object.
- [kCFNumberFormatterPaddingPosition](cfnumberformatterkey/paddingposition.md) — Specifies the position of a formatted number within a string, a `CFNumber` object.
- [kCFNumberFormatterPerMillSymbol](cfnumberformatterkey/permillsymbol.md) — Specifies the per mill (1/1000) symbol to use when placing a formatted number within a string, a `CFString` object.
- [kCFNumberFormatterPercentSymbol](cfnumberformatterkey/percentsymbol.md) — Specifies the string that is used to represent the percent symbol, a `CFString` object.
- [kCFNumberFormatterPlusSign](cfnumberformatterkey/plussign.md) — Specifies the symbol for the plus sign, a `CFString` object.
- [kCFNumberFormatterPositivePrefix](cfnumberformatterkey/positiveprefix.md) — Specifies the plus sign prefix symbol to use when placing a formatted number within a string, a `CFString` object.
- [kCFNumberFormatterPositiveSuffix](cfnumberformatterkey/positivesuffix.md) — Specifies the plus sign suffix symbol to use when placing a formatted number within a string, a `CFString` object.
- [kCFNumberFormatterRoundingIncrement](cfnumberformatterkey/roundingincrement.md) — Specifies a positive rounding increment, or `0.0` to disable rounding, a `CFNumber` object.
- [kCFNumberFormatterRoundingMode](cfnumberformatterkey/roundingmode.md) — Specifies how the last digit is rounded, as when `3.1415926535…` is rounded to three decimal places, as in `3.142`. See [CFNumberFormatterRoundingMode](cfnumberformatterroundingmode.md) for possible values.
- [kCFNumberFormatterSecondaryGroupingSize](cfnumberformatterkey/secondarygroupingsize.md) — Specifies how often the secondary grouping separator appears, a `CFNumber` object.
- [kCFNumberFormatterUseGroupingSeparator](cfnumberformatterkey/usegroupingseparator.md) — Specifies if the grouping separator should be used, a `CFBoolean` object.
- [kCFNumberFormatterUseSignificantDigits](cfnumberformatterkey/usesignificantdigits.md) — Specifies the whether the formatter uses significant digits, a `CFBoolean` object.
- [kCFNumberFormatterZeroSymbol](cfnumberformatterkey/zerosymbol.md) — Specifies the string that is used to represent zero, a `CFString` object.
- [kCFNumberFormatterMinGroupingDigits](cfnumberformatterkey/mingroupingdigits.md)

### Initializers

- [init(rawValue:)](<cfnumberformatterkey/init(rawvalue_).md>)

## See Also

### Data Types

- [CFAllocatorTypeID](cfallocatortypeid.md)
- [CFCalendarIdentifier](cfcalendaridentifier.md)
- [CFDateFormatterKey](cfdateformatterkey.md)
- [CFErrorDomain](cferrordomain.md)
- [CFLocaleIdentifier](cflocaleidentifier.md)
- [CFLocaleKey](cflocalekey.md)
- [CFNotificationName](cfnotificationname.md)
- [CFRunLoopMode](cfrunloopmode.md)
- [CFStreamPropertyKey](cfstreampropertykey.md)
- [CFTypeRef](cftyperef.md) — An untyped “generic” reference to any Core Foundation object.
