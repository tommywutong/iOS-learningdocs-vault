---
title: 'dateWithTimeIntervalSinceReferenceDate:'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsdate/datewithtimeintervalsincereferencedate:'
source_url: 'https://developer.apple.com/documentation/foundation/nsdate/datewithtimeintervalsincereferencedate:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsdate/datewithtimeintervalsincereferencedate%3A.json'
content_hash: 'sha256:1c869b48f74912bc'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSDate](../nsdate.md)

# dateWithTimeIntervalSinceReferenceDate:

<sub>Type Method</sub>

Creates and returns a date object set to a given number of seconds from 00:00:00 UTC on 1 January 2001.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
+ (instancetype) dateWithTimeIntervalSinceReferenceDate:(NSTimeInterval) ti;
```

## Parameters

- `ti` — The number of seconds from the absolute reference date (00:00:00 UTC on 1 January 2001) for the new date. Use a negative argument to specify a date and time before the reference date.

## Return Value

An `NSDate` object set to `ti` seconds from the absolute reference date.

## See Also

### Related Documentation

- [- initWithTimeIntervalSinceReferenceDate:](<init(timeintervalsincereferencedate_).md>) — Returns a date object initialized relative to 00:00:00 UTC on 1 January 2001 by a given number of seconds.

### Creating a Date

- [date](date.md) — Creates and returns a new date object set to the current date and time.
- [dateWithTimeIntervalSinceNow:](datewithtimeintervalsincenow_.md) — Creates and returns a date object set to a given number of seconds from the current date and time.
- [dateWithTimeIntervalSince1970:](datewithtimeintervalsince1970_.md) — Creates and returns a date object set to the given number of seconds from 00:00:00 UTC on 1 January 1970.
