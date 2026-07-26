---
title: formattingContext
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/dateformatter/formattingcontext
source_url: 'https://developer.apple.com/documentation/foundation/dateformatter/formattingcontext'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/dateformatter/formattingcontext.json'
content_hash: 'sha256:892e9617d1951b22'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [DateFormatter](../dateformatter.md)

# formattingContext

<sub>Instance Property</sub>

The capitalization formatting context used when formatting a date.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var formattingContext: Formatter.Context { get set }
```

## Discussion

The formatting context allows the formatter to apply appropriate capitalization depending on how the how the string will be used, and whether the locale makes capitalization distinctions.

## See Also

### Managing Formats and Styles

- [dateStyle](datestyle.md) — The date style of the receiver.
- [timeStyle](timestyle.md) — The time style of the receiver.
- [dateFormat](dateformat.md) — The date format string used by the receiver.
- [- setLocalizedDateFormatFromTemplate:](<setlocalizeddateformatfromtemplate(__).md>) — Sets the date format from a template using the specified locale for the receiver.
- [+ dateFormatFromTemplate:options:locale:](<dateformat(fromtemplate_options_locale_).md>) — Returns a localized date format string representing the given date format components arranged appropriately for the specified locale.
