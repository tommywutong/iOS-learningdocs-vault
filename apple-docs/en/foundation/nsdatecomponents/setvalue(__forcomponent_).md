---
title: 'setValue(_:forComponent:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsdatecomponents/setvalue(_:forcomponent:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsdatecomponents/setvalue(_:forcomponent:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsdatecomponents/setvalue%28_%3Aforcomponent%3A%29.json'
content_hash: 'sha256:cbe6a275900ecaf4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSDateComponents](../nsdatecomponents.md)

# setValue(_:forComponent:)

<sub>Instance Method</sub>

Sets a value for a given calendar unit.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func setValue(_ value: Int, forComponent unit: NSCalendar.Unit)
```

## Parameters

- `value` — The value to set for the `unit` component.

- `unit` — The calendar unit for which to set `value`. Do not pass [NSCalendarUnitCalendar](../nscalendar/unit/calendar.md) or [NSCalendarUnitTimeZone](../nscalendar/unit/timezone.md).

## Discussion

This method allows for component values to be set for an [Unit](../nscalendar/unit.md) value.

## See Also

### Accessing Components as Calendrical Units

- [- valueForComponent:](<value(forcomponent_).md>) — Returns the value for a given calendar unit.
- [Unit](../nscalendar/unit.md) — Calendrical units such as year, month, day and hour.
