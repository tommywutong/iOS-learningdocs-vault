---
title: 'init(style:locale:calendar:fields:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/date/componentsformatstyle/init(style:locale:calendar:fields:)'
source_url: 'https://developer.apple.com/documentation/foundation/date/componentsformatstyle/init(style:locale:calendar:fields:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/date/componentsformatstyle/init%28style%3Alocale%3Acalendar%3Afields%3A%29.json'
content_hash: 'sha256:415cfffaf6e1fe3f'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [Date](../../date.md) · [ComponentsFormatStyle](../componentsformatstyle.md)

# init(style:locale:calendar:fields:)

<sub>Initializer</sub>

Shows the date interval with the specified style and the specified date and time fields.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(style: Date.ComponentsFormatStyle.Style, locale: Locale = .autoupdatingCurrent, calendar: Calendar = .autoupdatingCurrent, fields: Set<Date.ComponentsFormatStyle.Field>? = nil)
```

## Parameters

- `style` — The style for the field names.

- `locale` — The locale for formatting the date interval. May affect the language in which the formatted fields are displayed and how the individual fields are connected.

- `calendar` — The calendar to interpret date values.

- `fields` — The fields to be included in the output string. Chosen automatically based on the interval being formatted if unspecified. Fields with 0 value are dropped.
