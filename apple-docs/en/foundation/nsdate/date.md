---
title: date
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsdate/date
source_url: 'https://developer.apple.com/documentation/foundation/nsdate/date'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsdate/date.json'
content_hash: 'sha256:5839ca5137a1a8cf'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSDate](../nsdate.md)

# date

<sub>Type Method</sub>

Creates and returns a new date object set to the current date and time.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
+ (instancetype) date;
```

## Return Value

A new date object set to the current date and time.

## Discussion

This method uses the default initializer method for the class, [- init](<init().md>).

The following code sample shows how to use [date](date.md) to get the current date:

```objc
NSDate *today = [NSDate date];
```

## See Also

### Related Documentation

- [Date and Time Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/DatesAndTimes/DatesAndTimes.html#//apple_ref/doc/uid/10000039i)
- [Property List Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/PropertyLists/Introduction/Introduction.html#//apple_ref/doc/uid/10000048i)

### Creating a Date

- [dateWithTimeIntervalSinceNow:](datewithtimeintervalsincenow_.md) — Creates and returns a date object set to a given number of seconds from the current date and time.
- [dateWithTimeIntervalSinceReferenceDate:](datewithtimeintervalsincereferencedate_.md) — Creates and returns a date object set to a given number of seconds from 00:00:00 UTC on 1 January 2001.
- [dateWithTimeIntervalSince1970:](datewithtimeintervalsince1970_.md) — Creates and returns a date object set to the given number of seconds from 00:00:00 UTC on 1 January 1970.
