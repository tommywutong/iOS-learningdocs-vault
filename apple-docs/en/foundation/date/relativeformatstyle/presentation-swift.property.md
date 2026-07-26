---
title: presentation
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/date/relativeformatstyle/presentation-swift.property
source_url: 'https://developer.apple.com/documentation/foundation/date/relativeformatstyle/presentation-swift.property'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/date/relativeformatstyle/presentation-swift.property.json'
content_hash: 'sha256:bb703dff5927ca07'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [Date](../../date.md) · [RelativeFormatStyle](../relativeformatstyle.md)

# presentation

<sub>Instance Property</sub>

Specifies the style to use when describing a relative date, such as “1 day ago” or “yesterday”.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var presentation: Date.RelativeFormatStyle.Presentation
```

## Discussion

Express relative date formats in either `numeric` or `named` styles. For example:

```swift
if let past = Calendar.current.date(byAdding: .day, value: -7, to: Date()) {
    var formatStyle = Date.RelativeFormatStyle()
    
    formatStyle.presentation = .numeric
    past.formatted(formatStyle) // "1 week ago"
    
    formatStyle.presentation = .named
    past.formatted(formatStyle) // "last week"
}
```

## See Also

### Modifying a Relative Date Format Style

- [unitsStyle](unitsstyle-swift.property.md) — The style to use when formatting the quantity or the name of the unit, such as “1 day ago” or “one day ago”.
- [calendar](calendar.md) — The calendar to use when formatting relative dates.
- [capitalizationContext](capitalizationcontext.md) — The capitalization context to use when formatting the relative dates.
- [locale](locale.md) — The locale to use when formatting the relative date.
- [locale(_:)](<locale(__).md>) — Modifies the relative date format style to use the specified locale.
