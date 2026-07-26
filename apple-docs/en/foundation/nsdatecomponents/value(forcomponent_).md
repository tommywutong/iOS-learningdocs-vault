---
title: 'value(forComponent:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsdatecomponents/value(forcomponent:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsdatecomponents/value(forcomponent:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsdatecomponents/value%28forcomponent%3A%29.json'
content_hash: 'sha256:316953c6ca41e24c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSDateComponents](../nsdatecomponents.md)

# value(forComponent:)

<sub>Instance Method</sub>

Returns the value for a given calendar unit.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func value(forComponent unit: NSCalendar.Unit) -> Int
```

## Parameters

- `unit` — The calendar unit for which to retrieve its value. Do not pass [NSCalendarUnitCalendar](../nscalendar/unit/calendar.md) or [NSCalendarUnitTimeZone](../nscalendar/unit/timezone.md).

## Return Value

The value for the given calendar unit.

## Discussion

This method allows for component values to be retrieved for an [Unit](../nscalendar/unit.md) value.

## See Also

### Accessing Components as Calendrical Units

- [- setValue:forComponent:](<setvalue(__forcomponent_).md>) — Sets a value for a given calendar unit.
- [Unit](../nscalendar/unit.md) — Calendrical units such as year, month, day and hour.
