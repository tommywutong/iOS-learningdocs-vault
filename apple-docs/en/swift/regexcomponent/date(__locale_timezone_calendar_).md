---
title: 'date(_:locale:timeZone:calendar:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/regexcomponent/date(_:locale:timezone:calendar:)'
source_url: 'https://developer.apple.com/documentation/swift/regexcomponent/date(_:locale:timezone:calendar:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/regexcomponent/date%28_%3Alocale%3Atimezone%3Acalendar%3A%29.json'
content_hash: 'sha256:59fe4bd47a9032e5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [RegexComponent](../regexcomponent.md)

# date(_:locale:timeZone:calendar:)

<sub>Type Method</sub>

Creates a regex component that matches a localized date string formatted in accordance with a style, capturing it as a Foundation date.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func date(_ style: Date.FormatStyle.DateStyle, locale: Locale, timeZone: TimeZone, calendar: Calendar? = nil) -> Date.ParseStrategy
```

## Parameters

- `style` — A [Date.FormatStyle.DateStyle](../../foundation/date/formatstyle/datestyle.md) to use when matching date substrings.

- `locale` — The locale to use when matching date substrings. Matching uses this locale to evaluate the order of date components. It also uses the locale’s language for date format styles that use words.

- `timeZone` — The time zone to use when returning a captured [Date](../../foundation/date.md). The returned date’s time value is `00:00:00` in this time zone.

- `calendar` — The calendar to use when matching date substrings. If `nil`, matching uses the default calendar of the specified `locale`.

## Return Value

A `RegexComponent` that matches date substrings as Foundation [Date](../../foundation/date.md) instances.

## Discussion

This method matches date substrings in accordance with the formatting of Foundation’s [Date.FormatStyle](../../foundation/date/formatstyle.md).

If a time value follows the date substring, the matcher ignores it, treating it as any other character sequence. To match date and time substrings, use [dateTime(date:time:locale:timeZone:calendar:)](<datetime(date_time_locale_timezone_calendar_).md>).

The following example creates a [Regex](../regex.md) that matches a date formatted with the [numeric](../../foundation/date/formatstyle/datestyle/numeric.md) style in the `en_US` locale. It then matches this regex against a source string containing a date with this format, some whitespace, a substring, more whitespace, and a currency value.

```swift
let source = "7/31/2022  Lemon-lime slushie      $1.99"
let matcher = Regex {
    Capture {
        One(.date(.numeric,
                  locale: Locale(identifier: "en_US"),
                  timeZone: TimeZone(identifier: "PST")!))
    }
}
guard let match = source.firstMatch(of: matcher) else { return }
let date = match.1 // date == Jul 31, 2022 at 12:00 AM PST
```

## See Also

### Matching dates and times

- [date(format:locale:timeZone:calendar:twoDigitStartDate:)](<date(format_locale_timezone_calendar_twodigitstartdate_).md>) — Creates a regex component that matches a localized date string formatted in accordance with a format string, capturing it as a Foundation date.
- [dateTime(date:time:locale:timeZone:calendar:)](<datetime(date_time_locale_timezone_calendar_).md>) — Creates a regex component that matches a localized date and time string, capturing it as a Foundation date.
- [iso8601](iso8601.md) — A regex component that matches a default ISO 8601-formatted date string, capturing it as a Foundation date.
- [iso8601Date(timeZone:dateSeparator:)](<iso8601date(timezone_dateseparator_).md>) — Creates a regex component that matches an ISO 8601-formatted date string, capturing it as a Foundation date in the specified time zone.
- [iso8601(timeZone:includingFractionalSeconds:dateSeparator:dateTimeSeparator:timeSeparator:)](<iso8601(timezone_includingfractionalseconds_dateseparator_datetimeseparator_timeseparator_).md>) — Creates a regex component that matches an ISO 8601-formatted date string, capturing the matched substring as a Foundation date in the specified time zone.
- [iso8601WithTimeZone(includingFractionalSeconds:dateSeparator:dateTimeSeparator:timeSeparator:timeZoneSeparator:)](<iso8601withtimezone(includingfractionalseconds_dateseparator_datetimeseparator_timeseparator_timezoneseparator_).md>) — Creates a regex component that matches an ISO 8601-formatted date string that includes a time zone component, capturing the matched substring as a Foundation date.
