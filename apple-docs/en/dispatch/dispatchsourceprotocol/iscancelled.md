---
title: isCancelled
framework: Dispatch
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/dispatch/dispatchsourceprotocol/iscancelled
source_url: 'https://developer.apple.com/documentation/dispatch/dispatchsourceprotocol/iscancelled'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/dispatch/dispatchsourceprotocol/iscancelled.json'
content_hash: 'sha256:c73764d88838079a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Dispatch](../../dispatch.md) · [DispatchSourceProtocol](../dispatchsourceprotocol.md)

# isCancelled

<sub>Instance Property</sub>

Returns a Boolean indicating whether the given dispatch source has been canceled.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var isCancelled: Bool { get }
```

## See Also

### Canceling a Dispatch Source

- [cancel()](<cancel().md>) — Asynchronously cancels the dispatch source, preventing any further invocation of its event handler block.
- [setCancelHandler(handler:)](<setcancelhandler(handler_).md>) — Sets the cancellation handler block for the dispatch source.
- [setCancelHandler(qos:flags:handler:)](<setcancelhandler(qos_flags_handler_).md>) — Sets the cancellation handler block for the dispatch source with the specified quality-of-service class and work item options.
