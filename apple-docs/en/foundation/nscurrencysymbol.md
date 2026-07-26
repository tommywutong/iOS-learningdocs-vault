---
title: NSCurrencySymbol
framework: Foundation
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [macOS 10.0+（10.5 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: /documentation/foundation/nscurrencysymbol
source_url: 'https://developer.apple.com/documentation/foundation/nscurrencysymbol'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nscurrencysymbol.json'
content_hash: 'sha256:6a07a8ab90dbd06e'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSCurrencySymbol

<sub>Global Variable</sub>

A string that specifies the symbol used to denote currency in this language.

> [!warning] Deprecated
> These constants are deprecated in OS X v10.5. Where there are replacements, you can typically find them in [NumberFormatter](numberformatter.md) or [NSLocale](nslocale.md)—for example, [currencySymbol](numberformatter/currencysymbol.md), [currencyDecimalSeparator](numberformatter/currencydecimalseparator.md), and [thousandSeparator](numberformatter/thousandseparator.md)—otherwise you should use the patterns described in [Data Formatting Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/DataFormatting/DataFormatting.html#//apple_ref/doc/uid/10000029i).

<sub>macOS</sub>

```objc
extern NSString * const NSCurrencySymbol;
```

## Discussion

The default is “$”.

## See Also

### Numeric Information

- [NSDecimalDigits](nsdecimaldigits.md) — Strings that identify the decimal digits in addition to or instead of the ASCII digits. _(deprecated)_
- [NSDecimalSeparator](nsdecimalseparator.md) — A string that specifies the decimal separator. _(deprecated)_
- [NSInternationalCurrencyString](nsinternationalcurrencystring.md) — A string containing a three-letter abbreviation for currency, following the ISO 4217 standard. _(deprecated)_
- [NSNegativeCurrencyFormatString](nsnegativecurrencyformatstring.md) — A format string that specifies how negative numbers are printed when representing a currency value. _(deprecated)_
- [NSPositiveCurrencyFormatString](nspositivecurrencyformatstring.md) — A format string that specifies how positive numbers are printed when representing a currency value. _(deprecated)_
- [NSThousandsSeparator](nsthousandsseparator.md) — A string that specifies the separator character for the thousands place of a decimal number. _(deprecated)_
