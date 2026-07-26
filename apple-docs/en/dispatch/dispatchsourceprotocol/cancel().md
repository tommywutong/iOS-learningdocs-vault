---
title: cancel()
framework: Dispatch
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/dispatch/dispatchsourceprotocol/cancel()
source_url: 'https://developer.apple.com/documentation/dispatch/dispatchsourceprotocol/cancel()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/dispatch/dispatchsourceprotocol/cancel%28%29.json'
content_hash: 'sha256:07f8497ca26b805b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Dispatch](../../dispatch.md) · [DispatchSourceProtocol](../dispatchsourceprotocol.md)

# cancel()

<sub>Instance Method</sub>

Asynchronously cancels the dispatch source, preventing any further invocation of its event handler block.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func cancel()
```

## Discussion

Cancellation prevents any further invocation of the event handler block for the dispatch source, but does not interrupt any work that is already in progress. If a cancellation handler was set before cancellation, it is sub mitted to the target queue once any in-progress event handler work is finished. Once the cancellation handler is submitted, it is safe to close the source’s handle (file descriptor or mach port). It is invalid to close a file descriptor or deallocate a mach port that is currently being tracked by a dispatch source object before the cancellation handler is invoked.

## See Also

### Canceling a Dispatch Source

- [isCancelled](iscancelled.md) — Returns a Boolean indicating whether the given dispatch source has been canceled.
- [setCancelHandler(handler:)](<setcancelhandler(handler_).md>) — Sets the cancellation handler block for the dispatch source.
- [setCancelHandler(qos:flags:handler:)](<setcancelhandler(qos_flags_handler_).md>) — Sets the cancellation handler block for the dispatch source with the specified quality-of-service class and work item options.
