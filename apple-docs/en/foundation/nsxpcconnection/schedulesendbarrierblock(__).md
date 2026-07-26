---
title: 'scheduleSendBarrierBlock(_:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsxpcconnection/schedulesendbarrierblock(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsxpcconnection/schedulesendbarrierblock(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsxpcconnection/schedulesendbarrierblock%28_%3A%29.json'
content_hash: 'sha256:94207fd87abb720d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSXPCConnection](../nsxpcconnection.md)

# scheduleSendBarrierBlock(_:)

<sub>Instance Method</sub>

Add a barrier block to execute on the connection.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func scheduleSendBarrierBlock(_ block: @escaping () -> Void)
```

## Parameters

- `block` — A block or closure to execute. This block takes no parameters and returns no value.

## Discussion

This barrier block runs after any outstanding send commands complete. However, the remote process isn’t guaranteed to receive the sent messages by the time the block executes. If you need to ensure the remote process received a message, wait for a reply from the process.

## See Also

### Managing connection state

- [- activate](<activate().md>) — Activates the connection.
- [- resume](<resume().md>) — Starts or resumes handling of messages on a connection.
- [- invalidate](<invalidate().md>) — Invalidates the connection.
- [- suspend](<suspend().md>) — Suspends the connection.
- [interruptionHandler](interruptionhandler.md) — An interruption handler that is called if the remote process exits or crashes.
- [invalidationHandler](invalidationhandler.md) — An invalidation handler that is called if the connection can not be formed or the connection has terminated and may not be re-established.
- [+ currentConnection](<current().md>) — Returns the current connection, in the context of a call to a method on your exported object.
