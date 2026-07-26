---
title: 'timeZone(_:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/date/formatstyle/timezone(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/date/formatstyle/timezone(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/date/formatstyle/timezone%28_%3A%29.json'
content_hash: 'sha256:aaade4edc07d5d16'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [Date](../../date.md) · [FormatStyle](../formatstyle.md)

# timeZone(_:)

<sub>Instance Method</sub>

Modifies the date format style to use the specified time zone format style.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func timeZone(_ format: Date.FormatStyle.Symbol.TimeZone = .specificName(.short)) -> Date.FormatStyle
```

## Parameters

- `format` — The time zone format style applied to the date format style.

## Return Value

A date format style modified to include the specified time zone format style.

## Discussion

Values of [TimeZone](symbol/timezone.md) are [exemplarLocation](symbol/timezone/exemplarlocation.md) and [genericLocation](symbol/timezone/genericlocation.md).

Static methods that return [TimeZone](symbol/timezone.md) objects include [genericName(_:)](<symbol/timezone/genericname(__).md>), [identifier(_:)](<symbol/timezone/identifier(__).md>),  [iso8601(_:)](<symbol/timezone/iso8601(__).md>), [localizedGMT(_:)](<symbol/timezone/localizedgmt(__).md>), and [specificName(_:)](<symbol/timezone/specificname(__).md>).

## See Also

### Specifying the Time Format

- [hour(_:)](<hour(__).md>) — Modifies the date format style to use the specified hour format style.
- [minute(_:)](<minute(__).md>) — Modifies the date format style to use the specified minute format style.
- [second(_:)](<second(__).md>) — Modifies the date format style to use the specified second format style.
- [secondFraction(_:)](<secondfraction(__).md>) — Modifies the date format style to use the specified second fraction format style.
- [TimeStyle](timestyle.md) — Type that defines time styles varied in length or components included.
