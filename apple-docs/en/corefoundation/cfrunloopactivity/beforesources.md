---
title: beforeSources
framework: Core Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/cfrunloopactivity/beforesources
source_url: 'https://developer.apple.com/documentation/corefoundation/cfrunloopactivity/beforesources'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfrunloopactivity/beforesources.json'
content_hash: 'sha256:a699ee52dad96777'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Foundation](../../corefoundation.md) · [CFRunLoopActivity](../cfrunloopactivity.md)

# beforeSources

<sub>Type Property</sub>

Inside the event processing loop before any sources are processed.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var beforeSources: CFRunLoopActivity { get }
```

## See Also

### Constants

- [kCFRunLoopEntry](entry.md) — The entrance of the run loop, before entering the event processing loop. This activity occurs once for each call to [CFRunLoopRun](<../cfrunlooprun().md>) and [CFRunLoopRunInMode](<../cfrunloopruninmode(______).md>).
- [kCFRunLoopBeforeTimers](beforetimers.md) — Inside the event processing loop before any timers are processed.
- [kCFRunLoopBeforeWaiting](beforewaiting.md)
- [kCFRunLoopAfterWaiting](afterwaiting.md) — Inside the event processing loop after the run loop wakes up, but before processing the event that woke it up. This activity occurs only if the run loop did in fact go to sleep during the current loop.
- [kCFRunLoopExit](exit.md) — The exit of the run loop, after exiting the event processing loop. This activity occurs once for each call to [CFRunLoopRun](<../cfrunlooprun().md>) and [CFRunLoopRunInMode](<../cfrunloopruninmode(______).md>).
- [kCFRunLoopAllActivities](allactivities.md) — A combination of all the preceding stages.
