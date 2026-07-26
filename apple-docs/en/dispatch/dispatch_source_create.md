---
title: dispatch_source_create
framework: Dispatch
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/dispatch/dispatch_source_create
source_url: 'https://developer.apple.com/documentation/dispatch/dispatch_source_create'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/dispatch/dispatch_source_create.json'
content_hash: 'sha256:b0ee0946fa1060af'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Dispatch](../dispatch.md)

# dispatch_source_create

<sub>Function</sub>

Creates a new dispatch source to monitor low-level system events.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
extern dispatch_source_tdispatch_source_create(dispatch_source_type_t type, uintptr_t handle, uintptr_t mask, dispatch_queue_t queue);
```

## Parameters

- `type` — The type of the dispatch source. For example, to create a timer source, specify [DISPATCH_SOURCE_TYPE_TIMER](dispatch_source_type_timer.md). For a complete list of constants, see [dispatch_source_type_t](dispatch_source_type_t.md).

- `handle` — The underlying system handle to monitor. The interpretation of this argument is determined by the constant provided in the type parameter.

- `mask` — A mask of flags specifying which events are desired. The interpretation of this argument is determined by the constant provided in the type parameter.

- `queue` — The dispatch queue to which the event handler block is submitted.

## Return Value

A new dispatch source object or `NULL` if the dispatch source could not be created.

## Discussion

Dispatch sources are not reentrant. Any events received while the dispatch source is suspended or while the event handler block is currently executing are coalesced and delivered after the dispatch source is resumed or the event handler block has returned.

Dispatch sources are created in a suspended state. After creating the source and setting any desired attributes (for example, the handler or the context), your application must call [dispatch_activate](<dispatchobject/activate().md>) to begin event delivery.

> [!important] Important
> Event source creation is asynchronous, so be aware of any race conditions with monitored system handles. For example, if a dispatch source is created for a process and that process exits before the source is created, any specified cancellation handler may not be called.

## See Also

### Creating a Dispatch Source

- [dispatch_source_t](dispatch_source_t.md) — An object that coordinates the processing of specific low-level system events, such as file-system events, timers, and UNIX signals.
- [dispatch_source_type_t](dispatch_source_type_t.md) — An identifier for the type of system object being monitored by a dispatch source.
