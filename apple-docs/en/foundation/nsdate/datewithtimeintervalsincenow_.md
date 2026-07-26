---
title: 'dateWithTimeIntervalSinceNow:'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsdate/datewithtimeintervalsincenow:'
source_url: 'https://developer.apple.com/documentation/foundation/nsdate/datewithtimeintervalsincenow:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsdate/datewithtimeintervalsincenow%3A.json'
content_hash: 'sha256:f5a9086e6dda1be9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSDate](../nsdate.md)

# dateWithTimeIntervalSinceNow:

<sub>Type Method</sub>

Creates and returns a date object set to a given number of seconds from the current date and time.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
+ (instancetype) dateWithTimeIntervalSinceNow:(NSTimeInterval) secs;
```

## Parameters

- `secs` — The number of seconds from the current date and time for the new date. Use a negative value to specify a date before the current date.

## Return Value

An `NSDate` object set to `secs` seconds from the current date and time.

## See Also

### Related Documentation

- [- initWithTimeIntervalSinceNow:](<init(timeintervalsincenow_).md>) — Returns a date object initialized relative to the current date and time by a given number of seconds.

### Creating a Date

- [date](date.md) — Creates and returns a new date object set to the current date and time.
- [dateWithTimeIntervalSinceReferenceDate:](datewithtimeintervalsincereferencedate_.md) — Creates and returns a date object set to a given number of seconds from 00:00:00 UTC on 1 January 2001.
- [dateWithTimeIntervalSince1970:](datewithtimeintervalsince1970_.md) — Creates and returns a date object set to the given number of seconds from 00:00:00 UTC on 1 January 1970.
