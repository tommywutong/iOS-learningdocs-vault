---
title: 'remoteObjectProxyWithErrorHandler(_:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, macOS 10.8+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsxpcconnection/remoteobjectproxywitherrorhandler(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsxpcconnection/remoteobjectproxywitherrorhandler(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsxpcconnection/remoteobjectproxywitherrorhandler%28_%3A%29.json'
content_hash: 'sha256:d724bc1ed9f72cc8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSXPCConnection](../nsxpcconnection.md)

# remoteObjectProxyWithErrorHandler(_:)

<sub>Instance Method</sub>

Returns a proxy for the remote object (that is, the object exported from the other side of this connection) with the specified error handler.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func remoteObjectProxyWithErrorHandler(_ handler: @escaping (any Error) -> Void) -> Any
```

## Discussion

See descriptions in [NSXPCProxyCreating](../nsxpcproxycreating.md) for more details.

## See Also

### Working with proxy objects

- [- synchronousRemoteObjectProxyWithErrorHandler:](<synchronousremoteobjectproxywitherrorhandler(__).md>) — Returns a proxy that makes a synchronous IPC call instead of the default async behavior.
