---
title: 'init(timeIntervalSince1970:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsdate/init(timeintervalsince1970:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsdate/init(timeintervalsince1970:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsdate/init%28timeintervalsince1970%3A%29.json'
content_hash: 'sha256:66ce534a095108b5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSDate](../nsdate.md)

# init(timeIntervalSince1970:)

<sub>Initializer</sub>

Returns a date object initialized relative to 00:00:00 UTC on 1 January 1970 by a given number of seconds.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
convenience init(timeIntervalSince1970 secs: TimeInterval)
```

## Parameters

- `secs` — The number of seconds from the reference date (00:00:00 UTC on 1 January 1970) for the new date. Use a negative argument to specify a date and time before the reference date.

## Return Value

An `NSDate` object set to `seconds` seconds from the reference date.

## Discussion

This method is useful for creating `NSDate` objects from time_t values returned by BSD system functions.

## See Also

### Initializing a Date

- [- init](<init().md>) — Returns a date object initialized to the current date and time.
- [- initWithTimeIntervalSinceNow:](<init(timeintervalsincenow_).md>) — Returns a date object initialized relative to the current date and time by a given number of seconds.
- [- initWithTimeIntervalSinceReferenceDate:](<init(timeintervalsincereferencedate_).md>) — Returns a date object initialized relative to 00:00:00 UTC on 1 January 2001 by a given number of seconds.
- [- initWithCoder:](<init(coder_).md>) — Returns a date object initialized from data in the given unarchiver.
