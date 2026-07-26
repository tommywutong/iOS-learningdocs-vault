---
title: 'dateTime(date:time:locale:timeZone:calendar:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/regexcomponent/datetime(date:time:locale:timezone:calendar:)'
source_url: 'https://developer.apple.com/documentation/swift/regexcomponent/datetime(date:time:locale:timezone:calendar:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/regexcomponent/datetime%28date%3Atime%3Alocale%3Atimezone%3Acalendar%3A%29.json'
content_hash: 'sha256:146a810883b71baf'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [RegexComponent](../regexcomponent.md)

# dateTime(date:time:locale:timeZone:calendar:)

<sub>Type Method</sub>

Creates a regex component that matches a localized date and time string, capturing it as a Foundation date.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func dateTime(date: Date.FormatStyle.DateStyle, time: Date.FormatStyle.TimeStyle, locale: Locale, timeZone: TimeZone, calendar: Calendar? = nil) -> Date.ParseStrategy
```

## Parameters

- `date` — A [Date.FormatStyle.DateStyle](../../foundation/date/formatstyle/datestyle.md) to use when matching date substrings. Pass [omitted](../../foundation/date/formatstyle/datestyle/omitted.md) to match a time-only substring.

- `time` — A [Date.FormatStyle.TimeStyle](../../foundation/date/formatstyle/timestyle.md) to use when matching time substrings. Pass [omitted](../../foundation/date/formatstyle/timestyle/omitted.md) to match a date-only substring.

- `locale` — The locale to use when matching date substrings. Matching uses this locale to evaluate the order of date components. It also uses the locale’s language for date format styles that use words.

- `timeZone` — The time zone to use when capturing the date and time values. The regex component ignores this parameter if the source string contains a time zone substring that the format style supports.

- `calendar` — The calendar to use when matching date substrings. If `nil`, matching uses the default calendar of the specified `locale`.

## Return Value

A `RegexComponent` that matches date substrings as Foundation [Date](../../foundation/date.md) instances.

## Discussion

This method matches date substrings in accordance with the formatting of Foundation’s [Date.FormatStyle](../../foundation/date/formatstyle.md). If your source contains only a date or a time, use the `.omitted` value for the `date` or `time` style parameter to ignore the missing part.

The following example creates a [Regex](../regex.md) that matches a date and time formatted with the [numeric](../../foundation/date/formatstyle/datestyle/numeric.md) style in the `en_US` locale. It then matches this regex against a source string containing a date with this format, some whitespace, a substring, more whitespace, and a currency value.

```swift
let enUSLocale = Locale(languageCode: .english, languageRegion: .unitedStates)
let source = "7/31/2022, 5:15:12 PM  Lemon-lime slushie      $1.99"
let matcher = Regex {
    Capture {
        One(.dateTime(date: .numeric,
                      time: .standard,
                      locale: enUSLocale,
                      timeZone: TimeZone(identifier: "PST")!))
    }
    OneOrMore(.horizontalWhitespace)
    OneOrMore(.any)
    OneOrMore(.horizontalWhitespace)
    One(.localizedCurrency(code: Locale.Currency("USD"),
                           locale: enUSLocale))
}

guard let match = source.firstMatch(of: matcher) else { return }
let date = match.1 // date == Jul 31, 2022 at 5:15 PM PST
```

## See Also

### Matching dates and times

- [date(_:locale:timeZone:calendar:)](<date(__locale_timezone_calendar_).md>) — Creates a regex component that matches a localized date string formatted in accordance with a style, capturing it as a Foundation date.
- [date(format:locale:timeZone:calendar:twoDigitStartDate:)](<date(format_locale_timezone_calendar_twodigitstartdate_).md>) — Creates a regex component that matches a localized date string formatted in accordance with a format string, capturing it as a Foundation date.
- [iso8601](iso8601.md) — A regex component that matches a default ISO 8601-formatted date string, capturing it as a Foundation date.
- [iso8601Date(timeZone:dateSeparator:)](<iso8601date(timezone_dateseparator_).md>) — Creates a regex component that matches an ISO 8601-formatted date string, capturing it as a Foundation date in the specified time zone.
- [iso8601(timeZone:includingFractionalSeconds:dateSeparator:dateTimeSeparator:timeSeparator:)](<iso8601(timezone_includingfractionalseconds_dateseparator_datetimeseparator_timeseparator_).md>) — Creates a regex component that matches an ISO 8601-formatted date string, capturing the matched substring as a Foundation date in the specified time zone.
- [iso8601WithTimeZone(includingFractionalSeconds:dateSeparator:dateTimeSeparator:timeSeparator:timeZoneSeparator:)](<iso8601withtimezone(includingfractionalseconds_dateseparator_datetimeseparator_timeseparator_timezoneseparator_).md>) — Creates a regex component that matches an ISO 8601-formatted date string that includes a time zone component, capturing the matched substring as a Foundation date.
