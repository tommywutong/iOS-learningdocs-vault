---
title: 'init(presentation:unitsStyle:locale:calendar:capitalizationContext:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/date/relativeformatstyle/init(presentation:unitsstyle:locale:calendar:capitalizationcontext:)'
source_url: 'https://developer.apple.com/documentation/foundation/date/relativeformatstyle/init(presentation:unitsstyle:locale:calendar:capitalizationcontext:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/date/relativeformatstyle/init%28presentation%3Aunitsstyle%3Alocale%3Acalendar%3Acapitalizationcontext%3A%29.json'
content_hash: 'sha256:dcb8350869448d6e'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [Date](../../date.md) · [RelativeFormatStyle](../relativeformatstyle.md)

# init(presentation:unitsStyle:locale:calendar:capitalizationContext:)

<sub>Initializer</sub>

Creates a relative date format style with the specified presentation, units, locale, calendar, and capitalization context.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(presentation: Date.RelativeFormatStyle.Presentation = .numeric, unitsStyle: Date.RelativeFormatStyle.UnitsStyle = .wide, locale: Locale = .autoupdatingCurrent, calendar: Calendar = .autoupdatingCurrent, capitalizationContext: FormatStyleCapitalizationContext = .unknown)
```

## Parameters

- `presentation` — The style to use when describing a relative date, such as “1 day ago” or “yesterday”.

- `unitsStyle` — The style to use when formatting the quantity or the name of the unit, such as “1 day ago” or “one day ago”.

- `locale` — The locale to use when formatting the relative date.

- `calendar` — The calendar to use when formatting the relative date.

- `capitalizationContext` — The capitalization context to use when formatting the relative date.

## Discussion

The following example creates a format style applied to a relative date to create a string representation.

```swift
if let past = Calendar.current.date(byAdding: .day, value: -7, to: Date()) {

    let formatStyle = Date.RelativeFormatStyle(
        presentation: .named,
        unitsStyle: .abbreviated,
        locale: Locale(identifier: "en_US"),
        calendar: Calendar.current,
        capitalizationContext: .beginningOfSentence)
    
    print(past.formatted(formatStyle)) // "Last wk."
}
```
