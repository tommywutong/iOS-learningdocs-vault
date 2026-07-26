---
title: beforeTimers
framework: Core Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/cfrunloopactivity/beforetimers
source_url: 'https://developer.apple.com/documentation/corefoundation/cfrunloopactivity/beforetimers'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfrunloopactivity/beforetimers.json'
content_hash: 'sha256:d770da31c4b29e9d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Foundation](../../corefoundation.md) · [CFRunLoopActivity](../cfrunloopactivity.md)

# beforeTimers

<sub>Type Property</sub>

Inside the event processing loop before any timers are processed.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var beforeTimers: CFRunLoopActivity { get }
```

## See Also

### Constants

- [kCFRunLoopEntry](entry.md) — The entrance of the run loop, before entering the event processing loop. This activity occurs once for each call to [CFRunLoopRun](<../cfrunlooprun().md>) and [CFRunLoopRunInMode](<../cfrunloopruninmode(______).md>).
- [kCFRunLoopBeforeSources](beforesources.md) — Inside the event processing loop before any sources are processed.
- [kCFRunLoopBeforeWaiting](beforewaiting.md)
- [kCFRunLoopAfterWaiting](afterwaiting.md) — Inside the event processing loop after the run loop wakes up, but before processing the event that woke it up. This activity occurs only if the run loop did in fact go to sleep during the current loop.
- [kCFRunLoopExit](exit.md) — The exit of the run loop, after exiting the event processing loop. This activity occurs once for each call to [CFRunLoopRun](<../cfrunlooprun().md>) and [CFRunLoopRunInMode](<../cfrunloopruninmode(______).md>).
- [kCFRunLoopAllActivities](allactivities.md) — A combination of all the preceding stages.
