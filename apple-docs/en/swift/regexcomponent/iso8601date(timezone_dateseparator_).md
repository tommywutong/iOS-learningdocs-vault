---
title: 'iso8601Date(timeZone:dateSeparator:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/regexcomponent/iso8601date(timezone:dateseparator:)'
source_url: 'https://developer.apple.com/documentation/swift/regexcomponent/iso8601date(timezone:dateseparator:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/regexcomponent/iso8601date%28timezone%3Adateseparator%3A%29.json'
content_hash: 'sha256:54b82c0511776721'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [RegexComponent](../regexcomponent.md)

# iso8601Date(timeZone:dateSeparator:)

<sub>Type Method</sub>

Creates a regex component that matches an ISO 8601-formatted date string, capturing it as a Foundation date in the specified time zone.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func iso8601Date(timeZone: TimeZone, dateSeparator: Date.ISO8601FormatStyle.DateSeparator = .dash) -> Self
```

## Parameters

- `timeZone` — The time zone to use when returning a captured [Date](../../foundation/date.md). The returned date’s time value is `00:00:00` in this time zone.

- `dateSeparator` — The character that separates year, month, and day sections of the date substring.

## Return Value

A `RegexComponent` that matches ISO 8601-formatted date substrings as Foundation [Date](../../foundation/date.md) instances.

## Discussion

This method matches an ISO 8601 date string using the provided date separator. This method only matches a date substring. If the source string also contains a time, this method doesn’t match it. To match both date and time in an ISO 8601-formatted string, use [iso8601(timeZone:includingFractionalSeconds:dateSeparator:dateTimeSeparator:timeSeparator:)](<iso8601(timezone_includingfractionalseconds_dateseparator_datetimeseparator_timeseparator_).md>).

The returned date’s time is midnight in the provided time zone.

The following example creates a [Regex](../regex.md) that matches a date formatted with the base ISO 8601 format and dashes for date separators. It then matches this regex against a source string containing a date with this format, some whitespace, a substring, more whitespace, and a currency value.

```swift
let iso860Source = "2022-07-14   Lemon-lime slushie      $1.99"
let matcher = Regex {
    Capture {
        One(.iso8601Date(timeZone: TimeZone(identifier: "PST")!,
                         dateSeparator: .dash))
    }
    OneOrMore(.horizontalWhitespace)
    OneOrMore(.any)
    OneOrMore(.horizontalWhitespace)
    One(.localizedCurrency(code:Locale.Currency("USD"),
                           locale:Locale(identifier: "en_US")))
}
let match = iso860Source.firstMatch(of: matcher)
let date = match?.1 // date == Jul 14, 2022 at 12:00 AM PST
```

## See Also

### Matching dates and times

- [date(_:locale:timeZone:calendar:)](<date(__locale_timezone_calendar_).md>) — Creates a regex component that matches a localized date string formatted in accordance with a style, capturing it as a Foundation date.
- [date(format:locale:timeZone:calendar:twoDigitStartDate:)](<date(format_locale_timezone_calendar_twodigitstartdate_).md>) — Creates a regex component that matches a localized date string formatted in accordance with a format string, capturing it as a Foundation date.
- [dateTime(date:time:locale:timeZone:calendar:)](<datetime(date_time_locale_timezone_calendar_).md>) — Creates a regex component that matches a localized date and time string, capturing it as a Foundation date.
- [iso8601](iso8601.md) — A regex component that matches a default ISO 8601-formatted date string, capturing it as a Foundation date.
- [iso8601(timeZone:includingFractionalSeconds:dateSeparator:dateTimeSeparator:timeSeparator:)](<iso8601(timezone_includingfractionalseconds_dateseparator_datetimeseparator_timeseparator_).md>) — Creates a regex component that matches an ISO 8601-formatted date string, capturing the matched substring as a Foundation date in the specified time zone.
- [iso8601WithTimeZone(includingFractionalSeconds:dateSeparator:dateTimeSeparator:timeSeparator:timeZoneSeparator:)](<iso8601withtimezone(includingfractionalseconds_dateseparator_datetimeseparator_timeseparator_timezoneseparator_).md>) — Creates a regex component that matches an ISO 8601-formatted date string that includes a time zone component, capturing the matched substring as a Foundation date.
