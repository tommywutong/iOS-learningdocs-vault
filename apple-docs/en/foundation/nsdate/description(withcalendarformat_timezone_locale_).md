---
title: 'description(withCalendarFormat:timeZone:locale:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+（8.0 起废弃）, iPadOS 2.0+（8.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）, macOS 10.4+（10.10 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/foundation/nsdate/description(withcalendarformat:timezone:locale:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsdate/description(withcalendarformat:timezone:locale:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsdate/description%28withcalendarformat%3Atimezone%3Alocale%3A%29.json'
content_hash: 'sha256:1272d69e2a35549c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSDate](../nsdate.md)

# description(withCalendarFormat:timeZone:locale:)

<sub>Instance Method</sub>

Returns a string representation of the date formatted as specified by given conversion specifiers.

<sub>Mac Catalyst, macOS</sub>

```swift
func description(withCalendarFormat format: String?, timeZone aTimeZone: TimeZone?, locale: Any?) -> String?
```

## Parameters

- `format` — The format for the returned string (see Date and Number Formatters in OS X v10.0 to 10.3 for a discussion of how to create the format string). Pass `nil` to use the default format string, “`%Y-%m-%d %H:%M:%S %z`” (this conforms to the international format `YYYY-MM-DD HH:MM:SS ±HHMM`.)

- `aTimeZone` — The time zone in which to represent the receiver. Pass `nil` to use the default time zone—specific to the current locale.

- `locale` — An `NSDictionary` object containing locale data. To use the user’s preferences, you can use `[[NSUserDefaults standardUserDefaults] dictionaryRepresentation]`. If you pass `nil` or an instance of `NSLocale`, `NSDate` uses the system default locale—this is not the same as the current user’s locale.

## Return Value

A string representation of the receiver, formatted as specified by the given conversion specifiers.

## Discussion

There are several problems with the implementation of this method that cannot be fixed for compatibility reasons. To format a date, you should use a date formatter object instead (see [DateFormatter](../dateformatter.md) and [Data Formatting Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/DataFormatting/DataFormatting.html#//apple_ref/doc/uid/10000029i)).

You could use this method to print the current time as follows:

```objc
sprintf(aString, "The current time is %s\n", [[[NSDate  date]
    descriptionWithCalendarFormat:@"%H:%M:%S %Z" timeZone:nil
    locale:[[NSUserDefaults standardUserDefaults] dictionaryRepresentation]]
        UTF8String]);
```

## See Also

### Related Documentation

- [- descriptionWithLocale:](<description(with_).md>) — Returns a string representation of the date using the given locale.

### Legacy Operations

- [+ dateWithNaturalLanguageString:](<date(withnaturallanguagestring_).md>) — Creates and returns a date object set to the date and time specified by a given string. _(deprecated)_
- [+ dateWithNaturalLanguageString:locale:](<date(withnaturallanguagestring_locale_).md>) — Creates and returns a date object set to the date and time specified by a given string. _(deprecated)_
- [+ dateWithString:](<date(with_).md>) — Creates and returns a date object with a date and time value specified by a given string in the international string representation format (`YYYY-MM-DD HH:MM:SS ±HHMM`). _(deprecated)_
- [- initWithString:](<init(string_).md>) — Returns a date object initialized with a date and time value specified by a given string in the international string representation format. _(deprecated)_
- [- addTimeInterval:](<addtimeinterval(__).md>) — Returns a new date object that is set to a given number of seconds relative to the receiver. _(deprecated)_
- [- dateWithCalendarFormat:timeZone:](<date(withcalendarformat_timezone_).md>) — Converts the receiver to a calendar date with a given format string and time zone. _(deprecated)_
