---
title: 'setLocalizedDateFormatFromTemplate(_:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/dateformatter/setlocalizeddateformatfromtemplate(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/dateformatter/setlocalizeddateformatfromtemplate(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/dateformatter/setlocalizeddateformatfromtemplate%28_%3A%29.json'
content_hash: 'sha256:75f17a2d382a4069'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [DateFormatter](../dateformatter.md)

# setLocalizedDateFormatFromTemplate(_:)

<sub>Instance Method</sub>

Sets the date format from a template using the specified locale for the receiver.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func setLocalizedDateFormatFromTemplate(_ dateFormatTemplate: String)
```

## Parameters

- `dateFormatTemplate` — A string containing date format patterns (such as “MM” or “h”). For full details, see [Date and Time Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/DatesAndTimes/DatesAndTimes.html#//apple_ref/doc/uid/10000039i).

## Discussion

See [Data Formatting Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/DataFormatting/DataFormatting.html#//apple_ref/doc/uid/10000029i) for a list of the conversion specifiers permitted in date format strings.

Calling this method is equivalent to, but not necessarily implemented as, setting the [dateFormat](dateformat.md) property to the result of calling the [+ dateFormatFromTemplate:options:locale:](<dateformat(fromtemplate_options_locale_).md>) method, passing no options and the [locale](locale.md) property value.

> [!important] Important
> You should call this method only after setting the [locale](locale.md) of the receiver.

## See Also

### Related Documentation

- [locale](locale.md) — The locale for the receiver.

### Managing Formats and Styles

- [dateStyle](datestyle.md) — The date style of the receiver.
- [timeStyle](timestyle.md) — The time style of the receiver.
- [dateFormat](dateformat.md) — The date format string used by the receiver.
- [+ dateFormatFromTemplate:options:locale:](<dateformat(fromtemplate_options_locale_).md>) — Returns a localized date format string representing the given date format components arranged appropriately for the specified locale.
- [formattingContext](formattingcontext.md) — The capitalization formatting context used when formatting a date.
