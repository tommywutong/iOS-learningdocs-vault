---
title: dateFormat
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/dateformatter/dateformat
source_url: 'https://developer.apple.com/documentation/foundation/dateformatter/dateformat'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/dateformatter/dateformat.json'
content_hash: 'sha256:b72f201d06dd3e8b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [DateFormatter](../dateformatter.md)

# dateFormat

<sub>Instance Property</sub>

The date format string used by the receiver.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var dateFormat: String! { get set }
```

## Discussion

See [Data Formatting Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/DataFormatting/DataFormatting.html#//apple_ref/doc/uid/10000029i) for a list of the conversion specifiers permitted in date format strings.

You should only set this property when working with fixed format representations, as discussed in [Working With Fixed Format Date Representations](../dateformatter.md#Working-With-Fixed-Format-Date-Representations). For user-visible representations, you should use the [dateStyle](datestyle.md) and [timeStyle](timestyle.md) properties, or the [- setLocalizedDateFormatFromTemplate:](<setlocalizeddateformatfromtemplate(__).md>) method if your desired format cannot be achieved using the predefined styles; both of these properties and this method provide a localized date representation appropriate for display to the user.

## See Also

### Managing Formats and Styles

- [dateStyle](datestyle.md) — The date style of the receiver.
- [timeStyle](timestyle.md) — The time style of the receiver.
- [- setLocalizedDateFormatFromTemplate:](<setlocalizeddateformatfromtemplate(__).md>) — Sets the date format from a template using the specified locale for the receiver.
- [+ dateFormatFromTemplate:options:locale:](<dateformat(fromtemplate_options_locale_).md>) — Returns a localized date format string representing the given date format components arranged appropriately for the specified locale.
- [formattingContext](formattingcontext.md) — The capitalization formatting context used when formatting a date.
