---
title: 'date(withCalendarFormat:timeZone:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+（8.0 起废弃）, iPadOS 2.0+（8.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）, macOS 10.4+（10.10 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/foundation/nsdate/date(withcalendarformat:timezone:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsdate/date(withcalendarformat:timezone:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsdate/date%28withcalendarformat%3Atimezone%3A%29.json'
content_hash: 'sha256:fdf4749e509c4565'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSDate](../nsdate.md)

# date(withCalendarFormat:timeZone:)

<sub>Instance Method</sub>

Converts the receiver to a calendar date with a given format string and time zone.

> [!warning] Deprecated
> Use [NSDate](../nsdate.md) methods to set the individual date values.

<sub>Mac Catalyst, macOS</sub>

```swift
func date(withCalendarFormat format: String?, timeZone aTimeZone: TimeZone?) -> NSCalendarDate
```

## Parameters

- `format` — The format for the returned string (see Date and Number Formatters in OS X v10.0 to 10.3 for a discussion of how to create the format string). Pass `nil` to use the default format string, “`%Y-%m-%d %H:%M:%S %z`” (this conforms to the international format `YYYY-MM-DD HH:MM:SS ±HHMM`.)

- `aTimeZone` — The time zone for the new calendar date. Pass `nil` to use the default time zone—specific to the current locale.

## Return Value

A new [NSCalendarDate](../nscalendardate.md) object bound to `format` and the time zone `aTimeZone`.

## See Also

### Legacy Operations

- [+ dateWithNaturalLanguageString:](<date(withnaturallanguagestring_).md>) — Creates and returns a date object set to the date and time specified by a given string. _(deprecated)_
- [+ dateWithNaturalLanguageString:locale:](<date(withnaturallanguagestring_locale_).md>) — Creates and returns a date object set to the date and time specified by a given string. _(deprecated)_
- [+ dateWithString:](<date(with_).md>) — Creates and returns a date object with a date and time value specified by a given string in the international string representation format (`YYYY-MM-DD HH:MM:SS ±HHMM`). _(deprecated)_
- [- initWithString:](<init(string_).md>) — Returns a date object initialized with a date and time value specified by a given string in the international string representation format. _(deprecated)_
- [- addTimeInterval:](<addtimeinterval(__).md>) — Returns a new date object that is set to a given number of seconds relative to the receiver. _(deprecated)_
- [- descriptionWithCalendarFormat:timeZone:locale:](<description(withcalendarformat_timezone_locale_).md>) — Returns a string representation of the date formatted as specified by given conversion specifiers. _(deprecated)_
