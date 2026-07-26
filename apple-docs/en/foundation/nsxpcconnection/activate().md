---
title: activate()
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsxpcconnection/activate()
source_url: 'https://developer.apple.com/documentation/foundation/nsxpcconnection/activate()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsxpcconnection/activate%28%29.json'
content_hash: 'sha256:560157a4ef4c994e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSXPCConnection](../nsxpcconnection.md)

# activate()

<sub>Instance Method</sub>

Activates the connection.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func activate()
```

## Discussion

Connections start in an inactive state. You must call [- activate](<activate().md>) on a connection before it can send or receive any messages.

Calling [- activate](<activate().md>) on an active connection has no effect.

For backward compatibility reasons, calling [- resume](<resume().md>) on an inactive and otherwise not suspended [NSXPCConnection](../nsxpcconnection.md) has the same effect as calling [- activate](<activate().md>). For new code, prefer [- activate](<activate().md>).

## See Also

### Managing connection state

- [- resume](<resume().md>) — Starts or resumes handling of messages on a connection.
- [- invalidate](<invalidate().md>) — Invalidates the connection.
- [- suspend](<suspend().md>) — Suspends the connection.
- [interruptionHandler](interruptionhandler.md) — An interruption handler that is called if the remote process exits or crashes.
- [invalidationHandler](invalidationhandler.md) — An invalidation handler that is called if the connection can not be formed or the connection has terminated and may not be re-established.
- [+ currentConnection](<current().md>) — Returns the current connection, in the context of a call to a method on your exported object.
- [- scheduleSendBarrierBlock:](<schedulesendbarrierblock(__).md>) — Add a barrier block to execute on the connection.
