---
title: NSDidBecomeSingleThreaded
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 2.0+（26.0 起废弃）, iPadOS 2.0+（26.0 起废弃）, Mac Catalyst 13.1+（26.0 起废弃）, macOS 10.0+（26.0 起废弃）, tvOS 9.0+（26.0 起废弃）, visionOS 1.0+（26.0 起废弃）, watchOS 2.0+（26.0 起废弃）]
languages: [swift, swift, swift, occ, occ]
beta: false
deprecated: true
doc_path: /documentation/foundation/nsnotification/name-swift.struct/nsdidbecomesinglethreaded
source_url: 'https://developer.apple.com/documentation/foundation/nsnotification/name-swift.struct/nsdidbecomesinglethreaded'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsnotification/name-swift.struct/nsdidbecomesinglethreaded.json'
content_hash: 'sha256:1b0e857fcef5cfb6'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [NSNotification](../../nsnotification.md) · [Name](../name-swift.struct.md)

# NSDidBecomeSingleThreaded

<sub>Type Property</sub>

Not implemented.

> [!warning] Deprecated
> Programs no longer transition to single-threaded mode from threaded environments

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static let NSDidBecomeSingleThreaded: NSNotification.Name
```

## See Also

### Notifications

- [NSThreadWillExitNotification](nsthreadwillexit.md) — An `NSThread` object posts this notification when it receives the [+ exit](<../../thread/exit().md>) message, before the thread exits. Observer methods invoked to receive this notification execute in the exiting thread, before it exits. _(deprecated)_
- [NSWillBecomeMultiThreadedNotification](nswillbecomemultithreaded.md) — Posted when the first thread is detached from the current thread. The `NSThread` class posts this notification at most once—the first time a thread is detached using [+ detachNewThreadSelector:toTarget:withObject:](<../../thread/detachnewthreadselector(__totarget_with_).md>) or the [- start](<../../thread/start().md>) method. Subsequent invocations of those methods do not post this notification. Observers of this notification have their notification method invoked in the main thread, not the new thread. The observer notification methods always execute before the new thread begins executing. _(deprecated)_
