---
title: 'detachNewThreadSelector(_:toTarget:with:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/thread/detachnewthreadselector(_:totarget:with:)'
source_url: 'https://developer.apple.com/documentation/foundation/thread/detachnewthreadselector(_:totarget:with:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/thread/detachnewthreadselector%28_%3Atotarget%3Awith%3A%29.json'
content_hash: 'sha256:ca894e9f8fc6626c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Thread](../thread.md)

# detachNewThreadSelector(_:toTarget:with:)

<sub>Type Method</sub>

Detaches a new thread and uses the specified selector as the thread entry point.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class func detachNewThreadSelector(_ selector: Selector, toTarget target: Any, with argument: Any?)
```

## Parameters

- `selector` — The selector for the message to send to the target. This selector must take only one argument and must not have a return value.

- `target` — The object that will receive the message `aSelector` on the new thread.

- `argument` — The single argument passed to the target. May be `nil`.

## Discussion

The objects `aTarget` and `anArgument` are retained during the execution of the detached thread, then released. The detached thread is exited (using the [+ exit](<exit().md>) class method) as soon as `aTarget` has completed executing the `aSelector` method.

If this thread is the first thread detached in the application, this method posts the [NSWillBecomeMultiThreadedNotification](../nsnotification/name-swift.struct/nswillbecomemultithreaded.md) with object `nil` to the default notification center.

## See Also

### Related Documentation

- [+ isMultiThreaded](<ismultithreaded().md>) — Returns whether the application is multithreaded.
- [currentThread](current.md) — Returns the thread object representing the current thread of execution.

### Starting a Thread

- [- start](<start().md>) — Starts the receiver.
- [- main](<main().md>) — The main entry point routine for the thread.
