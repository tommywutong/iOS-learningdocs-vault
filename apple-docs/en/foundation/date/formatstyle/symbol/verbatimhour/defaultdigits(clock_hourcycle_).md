---
title: 'defaultDigits(clock:hourCycle:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/date/formatstyle/symbol/verbatimhour/defaultdigits(clock:hourcycle:)'
source_url: 'https://developer.apple.com/documentation/foundation/date/formatstyle/symbol/verbatimhour/defaultdigits(clock:hourcycle:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/date/formatstyle/symbol/verbatimhour/defaultdigits%28clock%3Ahourcycle%3A%29.json'
content_hash: 'sha256:d8b28680a77d907e'
translated: false
---

> Navigation: [Technologies](../../../../../technologies.md) · [Foundation](../../../../../foundation.md) · [Date](../../../../date.md) · [FormatStyle](../../../formatstyle.md) · [Symbol](../../symbol.md) · [VerbatimHour](../verbatimhour.md)

# defaultDigits(clock:hourCycle:)

<sub>Type Method</sub>

Creates a custom format style portraying the minimum number of digits that represents the hour.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func defaultDigits(clock: Date.FormatStyle.Symbol.VerbatimHour.Clock, hourCycle: Date.FormatStyle.Symbol.VerbatimHour.HourCycle) -> Date.FormatStyle.Symbol.VerbatimHour
```

## Parameters

- `clock` — The clock representation.

- `hourCycle` — The start of the clock representation.

## Return Value

An hour format style customized according to the specified clock representation and the start of the clock representation.

## See Also

### Modifying a Verbatim Hour

- [twoDigits(clock:hourCycle:)](<twodigits(clock_hourcycle_).md>) — Creates a custom format style portraying two digits that represent the hour.
