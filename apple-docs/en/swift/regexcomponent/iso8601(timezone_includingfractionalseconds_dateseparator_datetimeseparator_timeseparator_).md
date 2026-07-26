---
title: 'iso8601(timeZone:includingFractionalSeconds:dateSeparator:dateTimeSeparator:timeSeparator:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/regexcomponent/iso8601(timezone:includingfractionalseconds:dateseparator:datetimeseparator:timeseparator:)'
source_url: 'https://developer.apple.com/documentation/swift/regexcomponent/iso8601(timezone:includingfractionalseconds:dateseparator:datetimeseparator:timeseparator:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/regexcomponent/iso8601%28timezone%3Aincludingfractionalseconds%3Adateseparator%3Adatetimeseparator%3Atimeseparator%3A%29.json'
content_hash: 'sha256:f74c4ce9672edd8f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [RegexComponent](../regexcomponent.md)

# iso8601(timeZone:includingFractionalSeconds:dateSeparator:dateTimeSeparator:timeSeparator:)

<sub>Type Method</sub>

Creates a regex component that matches an ISO 8601-formatted date string, capturing the matched substring as a Foundation date in the specified time zone.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func iso8601(timeZone: TimeZone, includingFractionalSeconds: Bool = false, dateSeparator: Date.ISO8601FormatStyle.DateSeparator = .dash, dateTimeSeparator: Date.ISO8601FormatStyle.DateTimeSeparator = .standard, timeSeparator: Date.ISO8601FormatStyle.TimeSeparator = .colon) -> Self
```

## Parameters

- `timeZone` — The time zone to use when returning a captured [Date](../../foundation/date.md). The returned date’s time value is `00:00:00` in this time zone.

- `includingFractionalSeconds` — A Boolean value that specifies whether the source string contains fractional seconds. The default is `false`.

- `dateSeparator` — The character that separates year, month, and day sections of the date substring. The default is [Date.ISO8601FormatStyle.DateSeparator.dash](../../foundation/date/iso8601formatstyle/dateseparator-swift.enum/dash.md).

- `dateTimeSeparator` — The character that separates the date and time sections of the substring. The default is [Date.ISO8601FormatStyle.DateTimeSeparator.standard](../../foundation/date/iso8601formatstyle/datetimeseparator-swift.enum/standard.md).

- `timeSeparator` — The character that separates the date and time sections of the substring. The default is [Date.ISO8601FormatStyle.TimeSeparator.colon](../../foundation/date/iso8601formatstyle/timeseparator-swift.enum/colon.md).

## Return Value

A `RegexComponent` that matches ISO 8601-formatted date substrings as Foundation [Date](../../foundation/date.md) instances.

## Discussion

This method matches an ISO 8601 date string using the provided separator characters. It doesn’t look for a time zone in the source string, and the match doesn’t include time zone characters if they’re present. Instead, the matcher interprets the string as being in the provided `timeZone`.

The following example creates a [Regex](../regex.md) that matches an ISO 8601-formatted date. The format looks for a dash for the date separator, the standard date/time separator (none), and a colon for the time separator. It also interprets the source string as being in the current time zone. The example then matches this regex against a source string containing a date with this format, some whitespace, a substring, more whitespace, and a currency value.

```swift
let iso860Source = "2022-07-14T21:10:15   Lemon-lime slushie      $1.99"
let matcher = Regex {
    Capture {
        One(.iso8601(timeZone: .current,
                     includingFractionalSeconds: false,
                     dateSeparator: .dash,
                     dateTimeSeparator: .standard,
                     timeSeparator: .colon))
    }
    OneOrMore(.horizontalWhitespace)
    OneOrMore(.any)
    OneOrMore(.horizontalWhitespace)
    One(.localizedCurrency(code:Locale.Currency("USD"),
                               locale:Locale(identifier: "en_US")))
}
let match = iso860Source.firstMatch(of: matcher)
let date = match?.1 // date == Jul 14, 2022 at 9:10 PM (may vary depending on current locale)
```

## See Also

### Matching dates and times

- [date(_:locale:timeZone:calendar:)](<date(__locale_timezone_calendar_).md>) — Creates a regex component that matches a localized date string formatted in accordance with a style, capturing it as a Foundation date.
- [date(format:locale:timeZone:calendar:twoDigitStartDate:)](<date(format_locale_timezone_calendar_twodigitstartdate_).md>) — Creates a regex component that matches a localized date string formatted in accordance with a format string, capturing it as a Foundation date.
- [dateTime(date:time:locale:timeZone:calendar:)](<datetime(date_time_locale_timezone_calendar_).md>) — Creates a regex component that matches a localized date and time string, capturing it as a Foundation date.
- [iso8601](iso8601.md) — A regex component that matches a default ISO 8601-formatted date string, capturing it as a Foundation date.
- [iso8601Date(timeZone:dateSeparator:)](<iso8601date(timezone_dateseparator_).md>) — Creates a regex component that matches an ISO 8601-formatted date string, capturing it as a Foundation date in the specified time zone.
- [iso8601WithTimeZone(includingFractionalSeconds:dateSeparator:dateTimeSeparator:timeSeparator:timeZoneSeparator:)](<iso8601withtimezone(includingfractionalseconds_dateseparator_datetimeseparator_timeseparator_timezoneseparator_).md>) — Creates a regex component that matches an ISO 8601-formatted date string that includes a time zone component, capturing the matched substring as a Foundation date.
