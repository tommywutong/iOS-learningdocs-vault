---
title: 'init(anchor:presentation:unitsStyle:locale:calendar:capitalizationContext:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 1.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/date/anchoredrelativeformatstyle/init(anchor:presentation:unitsstyle:locale:calendar:capitalizationcontext:)'
source_url: 'https://developer.apple.com/documentation/foundation/date/anchoredrelativeformatstyle/init(anchor:presentation:unitsstyle:locale:calendar:capitalizationcontext:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/date/anchoredrelativeformatstyle/init%28anchor%3Apresentation%3Aunitsstyle%3Alocale%3Acalendar%3Acapitalizationcontext%3A%29.json'
content_hash: 'sha256:5a14411d5d36b06e'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [Date](../../date.md) · [AnchoredRelativeFormatStyle](../anchoredrelativeformatstyle.md)

# init(anchor:presentation:unitsStyle:locale:calendar:capitalizationContext:)

<sub>Initializer</sub>

Create a relative format style that is detached from the system time, and instead formats an anchor date relative to the format input.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(anchor: Date, presentation: Date.AnchoredRelativeFormatStyle.Presentation = .numeric, unitsStyle: Date.AnchoredRelativeFormatStyle.UnitsStyle = .wide, locale: Locale = .autoupdatingCurrent, calendar: Calendar = .autoupdatingCurrent, capitalizationContext: FormatStyleCapitalizationContext = .unknown)
```

## Parameters

- `anchor` — The date the formatted output is referring to.
