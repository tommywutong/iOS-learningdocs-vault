---
title: 'addTimeInterval(_:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+（4.0 起废弃）, iPadOS 2.0+（4.0 起废弃）, tvOS 9.0+（9.0 起废弃）, visionOS 1.0+（1.0 起废弃）, watchOS 2.0+（2.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/foundation/nsdate/addtimeinterval(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsdate/addtimeinterval(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsdate/addtimeinterval%28_%3A%29.json'
content_hash: 'sha256:e968f01602677eab'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSDate](../nsdate.md)

# addTimeInterval(_:)

<sub>Instance Method</sub>

Returns a new date object that is set to a given number of seconds relative to the receiver.

> [!warning] Deprecated
> Use [- dateByAddingTimeInterval:](<addingtimeinterval(__).md>) instead.

<sub>tvOS, visionOS, watchOS</sub>

```swift
func addTimeInterval(_ seconds: TimeInterval) -> Any
```

## Parameters

- `seconds` — The number of seconds to add to the receiver. Use a negative value for seconds to have the returned object specify a date before the receiver.

## Return Value

A new [NSDate](../nsdate.md) object that is set to `seconds` seconds relative to the receiver. The date returned might have a representation different from the receiver’s.

## See Also

### Related Documentation

- [- dateByAddingTimeInterval:](<addingtimeinterval(__).md>) — Returns a new date object that is set to a given number of seconds relative to the receiver.
- [- timeIntervalSinceDate:](<timeintervalsince(__).md>) — Returns the interval between the receiver and another given date.

### Legacy Operations

- [+ dateWithNaturalLanguageString:](<date(withnaturallanguagestring_).md>) — Creates and returns a date object set to the date and time specified by a given string. _(deprecated)_
- [+ dateWithNaturalLanguageString:locale:](<date(withnaturallanguagestring_locale_).md>) — Creates and returns a date object set to the date and time specified by a given string. _(deprecated)_
- [+ dateWithString:](<date(with_).md>) — Creates and returns a date object with a date and time value specified by a given string in the international string representation format (`YYYY-MM-DD HH:MM:SS ±HHMM`). _(deprecated)_
- [- initWithString:](<init(string_).md>) — Returns a date object initialized with a date and time value specified by a given string in the international string representation format. _(deprecated)_
- [- dateWithCalendarFormat:timeZone:](<date(withcalendarformat_timezone_).md>) — Converts the receiver to a calendar date with a given format string and time zone. _(deprecated)_
- [- descriptionWithCalendarFormat:timeZone:locale:](<description(withcalendarformat_timezone_locale_).md>) — Returns a string representation of the date formatted as specified by given conversion specifiers. _(deprecated)_
