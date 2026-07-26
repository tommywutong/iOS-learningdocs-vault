---
title: 'with12s(_:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/date/formatstyle/symbol/dayperiod/with12s(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/date/formatstyle/symbol/dayperiod/with12s(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/date/formatstyle/symbol/dayperiod/with12s%28_%3A%29.json'
content_hash: 'sha256:73c89d3250a89aa5'
translated: false
---

> Navigation: [Technologies](../../../../../technologies.md) · [Foundation](../../../../../foundation.md) · [Date](../../../../date.md) · [FormatStyle](../../../formatstyle.md) · [Symbol](../../symbol.md) · [DayPeriod](../dayperiod.md)

# with12s(_:)

<sub>Type Method</sub>

Static factory method that creates a custom day period format style using a style that represents midday and midnight.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func with12s(_ width: Date.FormatStyle.Symbol.DayPeriod.Width) -> Date.FormatStyle.Symbol.DayPeriod
```

## Parameters

- `width` — Specifies the width of the string result.

## Return Value

A day period format style appropriate for the locale and specified width.

## See Also

### Modifying a Day Period

- [conversational(_:)](<conversational(__).md>) — Static factory method that creates a custom day period format style using a conversational style.
- [standard(_:)](<standard(__).md>) — Static factory method that creates a custom day period format style using a standard style.
