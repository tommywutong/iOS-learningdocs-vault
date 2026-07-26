---
title: 'date(with:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 2.0+（8.0 起废弃）, iPadOS 2.0+（8.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）, macOS 10.4+（10.10 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/foundation/nsdate/date(with:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsdate/date(with:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsdate/date%28with%3A%29.json'
content_hash: 'sha256:29462d5e1f13cf85'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSDate](../nsdate.md)

# date(with:)

<sub>Type Method</sub>

Creates and returns a date object with a date and time value specified by a given string in the international string representation format (`YYYY-MM-DD HH:MM:SS ±HHMM`).

> [!warning] Deprecated
> Use NSDateFormatter instead

<sub>Mac Catalyst, macOS</sub>

```swift
class func date(with aString: String) -> Any
```

## Parameters

- `aString` — A string that specifies a date and time value in the international string representation format—`YYYY-MM-DD HH:MM:SS ±HHMM`, where `±HHMM` is a time zone offset in hours and minutes from UTC (for example, “`2001-03-24 10:45:32 +0600`”). You must specify all fields of the format string, including the time zone offset, which must have a plus or minus sign prefix.

## Return Value

An `NSDate` object with a date and time value specified by `aString`.

## Discussion

To create a date object from a string, you should typically use a date formatter object instead (see [DateFormatter](../dateformatter.md) and [Data Formatting Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/DataFormatting/DataFormatting.html#//apple_ref/doc/uid/10000029i)).

## See Also

### Legacy Operations

- [+ dateWithNaturalLanguageString:](<date(withnaturallanguagestring_).md>) — Creates and returns a date object set to the date and time specified by a given string. _(deprecated)_
- [+ dateWithNaturalLanguageString:locale:](<date(withnaturallanguagestring_locale_).md>) — Creates and returns a date object set to the date and time specified by a given string. _(deprecated)_
- [- initWithString:](<init(string_).md>) — Returns a date object initialized with a date and time value specified by a given string in the international string representation format. _(deprecated)_
- [- addTimeInterval:](<addtimeinterval(__).md>) — Returns a new date object that is set to a given number of seconds relative to the receiver. _(deprecated)_
- [- dateWithCalendarFormat:timeZone:](<date(withcalendarformat_timezone_).md>) — Converts the receiver to a calendar date with a given format string and time zone. _(deprecated)_
- [- descriptionWithCalendarFormat:timeZone:locale:](<description(withcalendarformat_timezone_locale_).md>) — Returns a string representation of the date formatted as specified by given conversion specifiers. _(deprecated)_
