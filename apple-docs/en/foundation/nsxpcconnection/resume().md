---
title: resume()
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, macOS 10.8+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsxpcconnection/resume()
source_url: 'https://developer.apple.com/documentation/foundation/nsxpcconnection/resume()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsxpcconnection/resume%28%29.json'
content_hash: 'sha256:41f9423c131fd615'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSXPCConnection](../nsxpcconnection.md)

# resume()

<sub>Instance Method</sub>

Starts or resumes handling of messages on a connection.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func resume()
```

## Discussion

All connections start suspended. You must resume them before they start processing received messages or sending messages through the [- remoteObjectProxy](<../nsxpcproxycreating/remoteobjectproxy().md>) object.

## See Also

### Managing connection state

- [- activate](<activate().md>) — Activates the connection.
- [- invalidate](<invalidate().md>) — Invalidates the connection.
- [- suspend](<suspend().md>) — Suspends the connection.
- [interruptionHandler](interruptionhandler.md) — An interruption handler that is called if the remote process exits or crashes.
- [invalidationHandler](invalidationhandler.md) — An invalidation handler that is called if the connection can not be formed or the connection has terminated and may not be re-established.
- [+ currentConnection](<current().md>) — Returns the current connection, in the context of a call to a method on your exported object.
- [- scheduleSendBarrierBlock:](<schedulesendbarrierblock(__).md>) — Add a barrier block to execute on the connection.
