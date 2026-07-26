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
doc_path: /documentation/foundation/date/formatstyle/symbol/standalonemonth/defaultdigits
source_url: 'https://developer.apple.com/documentation/foundation/date/formatstyle/symbol/standalonemonth/defaultdigits'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/date/formatstyle/symbol/standalonemonth/defaultdigits.json'
content_hash: 'sha256:acba6273b090d511'
translated: false
---

> Navigation: [Technologies](../../../../../technologies.md) · [Foundation](../../../../../foundation.md) · [Date](../../../../date.md) · [FormatStyle](../../../formatstyle.md) · [Symbol](../../symbol.md) · [StandaloneMonth](../standalonemonth.md)

# defaultDigits

<sub>Type Property</sub>

The custom month format style that shows the minimum number of digits to represent a standalone month.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var defaultDigits: Date.FormatStyle.Symbol.StandaloneMonth { get }
```

## Discussion

This style uses representations like `1` for January and `10` for October.

## See Also

### Modifying a Standalone Month

- [abbreviated](abbreviated.md) — The abbreviated representation of a standalone month.
- [narrow](narrow.md) — The shortest representation of a standalone month.
- [twoDigits](twodigits.md) — The two-digit representation of a standalone month.
- [wide](wide.md) — The full representation of a standalone month.
