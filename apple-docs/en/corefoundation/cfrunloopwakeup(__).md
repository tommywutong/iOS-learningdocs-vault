---
title: 'CFRunLoopWakeUp(_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfrunloopwakeup(_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfrunloopwakeup(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfrunloopwakeup%28_%3A%29.json'
content_hash: 'sha256:498c8e98c703902b'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFRunLoopWakeUp(_:)

<sub>Function</sub>

Wakes a waiting CFRunLoop object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFRunLoopWakeUp(_ rl: CFRunLoop!)
```

## Parameters

- `rl` — The run loop to wake up.

## Discussion

A run loop goes to sleep when it is waiting for a source or timer to become ready to fire. If no source or timer fires, the run loop stays there until it times out or is explicitly woken up. If a run loop is modified, such as a new source added, you need to wake up the run loop to allow it to process the change. Version 0 sources use [CFRunLoopWakeUp](<cfrunloopwakeup(__).md>) to cause the run loop to wake up after setting a source to be signaled, if they want the source handled immediately.

## See Also

### Starting and Stopping a Run Loop

- [CFRunLoopRun](<cfrunlooprun().md>) — Runs the current thread’s CFRunLoop object in its default mode indefinitely.
- [CFRunLoopRunInMode](<cfrunloopruninmode(______).md>) — Runs the current thread’s CFRunLoop object in a particular mode.
- [CFRunLoopStop](<cfrunloopstop(__).md>) — Forces a CFRunLoop object to stop running.
- [CFRunLoopIsWaiting](<cfrunloopiswaiting(__).md>) — Returns a Boolean value that indicates whether the run loop is waiting for an event.
