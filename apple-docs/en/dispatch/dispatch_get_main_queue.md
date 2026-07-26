---
title: dispatch_get_main_queue
framework: Dispatch
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [occ, occ]
beta: false
deprecated: false
doc_path: /documentation/dispatch/dispatch_get_main_queue
source_url: 'https://developer.apple.com/documentation/dispatch/dispatch_get_main_queue'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/dispatch/dispatch_get_main_queue.json'
content_hash: 'sha256:d03db9874685b061'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Dispatch](../dispatch.md)

# dispatch_get_main_queue

<sub>Function</sub>

Returns the serial dispatch queue associated with the application’s main thread.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
static dispatch_queue_main_tdispatch_get_main_queue();
```

## Return Value

Returns the main queue. This queue is created automatically on behalf of the main thread before `main` is called.

## Discussion

The system automatically creates the main queue and associates it with your application’s main thread. Your app uses one (and only one) of the following three approaches to invoke blocks submitted to the main queue:

- Calling [dispatch_main](<dispatchmain().md>)
- Calling [UIApplicationMain(_:_:_:_:)](<../uikit/uiapplicationmain(________)-1yub7.md>) (iOS) or [NSApplicationMain(_:_:)](<../appkit/nsapplicationmain(____).md>) (macOS)
- Using a [CFRunLoop](../corefoundation/cfrunloop.md) on the main thread

As with the global concurrent queues, calls to [dispatch_suspend](<dispatchobject/suspend().md>), [dispatch_resume](<dispatchobject/resume().md>), [dispatch_set_context](dispatch_set_context.md), and the like have no effect when used with queues returned by this function.

## See Also

### Related Documentation

- [Concurrency Programming Guide](https://developer.apple.com/library/archive/documentation/General/Conceptual/ConcurrencyProgrammingGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40008091)

### Queues and Tasks

- [dispatch_get_global_queue](dispatch_get_global_queue.md) — Returns a system-defined global concurrent queue with the specified quality-of-service class.
- [Dispatch Queue](dispatch-queue.md) — An object that manages the execution of tasks serially or concurrently on your app’s main thread or on a background thread.
- [Dispatch Work Item](dispatch-work-item.md) — The work you want to perform, encapsulated in a way that lets you attach a completion handle or execution dependencies.
- [Dispatch Group](dispatch-group.md) — A group of tasks that you monitor as a single unit.
- [Workloop](workloop.md) — A dispatch object that prioritizes the execution of tasks based on their quality-of-service (QoS) level.
