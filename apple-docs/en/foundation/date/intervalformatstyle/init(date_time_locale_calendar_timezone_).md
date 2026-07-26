---
title: 'init(date:time:locale:calendar:timeZone:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/date/intervalformatstyle/init(date:time:locale:calendar:timezone:)'
source_url: 'https://developer.apple.com/documentation/foundation/date/intervalformatstyle/init(date:time:locale:calendar:timezone:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/date/intervalformatstyle/init%28date%3Atime%3Alocale%3Acalendar%3Atimezone%3A%29.json'
content_hash: 'sha256:1149a5369f0b5e91'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [Date](../../date.md) · [IntervalFormatStyle](../intervalformatstyle.md)

# init(date:time:locale:calendar:timeZone:)

<sub>Initializer</sub>

Creates an instance using the provided date, time, locale, calendar, time zone, and capitalization context.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(date: Date.IntervalFormatStyle.DateStyle? = nil, time: Date.IntervalFormatStyle.TimeStyle? = nil, locale: Locale = .autoupdatingCurrent, calendar: Calendar = .autoupdatingCurrent, timeZone: TimeZone = .autoupdatingCurrent)
```

## Parameters

- `date` — The [DateStyle](../formatstyle/datestyle.md) for creating the string representation of the date interval.

- `time` — The [TimeStyle](../formatstyle/timestyle.md) for creating the string representation of the date interval.

- `locale` — The [Locale](../../locale.md) for creating the string representation of the date interval.

- `calendar` — The [Calendar](../../calendar.md) for creating the string representation of the date interval.

- `timeZone` — The [TimeZone](../../timezone.md) for creating the string representation of the date interval.

## Discussion

Customize the date interval string by providing a date style, time style, locale, calendar, time zone, and capitalization scheme.

Values for date style are [complete](../formatstyle/datestyle/complete.md), [long](../formatstyle/datestyle/long.md), [abbreviated](../formatstyle/datestyle/abbreviated.md), [numeric](../formatstyle/datestyle/numeric.md), [omitted](../formatstyle/datestyle/omitted.md), or `none`. Time style values are [complete](../formatstyle/timestyle/complete.md), [standard](../formatstyle/timestyle/standard.md), [shortened](../formatstyle/timestyle/shortened.md), [omitted](../formatstyle/timestyle/omitted.md), or `none`.
