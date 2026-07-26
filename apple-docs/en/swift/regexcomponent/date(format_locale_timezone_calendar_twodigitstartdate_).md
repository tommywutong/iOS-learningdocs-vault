---
title: 'date(format:locale:timeZone:calendar:twoDigitStartDate:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/regexcomponent/date(format:locale:timezone:calendar:twodigitstartdate:)'
source_url: 'https://developer.apple.com/documentation/swift/regexcomponent/date(format:locale:timezone:calendar:twodigitstartdate:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/regexcomponent/date%28format%3Alocale%3Atimezone%3Acalendar%3Atwodigitstartdate%3A%29.json'
content_hash: 'sha256:f73514be7916a954'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [RegexComponent](../regexcomponent.md)

# date(format:locale:timeZone:calendar:twoDigitStartDate:)

<sub>Type Method</sub>

Creates a regex component that matches a localized date string formatted in accordance with a format string, capturing it as a Foundation date.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func date(format: Date.FormatString, locale: Locale, timeZone: TimeZone, calendar: Calendar? = nil, twoDigitStartDate: Date = Date(timeIntervalSince1970: 0)) -> Self
```

## Parameters

- `format` — A [Date.FormatString](../../foundation/date/formatstring.md) to use when matching date substrings.

- `locale` — The locale to use when matching date substrings. Matching uses this locale to evaluate the order of date components. It also uses the locale’s language for date format styles that use words.

- `timeZone` — The time zone to use when returning a captured [Date](../../foundation/date.md). The returned date’s time value is `00:00:00` in this time zone.

- `calendar` — The calendar to use when matching date substrings. If `nil`, matching uses the default calendar of the specified `locale`.

- `twoDigitStartDate` — The earliest date a matched two-year date can represent. For example, with the default value of `Date(timeIntervalSince1970: 0)`, the matcher treats `22` as 2022, and `84` as 1984. The matcher ignores this parameter for date substrings that contain year components with more than two digits.

## Return Value

A `RegexComponent` that matches date substrings as Foundation [Date](../../foundation/date.md) instances.

## Discussion

This method matches date substrings in accordance with a format from a [Date.FormatString](../../foundation/date/formatstring.md).

If a time value follows the date substring, the matcher ignores it, treating it as any other character sequence. To match date and time substrings, use [dateTime(date:time:locale:timeZone:calendar:)](<datetime(date_time_locale_timezone_calendar_).md>).

If the date substring uses a two-digit year, the matcher uses the `twoDigitStartDate` parameter, which defines the earliest date a string with a two-digit year can denote. The matcher ignores this parameter if the year contains more than two digits.

The following example creates a [Regex](../regex.md) that matches a date formatted with two-digit month, day, and year fields, and slash (`/`) separator characters. It sets midnight on January 1, 1970, as the `twoDigitStartDate`, and `PST` as the time zone. It then matches this regex against a source string containing a date with this format and a two-digit year, some whitespace, a substring, more whitespace, and a currency value. Because the source year `76` is after `thetwoDigitStartDate`, the date substring matches as `1976`.

```swift
let enUSLocale = Locale(languageCode: .english, languageRegion: .unitedStates)
let source = "4/1/76  Lemon-lime slushie      $0.40"
let matcher = Regex {
    Capture {
        One(.date(format: "\(month: .twoDigits)/\(day: .twoDigits)/\(year: .twoDigits)",
                  locale: enUSLocale,
                  timeZone: TimeZone(identifier: "PST")!,
                  twoDigitStartDate: try! Date("1970-01-01T00:00:00-0800", strategy: .iso8601)))
    }
    OneOrMore(.horizontalWhitespace)
    OneOrMore(.any)
    OneOrMore(.horizontalWhitespace)
    One(.localizedCurrency(code: Locale.Currency("USD"),
                           locale: enUSLocale))
}

let match = source.firstMatch(of: matcher)
let date = match?.1 // date == Mar 1, 1976 at 12:00 AM (may vary based on current locale)
```

## See Also

### Matching dates and times

- [date(_:locale:timeZone:calendar:)](<date(__locale_timezone_calendar_).md>) — Creates a regex component that matches a localized date string formatted in accordance with a style, capturing it as a Foundation date.
- [dateTime(date:time:locale:timeZone:calendar:)](<datetime(date_time_locale_timezone_calendar_).md>) — Creates a regex component that matches a localized date and time string, capturing it as a Foundation date.
- [iso8601](iso8601.md) — A regex component that matches a default ISO 8601-formatted date string, capturing it as a Foundation date.
- [iso8601Date(timeZone:dateSeparator:)](<iso8601date(timezone_dateseparator_).md>) — Creates a regex component that matches an ISO 8601-formatted date string, capturing it as a Foundation date in the specified time zone.
- [iso8601(timeZone:includingFractionalSeconds:dateSeparator:dateTimeSeparator:timeSeparator:)](<iso8601(timezone_includingfractionalseconds_dateseparator_datetimeseparator_timeseparator_).md>) — Creates a regex component that matches an ISO 8601-formatted date string, capturing the matched substring as a Foundation date in the specified time zone.
- [iso8601WithTimeZone(includingFractionalSeconds:dateSeparator:dateTimeSeparator:timeSeparator:timeZoneSeparator:)](<iso8601withtimezone(includingfractionalseconds_dateseparator_datetimeseparator_timeseparator_timezoneseparator_).md>) — Creates a regex component that matches an ISO 8601-formatted date string that includes a time zone component, capturing the matched substring as a Foundation date.
