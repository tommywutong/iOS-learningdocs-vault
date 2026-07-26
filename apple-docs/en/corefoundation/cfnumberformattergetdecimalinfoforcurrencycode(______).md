---
title: 'CFNumberFormatterGetDecimalInfoForCurrencyCode(_:_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfnumberformattergetdecimalinfoforcurrencycode(_:_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfnumberformattergetdecimalinfoforcurrencycode(_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfnumberformattergetdecimalinfoforcurrencycode%28_%3A_%3A_%3A%29.json'
content_hash: 'sha256:d13afb33313190dc'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFNumberFormatterGetDecimalInfoForCurrencyCode(_:_:_:)

<sub>Function</sub>

Returns the number of fraction digits that should be displayed, and the rounding increment, for a given currency.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFNumberFormatterGetDecimalInfoForCurrencyCode(_ currencyCode: CFString!, _ defaultFractionDigits: UnsafeMutablePointer<Int32>!, _ roundingIncrement: UnsafeMutablePointer<Double>!) -> Bool
```

## Parameters

- `currencyCode` — A string containing a ISO 4217 3-letter currency code. For example, AUD for Australian Dollars, EUR for Euros.

- `defaultFractionDigits` — Upon return, contains the number of fraction digits that should be displayed for the currency specified by `currencyCode`.

- `roundingIncrement` — Upon return, contains the rounding increment for the currency specified by `currencyCode`, or `0.0` if no rounding is done by the currency.

## Return Value

`true` if the information was obtained successfully, otherwise `false` (for example, if the currency code is unknown or the information is not available).

## Discussion

The returned values are not localized because these are properties of the currency.

## See Also

### Formatting Values

- [CFNumberFormatterCreateNumberFromString](<cfnumberformattercreatenumberfromstring(__________).md>) — Returns a number object representing a given string.
- [CFNumberFormatterCreateStringWithNumber](<cfnumberformattercreatestringwithnumber(______).md>) — Returns a string representation of the given number using the specified number formatter.
- [CFNumberFormatterCreateStringWithValue](<cfnumberformattercreatestringwithvalue(________).md>) — Returns a string representation of the given number or value using the specified number formatter.
- [CFNumberFormatterGetValueFromString](<cfnumberformattergetvaluefromstring(__________).md>) — Returns a number or value representing a given string.
