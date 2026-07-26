---
title: 'date(withNaturalLanguageString:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 2.0+（8.0 起废弃）, iPadOS 2.0+（8.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）, macOS 10.4+（10.10 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/foundation/nsdate/date(withnaturallanguagestring:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsdate/date(withnaturallanguagestring:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsdate/date%28withnaturallanguagestring%3A%29.json'
content_hash: 'sha256:b520a9f9663e5a12'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSDate](../nsdate.md)

# date(withNaturalLanguageString:)

<sub>Type Method</sub>

Creates and returns a date object set to the date and time specified by a given string.

> [!warning] Deprecated
> Create an NSDateFormatter with `init` and set the dateFormat property instead.

<sub>Mac Catalyst, macOS</sub>

```swift
class func date(withNaturalLanguageString string: String) -> Any?
```

## Parameters

- `string` — A string that contains a colloquial specification of a date, such as “last Tuesday at dinner,” “3pm December 31, 2001,” “12/31/01,” or “31/12/01.”

## Return Value

A new `NSDate` object set to the current date and time specified by `string`.

## Discussion

This method supports only a limited set of colloquial phrases, primarily in English. It may give unexpected results, and its use is strongly discouraged. To create a date object from a string, you should use a date formatter object instead (see [DateFormatter](../dateformatter.md) and [Data Formatting Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/DataFormatting/DataFormatting.html#//apple_ref/doc/uid/10000029i)).

In parsing the string, this method uses the date and time preferences stored in the user’s defaults database. (See [+ dateWithNaturalLanguageString:locale:](<date(withnaturallanguagestring_locale_).md>) for a list of the specific items used.)

## See Also

### Legacy Operations

- [+ dateWithNaturalLanguageString:locale:](<date(withnaturallanguagestring_locale_).md>) — Creates and returns a date object set to the date and time specified by a given string. _(deprecated)_
- [+ dateWithString:](<date(with_).md>) — Creates and returns a date object with a date and time value specified by a given string in the international string representation format (`YYYY-MM-DD HH:MM:SS ±HHMM`). _(deprecated)_
- [- initWithString:](<init(string_).md>) — Returns a date object initialized with a date and time value specified by a given string in the international string representation format. _(deprecated)_
- [- addTimeInterval:](<addtimeinterval(__).md>) — Returns a new date object that is set to a given number of seconds relative to the receiver. _(deprecated)_
- [- dateWithCalendarFormat:timeZone:](<date(withcalendarformat_timezone_).md>) — Converts the receiver to a calendar date with a given format string and time zone. _(deprecated)_
- [- descriptionWithCalendarFormat:timeZone:locale:](<description(withcalendarformat_timezone_locale_).md>) — Returns a string representation of the date formatted as specified by given conversion specifiers. _(deprecated)_
