---
title: unitsStyle
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/relativedatetimeformatter/unitsstyle-swift.property
source_url: 'https://developer.apple.com/documentation/foundation/relativedatetimeformatter/unitsstyle-swift.property'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/relativedatetimeformatter/unitsstyle-swift.property.json'
content_hash: 'sha256:b7a080454795f7f5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [RelativeDateTimeFormatter](../relativedatetimeformatter.md)

# unitsStyle

<sub>Instance Property</sub>

The style to use when formatting the quantity or the name of the unit, such as “1 day ago” or “one day ago”.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var unitsStyle: RelativeDateTimeFormatter.UnitsStyle { get set }
```

## Discussion

The default value is `full`.

## See Also

### Configuring Formatter Options

- [calendar](calendar.md) — The calendar to use for formatting values that don’t have an inherent calendar of their own.
- [locale](locale.md) — The locale to use when formatting the date.
- [dateTimeStyle](datetimestyle-swift.property.md) — The style to use when describing a relative date, for example “yesterday” or “1 day ago”.
- [DateTimeStyle](datetimestyle-swift.enum.md) — A type that represents the style to use when formatting relative dates, such as “1 week ago” or “last week”.
- [UnitsStyle](unitsstyle-swift.enum.md) — A type that represents the style to use when formatting the units of relative dates.
- [formattingContext](formattingcontext.md) — A description of where the formatted string will appear, allowing the formatter to capitalize the output appropriately.
