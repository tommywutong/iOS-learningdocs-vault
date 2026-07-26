---
title: 'init(date:time:locale:calendar:timeZone:capitalizationContext:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/date/formatstyle/init(date:time:locale:calendar:timezone:capitalizationcontext:)'
source_url: 'https://developer.apple.com/documentation/foundation/date/formatstyle/init(date:time:locale:calendar:timezone:capitalizationcontext:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/date/formatstyle/init%28date%3Atime%3Alocale%3Acalendar%3Atimezone%3Acapitalizationcontext%3A%29.json'
content_hash: 'sha256:82e9b4e3a2437703'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [Date](../../date.md) · [FormatStyle](../formatstyle.md)

# init(date:time:locale:calendar:timeZone:capitalizationContext:)

<sub>Initializer</sub>

Creates an instance using the provided date, time, locale, calendar, time zone, and capitalization context.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(date: Date.FormatStyle.DateStyle? = nil, time: Date.FormatStyle.TimeStyle? = nil, locale: Locale = .autoupdatingCurrent, calendar: Calendar = .autoupdatingCurrent, timeZone: TimeZone = .autoupdatingCurrent, capitalizationContext: FormatStyleCapitalizationContext = .unknown)
```

## Parameters

- `date` — The [DateStyle](datestyle.md) used to create the string representation of the date.

- `time` — The [TimeStyle](timestyle.md) used to create the string representation of the date.

- `locale` — The [Locale](../../locale.md) used to create the string representation of the date.

- `calendar` — The [Calendar](../../calendar.md) used to create the string representation of the date.

- `timeZone` — The [TimeZone](../../timezone.md) used to create the string representation of the date.

- `capitalizationContext` — The [FormatStyleCapitalizationContext](../../formatstylecapitalizationcontext.md) used to create the string representation of the date.

## Discussion

Customize the date string by providing a date style, time style, locale, calendar, time zone, and capitalization scheme.

Date style values are [complete](datestyle/complete.md), [long](datestyle/long.md), `abbreviated`, [numeric](datestyle/numeric.md), [omitted](datestyle/omitted.md), or `none`. Time style values are [complete](timestyle/complete.md), [standard](timestyle/standard.md), [shortened](timestyle/shortened.md), [omitted](timestyle/omitted.md), or `none`.
