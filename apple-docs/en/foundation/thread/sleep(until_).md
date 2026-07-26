---
title: 'sleep(until:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/thread/sleep(until:)'
source_url: 'https://developer.apple.com/documentation/foundation/thread/sleep(until:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/thread/sleep%28until%3A%29.json'
content_hash: 'sha256:df713d5d776bc018'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Thread](../thread.md)

# sleep(until:)

<sub>Type Method</sub>

Blocks the current thread until the time specified.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class func sleep(until date: Date)
```

## Parameters

- `date` — The time at which to resume processing.

## Discussion

No run loop processing occurs while the thread is blocked.

## See Also

### Related Documentation

- [currentThread](current.md) — Returns the thread object representing the current thread of execution.

### Stopping a Thread

- [+ sleepForTimeInterval:](<sleep(fortimeinterval_).md>) — Sleeps the thread for a given time interval.
- [+ exit](<exit().md>) — Terminates the current thread.
- [- cancel](<cancel().md>) — Changes the cancelled state of the receiver to indicate that it should exit.
