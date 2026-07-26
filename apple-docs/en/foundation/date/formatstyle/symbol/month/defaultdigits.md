---
title: defaultDigits
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/date/formatstyle/symbol/month/defaultdigits
source_url: 'https://developer.apple.com/documentation/foundation/date/formatstyle/symbol/month/defaultdigits'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/date/formatstyle/symbol/month/defaultdigits.json'
content_hash: 'sha256:0c75595fba7d8b7e'
translated: false
---

> Navigation: [Technologies](../../../../../technologies.md) · [Foundation](../../../../../foundation.md) · [Date](../../../../date.md) · [FormatStyle](../../../formatstyle.md) · [Symbol](../../symbol.md) · [Month](../month.md)

# defaultDigits

<sub>Type Property</sub>

Custom month format style showing the minimum number of digits that represents the numeric month.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var defaultDigits: Date.FormatStyle.Symbol.Month { get }
```

## Discussion

This style represents the month like `1` or `12`.

## See Also

### Modifying a Month

- [abbreviated](abbreviated.md) — The abbreviated representation of a month.
- [narrow](narrow.md) — The shortest representation of a month.
- [twoDigits](twodigits.md) — The custom month format style that uses two digits to represent the numeric month.
- [wide](wide.md) — The full representation of a month.
