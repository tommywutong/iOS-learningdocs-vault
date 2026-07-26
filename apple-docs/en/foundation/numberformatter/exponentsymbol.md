---
title: exponentSymbol
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/numberformatter/exponentsymbol
source_url: 'https://developer.apple.com/documentation/foundation/numberformatter/exponentsymbol'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/numberformatter/exponentsymbol.json'
content_hash: 'sha256:588b16a09e7a51b8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NumberFormatter](../numberformatter.md)

# exponentSymbol

<sub>Instance Property</sub>

The string used to represent an exponent symbol.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var exponentSymbol: String! { get set }
```

## Discussion

By default, this property is set to the latin capital letter e (E).

The exponent symbol is the “E” or “e” in the scientific notation of numbers, as in “1.0E+42”.

## See Also

### Related Documentation

- [NSNumberFormatterScientificStyle](style/scientific.md) — A scientific style format.

### Configuring Numeric Symbols

- [percentSymbol](percentsymbol.md) — The string used to represent a percent symbol.
- [perMillSymbol](permillsymbol.md) — The string used to represent a per-mill (per-thousand) symbol.
- [minusSign](minussign.md) — The string used to represent a minus sign.
- [plusSign](plussign.md) — The string used to represent a plus sign.
- [zeroSymbol](zerosymbol.md) — The string used to represent a zero value.
- [nilSymbol](nilsymbol.md) — The string used to represent a `nil` value.
- [notANumberSymbol](notanumbersymbol.md) — The string used to represent a NaN (“not a number”) value.
- [negativeInfinitySymbol](negativeinfinitysymbol.md) — The string used to represent a negative infinity symbol.
- [positiveInfinitySymbol](positiveinfinitysymbol.md) — The string used to represent a positive infinity symbol.
