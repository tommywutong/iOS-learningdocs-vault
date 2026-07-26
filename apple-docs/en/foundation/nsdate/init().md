---
title: init()
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsdate/init()
source_url: 'https://developer.apple.com/documentation/foundation/nsdate/init()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsdate/init%28%29.json'
content_hash: 'sha256:d00698666333a86f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSDate](../nsdate.md)

# init()

<sub>Initializer</sub>

Returns a date object initialized to the current date and time.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init()
```

## Return Value

An `NSDate` object initialized to the current date and time.

## Discussion

This method is a designated initializer for `NSDate`.

## See Also

### Initializing a Date

- [- initWithTimeIntervalSinceNow:](<init(timeintervalsincenow_).md>) — Returns a date object initialized relative to the current date and time by a given number of seconds.
- [- initWithTimeIntervalSinceReferenceDate:](<init(timeintervalsincereferencedate_).md>) — Returns a date object initialized relative to 00:00:00 UTC on 1 January 2001 by a given number of seconds.
- [- initWithTimeIntervalSince1970:](<init(timeintervalsince1970_).md>) — Returns a date object initialized relative to 00:00:00 UTC on 1 January 1970 by a given number of seconds.
- [- initWithCoder:](<init(coder_).md>) — Returns a date object initialized from data in the given unarchiver.
