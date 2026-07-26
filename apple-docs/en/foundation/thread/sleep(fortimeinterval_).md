---
title: 'sleep(forTimeInterval:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/thread/sleep(fortimeinterval:)'
source_url: 'https://developer.apple.com/documentation/foundation/thread/sleep(fortimeinterval:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/thread/sleep%28fortimeinterval%3A%29.json'
content_hash: 'sha256:1952fbb41aa7d51b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Thread](../thread.md)

# sleep(forTimeInterval:)

<sub>Type Method</sub>

Sleeps the thread for a given time interval.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class func sleep(forTimeInterval ti: TimeInterval)
```

## Parameters

- `ti` — The duration of the sleep.

## Discussion

No run loop processing occurs while the thread is blocked.

## See Also

### Stopping a Thread

- [+ sleepUntilDate:](<sleep(until_).md>) — Blocks the current thread until the time specified.
- [+ exit](<exit().md>) — Terminates the current thread.
- [- cancel](<cancel().md>) — Changes the cancelled state of the receiver to indicate that it should exit.
