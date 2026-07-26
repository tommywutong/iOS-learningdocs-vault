---
title: unitsStyle
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/date/relativeformatstyle/unitsstyle-swift.property
source_url: 'https://developer.apple.com/documentation/foundation/date/relativeformatstyle/unitsstyle-swift.property'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/date/relativeformatstyle/unitsstyle-swift.property.json'
content_hash: 'sha256:57cd22e33a550f24'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [Date](../../date.md) · [RelativeFormatStyle](../relativeformatstyle.md)

# unitsStyle

<sub>Instance Property</sub>

The style to use when formatting the quantity or the name of the unit, such as “1 day ago” or “one day ago”.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var unitsStyle: Date.RelativeFormatStyle.UnitsStyle
```

## Discussion

Express relative date format units in either `wide`, `narrow`, `abbreviated`, or `spellOut` styles. For example:

```swift
if let past = Calendar.current.date(byAdding: .day, value: -14, to: Date()) {
    past.formatted(.relative(presentation: .named, unitsStyle: .wide)) // "2 weeks ago"
    past.formatted(.relative(presentation: .named, unitsStyle: .narrow)) // "2 wk. ago"
    past.formatted(.relative(presentation: .named, unitsStyle: .abbreviated)) // "2 wk. ago"
    past.formatted(.relative(presentation: .named, unitsStyle: .spellOut)) // "two weeks ago"
}
```

## See Also

### Modifying a Relative Date Format Style

- [presentation](presentation-swift.property.md) — Specifies the style to use when describing a relative date, such as “1 day ago” or “yesterday”.
- [calendar](calendar.md) — The calendar to use when formatting relative dates.
- [capitalizationContext](capitalizationcontext.md) — The capitalization context to use when formatting the relative dates.
- [locale](locale.md) — The locale to use when formatting the relative date.
- [locale(_:)](<locale(__).md>) — Modifies the relative date format style to use the specified locale.
