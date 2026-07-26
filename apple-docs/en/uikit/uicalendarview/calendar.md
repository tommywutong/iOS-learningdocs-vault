---
title: calendar
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uicalendarview/calendar
source_url: 'https://developer.apple.com/documentation/uikit/uicalendarview/calendar'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicalendarview/calendar.json'
content_hash: 'sha256:f647a599aee1f94e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICalendarView](../uicalendarview.md)

# calendar

<sub>Instance Property</sub>

The calendar that the calendar view illustrates.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var calendar: Calendar { get set }
```

## Discussion

Defaults to [current](../../foundation/nscalendar/current.md), which is the user’s current calendar set in Settings.

## See Also

### Setting calendar details

- [locale](locale.md) — The locale the calendar view uses for calendar conventions.
- [timeZone](timezone.md) — The time zone from the date the calendar view displays.
