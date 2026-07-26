---
title: 'init(dateSeparator:dateTimeSeparator:timeZone:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/date/iso8601formatstyle/init(dateseparator:datetimeseparator:timezone:)'
source_url: 'https://developer.apple.com/documentation/foundation/date/iso8601formatstyle/init(dateseparator:datetimeseparator:timezone:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/date/iso8601formatstyle/init%28dateseparator%3Adatetimeseparator%3Atimezone%3A%29.json'
content_hash: 'sha256:7daf3a36f7d2056f'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [Date](../../date.md) · [ISO8601FormatStyle](../iso8601formatstyle.md)

# init(dateSeparator:dateTimeSeparator:timeZone:)

<sub>Initializer</sub>

Creates an instance using the provided date separator, date and time components separator, and time zone.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(dateSeparator: Date.ISO8601FormatStyle.DateSeparator = .dash, dateTimeSeparator: Date.ISO8601FormatStyle.DateTimeSeparator = .standard, timeZone: TimeZone = TimeZone(secondsFromGMT: 0)!)
```

## Parameters

- `dateSeparator` — The separator character used between the year, month, and day.

- `dateTimeSeparator` — The separator character used between the date and time components.

- `timeZone` — The [TimeZone](../../timezone.md) used to create the string representation of the date.

## Discussion

Possible values of `dateSeparator` are `dash` and `omitted`. Omitted is the default.

Possible values of `dateTimeSeparator` are `space` and `standard`. Standard is the default.

The following example shows the initizializer called with a variety of input parameters.

```swift
let aDate = Date()
print(aDate) // 2021-06-22 17:21:32 +0000
print(aDate.formatted(Date.ISO8601FormatStyle(dateSeparator: .omitted, dateTimeSeparator: .standard)))
// 20210622T172132Z

let cstDate = Date()
if let centralStandardTimeZone = TimeZone(identifier: "CST") {
   print(cstDate.formatted(Date.ISO8601FormatStyle(dateSeparator: .dash, dateTimeSeparator: .space, timeZone: centralStandardTimeZone)))
}
// 2021-06-22 122132-0500
```
