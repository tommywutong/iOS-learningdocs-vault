---
title: NSDecimalSeparator
framework: Foundation
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [macOS 10.0+（10.5 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: /documentation/foundation/nsdecimalseparator
source_url: 'https://developer.apple.com/documentation/foundation/nsdecimalseparator'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsdecimalseparator.json'
content_hash: 'sha256:ea4f30d46196f603'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSDecimalSeparator

<sub>Global Variable</sub>

A string that specifies the decimal separator.

> [!warning] Deprecated
> Use [decimalSeparator](numberformatter/decimalseparator.md) or [currencyDecimalSeparator](numberformatter/currencydecimalseparator.md) (`NSNumberFormatter`)  or retrieve the `NSLocaleDecimalSeparator` from the current locale instead.

<sub>macOS</sub>

```objc
extern NSString * const NSDecimalSeparator;
```

## Discussion

The decimal separator separates the ones place from the tenths place. The default is “`.`”.

## See Also

### Numeric Information

- [NSCurrencySymbol](nscurrencysymbol.md) — A string that specifies the symbol used to denote currency in this language. _(deprecated)_
- [NSDecimalDigits](nsdecimaldigits.md) — Strings that identify the decimal digits in addition to or instead of the ASCII digits. _(deprecated)_
- [NSInternationalCurrencyString](nsinternationalcurrencystring.md) — A string containing a three-letter abbreviation for currency, following the ISO 4217 standard. _(deprecated)_
- [NSNegativeCurrencyFormatString](nsnegativecurrencyformatstring.md) — A format string that specifies how negative numbers are printed when representing a currency value. _(deprecated)_
- [NSPositiveCurrencyFormatString](nspositivecurrencyformatstring.md) — A format string that specifies how positive numbers are printed when representing a currency value. _(deprecated)_
- [NSThousandsSeparator](nsthousandsseparator.md) — A string that specifies the separator character for the thousands place of a decimal number. _(deprecated)_
