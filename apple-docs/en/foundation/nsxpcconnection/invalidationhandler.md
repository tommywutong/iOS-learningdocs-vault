---
title: invalidationHandler
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, macOS 10.8+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsxpcconnection/invalidationhandler
source_url: 'https://developer.apple.com/documentation/foundation/nsxpcconnection/invalidationhandler'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsxpcconnection/invalidationhandler.json'
content_hash: 'sha256:0e2cfdc5efa0ba94'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSXPCConnection](../nsxpcconnection.md)

# invalidationHandler

<sub>Instance Property</sub>

An invalidation handler that is called if the connection can not be formed or the connection has terminated and may not be re-established.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var invalidationHandler: (() -> Void)? { get set }
```

## Discussion

This handler is invoked on the same queue as reply messages and other handlers, and is always executed last (after the interruption handler, if required). You may not send messages over the connection from within an invalidation handler block.

## See Also

### Managing connection state

- [- activate](<activate().md>) — Activates the connection.
- [- resume](<resume().md>) — Starts or resumes handling of messages on a connection.
- [- invalidate](<invalidate().md>) — Invalidates the connection.
- [- suspend](<suspend().md>) — Suspends the connection.
- [interruptionHandler](interruptionhandler.md) — An interruption handler that is called if the remote process exits or crashes.
- [+ currentConnection](<current().md>) — Returns the current connection, in the context of a call to a method on your exported object.
- [- scheduleSendBarrierBlock:](<schedulesendbarrierblock(__).md>) — Add a barrier block to execute on the connection.
