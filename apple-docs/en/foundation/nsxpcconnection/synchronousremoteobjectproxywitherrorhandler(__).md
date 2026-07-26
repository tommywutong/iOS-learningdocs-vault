---
title: 'synchronousRemoteObjectProxyWithErrorHandler(_:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsxpcconnection/synchronousremoteobjectproxywitherrorhandler(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsxpcconnection/synchronousremoteobjectproxywitherrorhandler(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsxpcconnection/synchronousremoteobjectproxywitherrorhandler%28_%3A%29.json'
content_hash: 'sha256:4f0a616e7321098d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSXPCConnection](../nsxpcconnection.md)

# synchronousRemoteObjectProxyWithErrorHandler(_:)

<sub>Instance Method</sub>

Returns a proxy that makes a synchronous IPC call instead of the default async behavior.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func synchronousRemoteObjectProxyWithErrorHandler(_ handler: @escaping (any Error) -> Void) -> Any
```

## Discussion

The error handler block and reply block will be invoked on the calling thread before the message to the proxy returns, instead of on the queue for the connection.

## See Also

### Working with proxy objects

- [- remoteObjectProxyWithErrorHandler:](<remoteobjectproxywitherrorhandler(__).md>) — Returns a proxy for the remote object (that is, the object exported from the other side of this connection) with the specified error handler.
