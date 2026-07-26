---
title: 'init(format:locale:timeZone:calendar:isLenient:twoDigitStartDate:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/date/parsestrategy/init(format:locale:timezone:calendar:islenient:twodigitstartdate:)'
source_url: 'https://developer.apple.com/documentation/foundation/date/parsestrategy/init(format:locale:timezone:calendar:islenient:twodigitstartdate:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/date/parsestrategy/init%28format%3Alocale%3Atimezone%3Acalendar%3Aislenient%3Atwodigitstartdate%3A%29.json'
content_hash: 'sha256:c52d8b765cdddd33'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [Date](../../date.md) · [ParseStrategy](../parsestrategy.md)

# init(format:locale:timeZone:calendar:isLenient:twoDigitStartDate:)

<sub>Initializer</sub>

Creates a new `ParseStrategy` with the given configurations.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(format: Date.FormatString, locale: Locale? = nil, timeZone: TimeZone, calendar: Calendar = Calendar(identifier: .gregorian), isLenient: Bool = true, twoDigitStartDate: Date = Date(timeIntervalSince1970: 0))
```

## Parameters

- `format` — A fixed format representing the pattern of the date string.

- `locale` — The locale of the fixed format.

- `timeZone` — The time zone to use for creating the date.

- `isLenient` — Whether to use heuristics when parsing the representation.

- `twoDigitStartDate` — The earliest date that can be denoted by a two-digit year specifier.
