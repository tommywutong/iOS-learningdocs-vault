---
title: 'description(with:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/date/description(with:)'
source_url: 'https://developer.apple.com/documentation/foundation/date/description(with:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/date/description%28with%3A%29.json'
content_hash: 'sha256:5fb85b8f333909d3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Date](../date.md)

# description(with:)

<sub>Instance Method</sub>

Returns a string representation of the receiver using the given locale.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func description(with locale: Locale?) -> String
```

## Parameters

- `locale` — A `Locale`. If you pass `nil`, `Date` formats the date in the same way as the `description` property.

## Return Value

A string representation of the `Date`, using the given locale, or if the locale argument is `nil`, in the international format `YYYY-MM-DD HH:MM:SS ±HHMM`, where `±HHMM` represents the time zone offset in hours and minutes from UTC (for example, “`2001-03-24 10:45:32 +0600`”).

## See Also

### Describing Dates

- [description](description.md) — The representation is useful for debugging only. There are a number of options to acquire a formatted string for a date including: date formatters (see [NSDateFormatter](//apple_ref/occ/cl/NSDateFormatter) and [Data Formatting Guide](//apple_ref/doc/uid/10000029i)), and the `Date` function `description(locale:)`.
- [customPlaygroundQuickLook](customplaygroundquicklook.md) — A custom playground Quick Look for the date. _(deprecated)_
