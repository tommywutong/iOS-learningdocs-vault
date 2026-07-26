---
title: invalidate()
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, macOS 10.8+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsxpcconnection/invalidate()
source_url: 'https://developer.apple.com/documentation/foundation/nsxpcconnection/invalidate()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsxpcconnection/invalidate%28%29.json'
content_hash: 'sha256:3595e4c4dc33775a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSXPCConnection](../nsxpcconnection.md)

# invalidate()

<sub>Instance Method</sub>

Invalidates the connection.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func invalidate()
```

## Discussion

When you call this method, all outstanding reply blocks, error handling blocks, and invalidation blocks are called on the message handling queue. The connection must be invalidated before it is deallocated. After a connection is invalidated, no more messages may be sent or received.

## See Also

### Managing connection state

- [- activate](<activate().md>) — Activates the connection.
- [- resume](<resume().md>) — Starts or resumes handling of messages on a connection.
- [- suspend](<suspend().md>) — Suspends the connection.
- [interruptionHandler](interruptionhandler.md) — An interruption handler that is called if the remote process exits or crashes.
- [invalidationHandler](invalidationhandler.md) — An invalidation handler that is called if the connection can not be formed or the connection has terminated and may not be re-established.
- [+ currentConnection](<current().md>) — Returns the current connection, in the context of a call to a method on your exported object.
- [- scheduleSendBarrierBlock:](<schedulesendbarrierblock(__).md>) — Add a barrier block to execute on the connection.
