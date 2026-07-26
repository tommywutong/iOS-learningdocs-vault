---
title: CFRunLoopActivity
framework: Core Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/cfrunloopactivity
source_url: 'https://developer.apple.com/documentation/corefoundation/cfrunloopactivity'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfrunloopactivity.json'
content_hash: 'sha256:02a5ebb95a78f603'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFRunLoopActivity

<sub>Structure</sub>

Run loop activity stages in which run loop observers can be scheduled.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct CFRunLoopActivity
```

## Overview

The run loop stages in which an observer is scheduled are selected when the observer is created with [CFRunLoopObserverCreate](<cfrunloopobservercreate(____________).md>).

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [ExpressibleByArrayLiteral](../swift/expressiblebyarrayliteral.md), [OptionSet](../swift/optionset.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [SetAlgebra](../swift/setalgebra.md)

## Topics

### Constants

- [kCFRunLoopEntry](cfrunloopactivity/entry.md) — The entrance of the run loop, before entering the event processing loop. This activity occurs once for each call to [CFRunLoopRun](<cfrunlooprun().md>) and [CFRunLoopRunInMode](<cfrunloopruninmode(______).md>).
- [kCFRunLoopBeforeTimers](cfrunloopactivity/beforetimers.md) — Inside the event processing loop before any timers are processed.
- [kCFRunLoopBeforeSources](cfrunloopactivity/beforesources.md) — Inside the event processing loop before any sources are processed.
- [kCFRunLoopBeforeWaiting](cfrunloopactivity/beforewaiting.md)
- [kCFRunLoopAfterWaiting](cfrunloopactivity/afterwaiting.md) — Inside the event processing loop after the run loop wakes up, but before processing the event that woke it up. This activity occurs only if the run loop did in fact go to sleep during the current loop.
- [kCFRunLoopExit](cfrunloopactivity/exit.md) — The exit of the run loop, after exiting the event processing loop. This activity occurs once for each call to [CFRunLoopRun](<cfrunlooprun().md>) and [CFRunLoopRunInMode](<cfrunloopruninmode(______).md>).
- [kCFRunLoopAllActivities](cfrunloopactivity/allactivities.md) — A combination of all the preceding stages.

### Initializers

- [init(rawValue:)](<cfrunloopactivity/init(rawvalue_).md>)
