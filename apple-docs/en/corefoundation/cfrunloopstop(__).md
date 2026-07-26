---
title: 'CFRunLoopStop(_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfrunloopstop(_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfrunloopstop(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfrunloopstop%28_%3A%29.json'
content_hash: 'sha256:2577f54d2db6ce1b'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFRunLoopStop(_:)

<sub>Function</sub>

Forces a CFRunLoop object to stop running.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFRunLoopStop(_ rl: CFRunLoop!)
```

## Parameters

- `rl` — The run loop to stop.

## Discussion

This function forces `rl` to stop running and return control to the function that called [CFRunLoopRun](<cfrunlooprun().md>) or [CFRunLoopRunInMode](<cfrunloopruninmode(______).md>) for the current run loop activation. If the run loop is nested with a callout from one activation starting another activation running, only the innermost activation is exited.

## See Also

### Starting and Stopping a Run Loop

- [CFRunLoopRun](<cfrunlooprun().md>) — Runs the current thread’s CFRunLoop object in its default mode indefinitely.
- [CFRunLoopRunInMode](<cfrunloopruninmode(______).md>) — Runs the current thread’s CFRunLoop object in a particular mode.
- [CFRunLoopWakeUp](<cfrunloopwakeup(__).md>) — Wakes a waiting CFRunLoop object.
- [CFRunLoopIsWaiting](<cfrunloopiswaiting(__).md>) — Returns a Boolean value that indicates whether the run loop is waiting for an event.
