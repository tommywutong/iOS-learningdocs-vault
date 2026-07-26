---
title: allActivities
framework: Core Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/cfrunloopactivity/allactivities
source_url: 'https://developer.apple.com/documentation/corefoundation/cfrunloopactivity/allactivities'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfrunloopactivity/allactivities.json'
content_hash: 'sha256:2a466b5836196484'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Foundation](../../corefoundation.md) · [CFRunLoopActivity](../cfrunloopactivity.md)

# allActivities

<sub>Type Property</sub>

A combination of all the preceding stages.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var allActivities: CFRunLoopActivity { get }
```

## See Also

### Constants

- [kCFRunLoopEntry](entry.md) — The entrance of the run loop, before entering the event processing loop. This activity occurs once for each call to [CFRunLoopRun](<../cfrunlooprun().md>) and [CFRunLoopRunInMode](<../cfrunloopruninmode(______).md>).
- [kCFRunLoopBeforeTimers](beforetimers.md) — Inside the event processing loop before any timers are processed.
- [kCFRunLoopBeforeSources](beforesources.md) — Inside the event processing loop before any sources are processed.
- [kCFRunLoopBeforeWaiting](beforewaiting.md)
- [kCFRunLoopAfterWaiting](afterwaiting.md) — Inside the event processing loop after the run loop wakes up, but before processing the event that woke it up. This activity occurs only if the run loop did in fact go to sleep during the current loop.
- [kCFRunLoopExit](exit.md) — The exit of the run loop, after exiting the event processing loop. This activity occurs once for each call to [CFRunLoopRun](<../cfrunlooprun().md>) and [CFRunLoopRunInMode](<../cfrunloopruninmode(______).md>).
