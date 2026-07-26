---
title: 'setCancelHandler(handler:)'
framework: Dispatch
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS, visionOS, watchOS]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/dispatch/dispatchsourceprotocol/setcancelhandler(handler:)'
source_url: 'https://developer.apple.com/documentation/dispatch/dispatchsourceprotocol/setcancelhandler(handler:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/dispatch/dispatchsourceprotocol/setcancelhandler%28handler%3A%29.json'
content_hash: 'sha256:189f1ced4e27d096'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Dispatch](../../dispatch.md) · [DispatchSourceProtocol](../dispatchsourceprotocol.md)

# setCancelHandler(handler:)

<sub>Instance Method</sub>

Sets the cancellation handler block for the dispatch source.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func setCancelHandler(handler: DispatchWorkItem)
```

## Parameters

- `handler` — The event handler block to submit to the source’s target queue.

## Discussion

The cancellation handler (if specified) is submitted to the source’s target queue in response to a call to a call to the [cancel()](<cancel().md>) method once the system has released all references to the source’s underlying handle and the source’s event handler block has returned.

To safely close a file descriptor or destroy a Mach port, a cancellation handler is required for that descriptor or port. Closing the descriptor or port before the cancellation handler runs can result in a race condition. If a new descriptor is allocated with the same value as the recently closed descriptor while the source’s event handler is still running, the event handler may read/write data using the wrong descriptor.

## See Also

### Canceling a Dispatch Source

- [cancel()](<cancel().md>) — Asynchronously cancels the dispatch source, preventing any further invocation of its event handler block.
- [isCancelled](iscancelled.md) — Returns a Boolean indicating whether the given dispatch source has been canceled.
- [setCancelHandler(qos:flags:handler:)](<setcancelhandler(qos_flags_handler_).md>) — Sets the cancellation handler block for the dispatch source with the specified quality-of-service class and work item options.
