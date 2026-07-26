---
title: start()
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/thread/start()
source_url: 'https://developer.apple.com/documentation/foundation/thread/start()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/thread/start%28%29.json'
content_hash: 'sha256:012f4b8e4491b638'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Thread](../thread.md)

# start()

<sub>Instance Method</sub>

Starts the receiver.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func start()
```

## Discussion

This method asynchronously spawns the new thread and invokes the receiver’s [- main](<main().md>) method on the new thread. The [executing](isexecuting.md) property returns [true](../../swift/true.md) once the thread starts executing, which may occur after the [- start](<start().md>) method returns.

If you initialized the receiver with a target and selector, the default [- main](<main().md>) method invokes that selector automatically.

If this thread is the first thread detached in the application, this method posts the [NSWillBecomeMultiThreadedNotification](../nsnotification/name-swift.struct/nswillbecomemultithreaded.md) with object `nil` to the default notification center.

## See Also

### Related Documentation

- [- initWithTarget:selector:object:](<init(target_selector_object_).md>) — Returns an `NSThread` object initialized with the given arguments.
- [- init](<init().md>) — Returns an initialized `NSThread` object.

### Starting a Thread

- [+ detachNewThreadSelector:toTarget:withObject:](<detachnewthreadselector(__totarget_with_).md>) — Detaches a new thread and uses the specified selector as the thread entry point.
- [- main](<main().md>) — The main entry point routine for the thread.
