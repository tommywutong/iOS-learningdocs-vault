---
title: NSPositiveCurrencyFormatString
framework: Foundation
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [macOS 10.0+（10.5 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: /documentation/foundation/nspositivecurrencyformatstring
source_url: 'https://developer.apple.com/documentation/foundation/nspositivecurrencyformatstring'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nspositivecurrencyformatstring.json'
content_hash: 'sha256:c679cb52352c62c2'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSPositiveCurrencyFormatString

<sub>Global Variable</sub>

A format string that specifies how positive numbers are printed when representing a currency value.

> [!warning] Deprecated
> Use the appropriate API from [NumberFormatter](numberformatter.md) instead—see [Data Formatting Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/DataFormatting/DataFormatting.html#//apple_ref/doc/uid/10000029i).

<sub>macOS</sub>

```objc
extern NSString * const NSPositiveCurrencyFormatString;
```

## Discussion

The default is `$9,999.00`.

## See Also

### Numeric Information

- [NSCurrencySymbol](nscurrencysymbol.md) — A string that specifies the symbol used to denote currency in this language. _(deprecated)_
- [NSDecimalDigits](nsdecimaldigits.md) — Strings that identify the decimal digits in addition to or instead of the ASCII digits. _(deprecated)_
- [NSDecimalSeparator](nsdecimalseparator.md) — A string that specifies the decimal separator. _(deprecated)_
- [NSInternationalCurrencyString](nsinternationalcurrencystring.md) — A string containing a three-letter abbreviation for currency, following the ISO 4217 standard. _(deprecated)_
- [NSNegativeCurrencyFormatString](nsnegativecurrencyformatstring.md) — A format string that specifies how negative numbers are printed when representing a currency value. _(deprecated)_
- [NSThousandsSeparator](nsthousandsseparator.md) — A string that specifies the separator character for the thousands place of a decimal number. _(deprecated)_
