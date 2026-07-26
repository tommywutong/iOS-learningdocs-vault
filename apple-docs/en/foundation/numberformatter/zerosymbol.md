---
title: zeroSymbol
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/numberformatter/zerosymbol
source_url: 'https://developer.apple.com/documentation/foundation/numberformatter/zerosymbol'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/numberformatter/zerosymbol.json'
content_hash: 'sha256:141f2f0506f4eb47'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NumberFormatter](../numberformatter.md)

# zeroSymbol

<sub>Instance Property</sub>

The string used to represent a zero value.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var zeroSymbol: String? { get set }
```

## Discussion

If not specified, zero values are formatted normally.

You might, for example, set this property to “` ``-`` `” in a spreadsheet used for accounting.

## See Also

### Configuring Numeric Symbols

- [percentSymbol](percentsymbol.md) — The string used to represent a percent symbol.
- [perMillSymbol](permillsymbol.md) — The string used to represent a per-mill (per-thousand) symbol.
- [minusSign](minussign.md) — The string used to represent a minus sign.
- [plusSign](plussign.md) — The string used to represent a plus sign.
- [exponentSymbol](exponentsymbol.md) — The string used to represent an exponent symbol.
- [nilSymbol](nilsymbol.md) — The string used to represent a `nil` value.
- [notANumberSymbol](notanumbersymbol.md) — The string used to represent a NaN (“not a number”) value.
- [negativeInfinitySymbol](negativeinfinitysymbol.md) — The string used to represent a negative infinity symbol.
- [positiveInfinitySymbol](positiveinfinitysymbol.md) — The string used to represent a positive infinity symbol.
