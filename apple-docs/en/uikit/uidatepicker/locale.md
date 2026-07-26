---
title: locale
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uidatepicker/locale
source_url: 'https://developer.apple.com/documentation/uikit/uidatepicker/locale'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uidatepicker/locale.json'
content_hash: 'sha256:7b843b65f322418a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIDatePicker](../uidatepicker.md)

# locale

<sub>Instance Property</sub>

The locale used by the date picker.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var locale: Locale? { get set }
```

## Discussion

The default value is the current locale as returned by the [current](../../foundation/nslocale/current.md) property of [NSLocale](../../foundation/nslocale.md), or the locale used by the date picker’s calendar. Locales encapsulate information about facets of a language or culture, such as the way dates are formatted.

## See Also

### Managing the date and calendar

- [calendar](calendar.md) — The calendar to use for the date picker.
- [date](date.md) — The date displayed by the date picker.
- [- setDate:animated:](<setdate(__animated_).md>) — Sets the date to display in the date picker, with an option to animate the setting.
- [timeZone](timezone.md) — The time zone reflected in the date displayed by the date picker.
