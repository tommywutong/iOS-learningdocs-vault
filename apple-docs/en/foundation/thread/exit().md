---
title: exit()
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/thread/exit()
source_url: 'https://developer.apple.com/documentation/foundation/thread/exit()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/thread/exit%28%29.json'
content_hash: 'sha256:1118a38b982f0e4e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Thread](../thread.md)

# exit()

<sub>Type Method</sub>

Terminates the current thread.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class func exit()
```

## Discussion

This method uses the [currentThread](current.md) class method to access the current thread. Before exiting the thread, this method posts the [NSThreadWillExitNotification](../nsnotification/name-swift.struct/nsthreadwillexit.md) with the thread being exited to the default notification center. Because notifications are delivered synchronously, all observers of [NSThreadWillExitNotification](../nsnotification/name-swift.struct/nsthreadwillexit.md) are guaranteed to receive the notification before the thread exits.

Invoking this method should be avoided as it does not give your thread a chance to clean up any resources it allocated during its execution.

## See Also

### Related Documentation

- [currentThread](current.md) — Returns the thread object representing the current thread of execution.

### Stopping a Thread

- [+ sleepUntilDate:](<sleep(until_).md>) — Blocks the current thread until the time specified.
- [+ sleepForTimeInterval:](<sleep(fortimeinterval_).md>) — Sleeps the thread for a given time interval.
- [- cancel](<cancel().md>) — Changes the cancelled state of the receiver to indicate that it should exit.
