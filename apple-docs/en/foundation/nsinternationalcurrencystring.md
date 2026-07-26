---
title: NSInternationalCurrencyString
framework: Foundation
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [macOS 10.0+（10.5 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: /documentation/foundation/nsinternationalcurrencystring
source_url: 'https://developer.apple.com/documentation/foundation/nsinternationalcurrencystring'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsinternationalcurrencystring.json'
content_hash: 'sha256:5d32f90bf5b45f30'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSInternationalCurrencyString

<sub>Global Variable</sub>

A string containing a three-letter abbreviation for currency, following the ISO 4217 standard.

> [!warning] Deprecated
> Retrieve the `NSLocaleCurrencySymbol` from the current locale instead.

<sub>macOS</sub>

```objc
extern NSString * const NSInternationalCurrencyString;
```

## See Also

### Numeric Information

- [NSCurrencySymbol](nscurrencysymbol.md) — A string that specifies the symbol used to denote currency in this language. _(deprecated)_
- [NSDecimalDigits](nsdecimaldigits.md) — Strings that identify the decimal digits in addition to or instead of the ASCII digits. _(deprecated)_
- [NSDecimalSeparator](nsdecimalseparator.md) — A string that specifies the decimal separator. _(deprecated)_
- [NSNegativeCurrencyFormatString](nsnegativecurrencyformatstring.md) — A format string that specifies how negative numbers are printed when representing a currency value. _(deprecated)_
- [NSPositiveCurrencyFormatString](nspositivecurrencyformatstring.md) — A format string that specifies how positive numbers are printed when representing a currency value. _(deprecated)_
- [NSThousandsSeparator](nsthousandsseparator.md) — A string that specifies the separator character for the thousands place of a decimal number. _(deprecated)_
