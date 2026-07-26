---
title: beforeWaiting
framework: Core Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/cfrunloopactivity/beforewaiting
source_url: 'https://developer.apple.com/documentation/corefoundation/cfrunloopactivity/beforewaiting'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfrunloopactivity/beforewaiting.json'
content_hash: 'sha256:3a604ab13ccc5968'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Foundation](../../corefoundation.md) · [CFRunLoopActivity](../cfrunloopactivity.md)

# beforeWaiting

<sub>Type Property</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var beforeWaiting: CFRunLoopActivity { get }
```

## Discussion

Inside the event processing loop before the run loop sleeps, waiting for a source or timer to fire. This activity does not occur if [CFRunLoopRunInMode](<../cfrunloopruninmode(______).md>) is called with a timeout of 0 seconds. It also does not occur in a particular iteration of the event processing loop if a version 0 source fires.

## See Also

### Constants

- [kCFRunLoopEntry](entry.md) — The entrance of the run loop, before entering the event processing loop. This activity occurs once for each call to [CFRunLoopRun](<../cfrunlooprun().md>) and [CFRunLoopRunInMode](<../cfrunloopruninmode(______).md>).
- [kCFRunLoopBeforeTimers](beforetimers.md) — Inside the event processing loop before any timers are processed.
- [kCFRunLoopBeforeSources](beforesources.md) — Inside the event processing loop before any sources are processed.
- [kCFRunLoopAfterWaiting](afterwaiting.md) — Inside the event processing loop after the run loop wakes up, but before processing the event that woke it up. This activity occurs only if the run loop did in fact go to sleep during the current loop.
- [kCFRunLoopExit](exit.md) — The exit of the run loop, after exiting the event processing loop. This activity occurs once for each call to [CFRunLoopRun](<../cfrunlooprun().md>) and [CFRunLoopRunInMode](<../cfrunloopruninmode(______).md>).
- [kCFRunLoopAllActivities](allactivities.md) — A combination of all the preceding stages.
