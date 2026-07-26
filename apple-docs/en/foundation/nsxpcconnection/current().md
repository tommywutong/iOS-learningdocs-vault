---
title: current()
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, macOS 10.8+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsxpcconnection/current()
source_url: 'https://developer.apple.com/documentation/foundation/nsxpcconnection/current()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsxpcconnection/current%28%29.json'
content_hash: 'sha256:e18bc90132ea7295'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSXPCConnection](../nsxpcconnection.md)

# current()

<sub>Type Method</sub>

Returns the current connection, in the context of a call to a method on your exported object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class func current() -> NSXPCConnection?
```

## Return Value

An [NSXPCConnection](../nsxpcconnection.md) object, representing a connection to another process.

## Discussion

Use this method to determine what process invoked the current call.

## See Also

### Managing connection state

- [- activate](<activate().md>) — Activates the connection.
- [- resume](<resume().md>) — Starts or resumes handling of messages on a connection.
- [- invalidate](<invalidate().md>) — Invalidates the connection.
- [- suspend](<suspend().md>) — Suspends the connection.
- [interruptionHandler](interruptionhandler.md) — An interruption handler that is called if the remote process exits or crashes.
- [invalidationHandler](invalidationhandler.md) — An invalidation handler that is called if the connection can not be formed or the connection has terminated and may not be re-established.
- [- scheduleSendBarrierBlock:](<schedulesendbarrierblock(__).md>) — Add a barrier block to execute on the connection.
