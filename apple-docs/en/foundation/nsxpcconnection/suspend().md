---
title: suspend()
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, macOS 10.8+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsxpcconnection/suspend()
source_url: 'https://developer.apple.com/documentation/foundation/nsxpcconnection/suspend()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsxpcconnection/suspend%28%29.json'
content_hash: 'sha256:45a2d07b17051c24'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSXPCConnection](../nsxpcconnection.md)

# suspend()

<sub>Instance Method</sub>

Suspends the connection.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func suspend()
```

## Discussion

As you cannot invalidate a suspended connection, every call to [- suspend](<../nsxpclistener/suspend().md>) that you make must be balanced by a call to [- resume](<resume().md>).

## See Also

### Managing connection state

- [- activate](<activate().md>) — Activates the connection.
- [- resume](<resume().md>) — Starts or resumes handling of messages on a connection.
- [- invalidate](<invalidate().md>) — Invalidates the connection.
- [interruptionHandler](interruptionhandler.md) — An interruption handler that is called if the remote process exits or crashes.
- [invalidationHandler](invalidationhandler.md) — An invalidation handler that is called if the connection can not be formed or the connection has terminated and may not be re-established.
- [+ currentConnection](<current().md>) — Returns the current connection, in the context of a call to a method on your exported object.
- [- scheduleSendBarrierBlock:](<schedulesendbarrierblock(__).md>) — Add a barrier block to execute on the connection.
