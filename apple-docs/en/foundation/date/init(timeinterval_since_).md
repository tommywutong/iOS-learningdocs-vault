---
title: 'init(timeInterval:since:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/date/init(timeinterval:since:)'
source_url: 'https://developer.apple.com/documentation/foundation/date/init(timeinterval:since:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/date/init%28timeinterval%3Asince%3A%29.json'
content_hash: 'sha256:b83ca4e816b6f821'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Date](../date.md)

# init(timeInterval:since:)

<sub>Initializer</sub>

Creates a date value initialized relative to another given date by a given number of seconds.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(timeInterval: TimeInterval, since date: Date)
```

## Parameters

- `timeInterval` — The number of seconds to add to `date`. A negative value means the receiver will be earlier than `date`.

- `date` — The reference date.

## See Also

### Creating a Date

- [init()](<init().md>) — Creates a date value initialized to the current date and time.
- [init(timeIntervalSinceNow:)](<init(timeintervalsincenow_).md>) — Creates a date value initialized relative to the current date and time by a given number of seconds.
- [init(timeIntervalSinceReferenceDate:)](<init(timeintervalsincereferencedate_).md>) — Creates a date value initialized relative to 00:00:00 UTC on 1 January 2001 by a given number of seconds.
- [init(timeIntervalSince1970:)](<init(timeintervalsince1970_).md>) — Creates a date value initialized relative to 00:00:00 UTC on 1 January 1970 by a given number of seconds.
