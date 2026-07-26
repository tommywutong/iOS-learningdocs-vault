---
title: 'setCancelHandler(qos:flags:handler:)'
framework: Dispatch
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/dispatch/dispatchsourceprotocol/setcancelhandler(qos:flags:handler:)'
source_url: 'https://developer.apple.com/documentation/dispatch/dispatchsourceprotocol/setcancelhandler(qos:flags:handler:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/dispatch/dispatchsourceprotocol/setcancelhandler%28qos%3Aflags%3Ahandler%3A%29.json'
content_hash: 'sha256:bb834aee3e3f9fb1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Dispatch](../../dispatch.md) · [DispatchSourceProtocol](../dispatchsourceprotocol.md)

# setCancelHandler(qos:flags:handler:)

<sub>Instance Method</sub>

Sets the cancellation handler block for the dispatch source with the specified quality-of-service class and work item options.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func setCancelHandler(qos: DispatchQoS = .unspecified, flags: DispatchWorkItemFlags = [], handler: Self.DispatchSourceHandler?)
```

## Parameters

- `qos` — The quality-of-service to apply to the handler block.

- `flags` — Configuration flags for the work item. For a list of possible values, see [DispatchWorkItemFlags](../dispatchworkitemflags.md).

- `handler` — The event handler block to submit to the source’s target queue.

## Discussion

The cancellation handler (if specified) is submitted to the source’s target queue in response to a call to a call to the [cancel()](<cancel().md>) method once the system has released all references to the source’s underlying handle and the source’s event handler block has returned.

To safely close a file descriptor or destroy a Mach port, a cancellation handler is required for that descriptor or port. Closing the descriptor or port before the cancellation handler runs can result in a race condition. If a new descriptor is allocated with the same value as the recently closed descriptor while the source’s event handler is still running, the event handler may read/write data using the wrong descriptor.

## See Also

### Canceling a Dispatch Source

- [cancel()](<cancel().md>) — Asynchronously cancels the dispatch source, preventing any further invocation of its event handler block.
- [isCancelled](iscancelled.md) — Returns a Boolean indicating whether the given dispatch source has been canceled.
- [setCancelHandler(handler:)](<setcancelhandler(handler_).md>) — Sets the cancellation handler block for the dispatch source.
