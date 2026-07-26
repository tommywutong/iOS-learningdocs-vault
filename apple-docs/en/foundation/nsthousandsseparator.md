---
title: NSThousandsSeparator
framework: Foundation
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [macOS 10.0+（10.5 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: /documentation/foundation/nsthousandsseparator
source_url: 'https://developer.apple.com/documentation/foundation/nsthousandsseparator'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsthousandsseparator.json'
content_hash: 'sha256:a3da5050c116479d'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSThousandsSeparator

<sub>Global Variable</sub>

A string that specifies the separator character for the thousands place of a decimal number.

> [!warning] Deprecated
> Retrieve the `NSLocaleGroupingSeparator` from the current locale instead.

<sub>macOS</sub>

```objc
extern NSString * const NSThousandsSeparator;
```

## Discussion

The default is a comma.

## See Also

### Numeric Information

- [NSCurrencySymbol](nscurrencysymbol.md) — A string that specifies the symbol used to denote currency in this language. _(deprecated)_
- [NSDecimalDigits](nsdecimaldigits.md) — Strings that identify the decimal digits in addition to or instead of the ASCII digits. _(deprecated)_
- [NSDecimalSeparator](nsdecimalseparator.md) — A string that specifies the decimal separator. _(deprecated)_
- [NSInternationalCurrencyString](nsinternationalcurrencystring.md) — A string containing a three-letter abbreviation for currency, following the ISO 4217 standard. _(deprecated)_
- [NSNegativeCurrencyFormatString](nsnegativecurrencyformatstring.md) — A format string that specifies how negative numbers are printed when representing a currency value. _(deprecated)_
- [NSPositiveCurrencyFormatString](nspositivecurrencyformatstring.md) — A format string that specifies how positive numbers are printed when representing a currency value. _(deprecated)_
