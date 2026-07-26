---
title: 'init(coder:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsdate/init(coder:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsdate/init(coder:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsdate/init%28coder%3A%29.json'
content_hash: 'sha256:59095b23fbe6d656'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSDate](../nsdate.md)

# init(coder:)

<sub>Initializer</sub>

Returns a date object initialized from data in the given unarchiver.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init?(coder: NSCoder)
```

## See Also

### Initializing a Date

- [- init](<init().md>) — Returns a date object initialized to the current date and time.
- [- initWithTimeIntervalSinceNow:](<init(timeintervalsincenow_).md>) — Returns a date object initialized relative to the current date and time by a given number of seconds.
- [- initWithTimeIntervalSinceReferenceDate:](<init(timeintervalsincereferencedate_).md>) — Returns a date object initialized relative to 00:00:00 UTC on 1 January 2001 by a given number of seconds.
- [- initWithTimeIntervalSince1970:](<init(timeintervalsince1970_).md>) — Returns a date object initialized relative to 00:00:00 UTC on 1 January 1970 by a given number of seconds.
