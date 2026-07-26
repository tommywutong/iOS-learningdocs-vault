---
title: 'init(timeInterval:since:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsdate/init(timeinterval:since:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsdate/init(timeinterval:since:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsdate/init%28timeinterval%3Asince%3A%29.json'
content_hash: 'sha256:7bfaf98c2401869a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSDate](../nsdate.md)

# init(timeInterval:since:)

<sub>Initializer</sub>

Returns a date object initialized relative to another given date by a given number of seconds.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
convenience init(timeInterval secsToBeAdded: TimeInterval, since date: Date)
```

## Parameters

- `secsToBeAdded` — The number of seconds to add to `date`. A negative value means the receiver will be earlier than `date`.

- `date` — The reference date.

## Return Value

An `NSDate` object initialized relative to `date` by `secsToBeAdded` seconds.
