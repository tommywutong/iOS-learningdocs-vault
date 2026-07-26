---
title: description
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsdate/description
source_url: 'https://developer.apple.com/documentation/foundation/nsdate/description'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsdate/description.json'
content_hash: 'sha256:76ca952739a264e5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSDate](../nsdate.md)

# description

<sub>Instance Property</sub>

A string representation of the date object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var description: String { get }
```

## Discussion

The representation is useful for debugging only.

There are a number of options to acquire a formatted string for a date including: date formatters (see [DateFormatter](../dateformatter.md) and [Data Formatting Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/DataFormatting/DataFormatting.html#//apple_ref/doc/uid/10000029i)), and the `NSDate` methods [- descriptionWithLocale:](<description(with_).md>), [- dateWithCalendarFormat:timeZone:](<date(withcalendarformat_timezone_).md>), and [- descriptionWithCalendarFormat:timeZone:locale:](<description(withcalendarformat_timezone_locale_).md>)

## See Also

### Related Documentation

- [- descriptionWithCalendarFormat:timeZone:locale:](<description(withcalendarformat_timezone_locale_).md>) — Returns a string representation of the date formatted as specified by given conversion specifiers. _(deprecated)_
- [- dateWithCalendarFormat:timeZone:](<date(withcalendarformat_timezone_).md>) — Converts the receiver to a calendar date with a given format string and time zone. _(deprecated)_

### Describing Dates

- [- descriptionWithLocale:](<description(with_).md>) — Returns a string representation of the date using the given locale.
- [customPlaygroundQuickLook](customplaygroundquicklook.md) — A custom playground Quick Look for this object. _(deprecated)_
