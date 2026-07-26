---
title: dispatch_queue_create_with_target
framework: Dispatch
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.12+, tvOS 10.0+, visionOS 1.0+, watchOS 3.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/dispatch/dispatch_queue_create_with_target
source_url: 'https://developer.apple.com/documentation/dispatch/dispatch_queue_create_with_target'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/dispatch/dispatch_queue_create_with_target.json'
content_hash: 'sha256:4d4142e14a69be2d'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Dispatch](../dispatch.md)

# dispatch_queue_create_with_target

<sub>Function</sub>

Creates a new dispatch queue to which you can submit blocks.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
extern dispatch_queue_tdispatch_queue_create_with_target(const char *label, dispatch_queue_attr_t attr, dispatch_queue_t target);
```

## Parameters

- `label` — A string label to attach to the queue to uniquely identify it in debugging tools such as Instruments, sample, stackshots, and crash reports.  Because applications, libraries, and frameworks can all create their own dispatch queues, a reverse-DNS naming style (_com.example.myqueue_) is recommended.  This parameter is optional and can be `NULL`.

- `attr` — The queue attributes. Specify [DISPATCH_QUEUE_SERIAL](dispatch_queue_serial.md) (or `NULL`) to create a serial queue or specify [DISPATCH_QUEUE_CONCURRENT](dispatch_queue_concurrent.md) to create a concurrent queue.

- `target` — The target queue on which to execute blocks. This method retains the target queue. Specify `DISPATCH_TARGET_QUEUE_DEFAULT` to set the target queue to the default type for the current dispatch queue.

## Return Value

The newly created dispatch queue.

## See Also

### Creating a Dispatch Queue

- [dispatch_get_main_queue](dispatch_get_main_queue.md) — Returns the serial dispatch queue associated with the application’s main thread.
- [dispatch_get_global_queue](dispatch_get_global_queue.md) — Returns a system-defined global concurrent queue with the specified quality-of-service class.
- [dispatch_queue_create](dispatch_queue_create.md) — Creates a new dispatch queue to which you can submit blocks.
- [DISPATCH_QUEUE_SERIAL](dispatch_queue_serial.md) — A dispatch queue that executes blocks serially in FIFO order.
- [DISPATCH_QUEUE_CONCURRENT](dispatch_queue_concurrent.md) — A dispatch queue that executes blocks concurrently.
- [dispatch_queue_t](dispatch_queue_t.md) — A lightweight object to which your application submits blocks for subsequent execution.
- [dispatch_queue_main_t](dispatch_queue_main_t.md) — A dispatch queue that is bound to the app’s main thread and executes tasks serially on that thread.
- [dispatch_queue_global_t](dispatch_queue_global_t.md) — A dispatch queue that executes tasks concurrently using threads from the global thread pool.
- [dispatch_queue_serial_t](dispatch_queue_serial_t.md) — A dispatch queue that executes tasks serially in first-in, first-out (FIFO) order.
- [dispatch_queue_concurrent_t](dispatch_queue_concurrent_t.md) — A dispatch queue that executes tasks concurrently and in any order, respecting any barriers that may be in place.
