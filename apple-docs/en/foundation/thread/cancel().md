---
title: cancel()
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/thread/cancel()
source_url: 'https://developer.apple.com/documentation/foundation/thread/cancel()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/thread/cancel%28%29.json'
content_hash: 'sha256:35c88287aed4d10e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Thread](../thread.md)

# cancel()

<sub>Instance Method</sub>

Changes the cancelled state of the receiver to indicate that it should exit.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func cancel()
```

## Discussion

The semantics of this method are the same as those used for [Operation](../operation.md). This method sets state information in the receiver that is then reflected by the [cancelled](iscancelled.md) property. Threads that support cancellation should periodically call the [cancelled](iscancelled.md) method to determine if the thread has in fact been cancelled, and exit if it has been.

For more information about cancellation and operation objects, see [Operation](../operation.md).

## See Also

### Related Documentation

- [cancelled](iscancelled.md) — A Boolean value that indicates whether the receiver is cancelled.

### Stopping a Thread

- [+ sleepUntilDate:](<sleep(until_).md>) — Blocks the current thread until the time specified.
- [+ sleepForTimeInterval:](<sleep(fortimeinterval_).md>) — Sleeps the thread for a given time interval.
- [+ exit](<exit().md>) — Terminates the current thread.
