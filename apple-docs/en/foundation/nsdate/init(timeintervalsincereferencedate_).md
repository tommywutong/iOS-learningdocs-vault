---
title: 'init(timeIntervalSinceReferenceDate:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsdate/init(timeintervalsincereferencedate:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsdate/init(timeintervalsincereferencedate:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsdate/init%28timeintervalsincereferencedate%3A%29.json'
content_hash: 'sha256:e08a1a730f67ddbe'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSDate](../nsdate.md)

# init(timeIntervalSinceReferenceDate:)

<sub>Initializer</sub>

Returns a date object initialized relative to 00:00:00 UTC on 1 January 2001 by a given number of seconds.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(timeIntervalSinceReferenceDate ti: TimeInterval)
```

## Parameters

- `ti` — The number of seconds to add to the reference date (00:00:00 UTC on 1 January 2001). A negative value means the receiver will be earlier than the reference date.

## Return Value

An `NSDate` object initialized relative to the absolute reference date by `ti` seconds.

## Discussion

This method is a designated initializer for the `NSDate` class and is declared primarily for the use of subclasses of `NSDate`. When you subclass `NSDate` to create a concrete date class, you must override this method.

## See Also

### Initializing a Date

- [- init](<init().md>) — Returns a date object initialized to the current date and time.
- [- initWithTimeIntervalSinceNow:](<init(timeintervalsincenow_).md>) — Returns a date object initialized relative to the current date and time by a given number of seconds.
- [- initWithTimeIntervalSince1970:](<init(timeintervalsince1970_).md>) — Returns a date object initialized relative to 00:00:00 UTC on 1 January 1970 by a given number of seconds.
- [- initWithCoder:](<init(coder_).md>) — Returns a date object initialized from data in the given unarchiver.
