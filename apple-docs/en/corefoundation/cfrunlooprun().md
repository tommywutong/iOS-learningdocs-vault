---
title: CFRunLoopRun()
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/cfrunlooprun()
source_url: 'https://developer.apple.com/documentation/corefoundation/cfrunlooprun()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfrunlooprun%28%29.json'
content_hash: 'sha256:743bd1fb26e573b4'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFRunLoopRun()

<sub>Function</sub>

Runs the current thread’s CFRunLoop object in its default mode indefinitely.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFRunLoopRun()
```

## Discussion

The current thread’s run loop runs in the default mode (see [Default Run Loop Mode](default-run-loop-mode.md)) until the run loop is stopped with [CFRunLoopStop](<cfrunloopstop(__).md>) or all the sources and timers are removed from the default run loop mode.

Run loops can be run recursively. You can call [CFRunLoopRun](<cfrunlooprun().md>) from within any run loop callout and create nested run loop activations on the current thread’s call stack.

## See Also

### Starting and Stopping a Run Loop

- [CFRunLoopRunInMode](<cfrunloopruninmode(______).md>) — Runs the current thread’s CFRunLoop object in a particular mode.
- [CFRunLoopWakeUp](<cfrunloopwakeup(__).md>) — Wakes a waiting CFRunLoop object.
- [CFRunLoopStop](<cfrunloopstop(__).md>) — Forces a CFRunLoop object to stop running.
- [CFRunLoopIsWaiting](<cfrunloopiswaiting(__).md>) — Returns a Boolean value that indicates whether the run loop is waiting for an event.
