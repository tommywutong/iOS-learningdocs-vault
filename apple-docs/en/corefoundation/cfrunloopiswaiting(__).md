---
title: 'CFRunLoopIsWaiting(_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfrunloopiswaiting(_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfrunloopiswaiting(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfrunloopiswaiting%28_%3A%29.json'
content_hash: 'sha256:5ce7137ca4af0df5'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFRunLoopIsWaiting(_:)

<sub>Function</sub>

Returns a Boolean value that indicates whether the run loop is waiting for an event.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFRunLoopIsWaiting(_ rl: CFRunLoop!) -> Bool
```

## Parameters

- `rl` — The run loop to examine.

## Return Value

`true` if `rl` has no events to process and is blocking, waiting for a source or timer to become ready to fire; `false` if `rl` either is not running or is currently processing a source, timer, or observer.

## Discussion

This function is useful only to test the state of another thread’s run loop. When called with the current thread’s run loop, this function always returns `false`.

## See Also

### Starting and Stopping a Run Loop

- [CFRunLoopRun](<cfrunlooprun().md>) — Runs the current thread’s CFRunLoop object in its default mode indefinitely.
- [CFRunLoopRunInMode](<cfrunloopruninmode(______).md>) — Runs the current thread’s CFRunLoop object in a particular mode.
- [CFRunLoopWakeUp](<cfrunloopwakeup(__).md>) — Wakes a waiting CFRunLoop object.
- [CFRunLoopStop](<cfrunloopstop(__).md>) — Forces a CFRunLoop object to stop running.
