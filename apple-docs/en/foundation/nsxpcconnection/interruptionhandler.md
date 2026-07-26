---
title: interruptionHandler
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, macOS 10.8+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsxpcconnection/interruptionhandler
source_url: 'https://developer.apple.com/documentation/foundation/nsxpcconnection/interruptionhandler'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsxpcconnection/interruptionhandler.json'
content_hash: 'sha256:63a269e609b993cc'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSXPCConnection](../nsxpcconnection.md)

# interruptionHandler

<sub>Instance Property</sub>

An interruption handler that is called if the remote process exits or crashes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var interruptionHandler: (() -> Void)? { get set }
```

## Discussion

It may be possible to re-establish the connection by simply sending another message. The handler is invoked on the same queue as reply messages and other handlers, and it is always executed after any other messages or reply block handlers (except for the invalidation handler).

## See Also

### Managing connection state

- [- activate](<activate().md>) — Activates the connection.
- [- resume](<resume().md>) — Starts or resumes handling of messages on a connection.
- [- invalidate](<invalidate().md>) — Invalidates the connection.
- [- suspend](<suspend().md>) — Suspends the connection.
- [invalidationHandler](invalidationhandler.md) — An invalidation handler that is called if the connection can not be formed or the connection has terminated and may not be re-established.
- [+ currentConnection](<current().md>) — Returns the current connection, in the context of a call to a method on your exported object.
- [- scheduleSendBarrierBlock:](<schedulesendbarrierblock(__).md>) — Add a barrier block to execute on the connection.
