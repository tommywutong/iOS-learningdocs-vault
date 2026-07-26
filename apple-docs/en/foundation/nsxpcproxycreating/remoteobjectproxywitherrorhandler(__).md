---
title: 'remoteObjectProxyWithErrorHandler(_:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsxpcproxycreating/remoteobjectproxywitherrorhandler(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsxpcproxycreating/remoteobjectproxywitherrorhandler(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsxpcproxycreating/remoteobjectproxywitherrorhandler%28_%3A%29.json'
content_hash: 'sha256:1f8238c5af4586ac'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSXPCProxyCreating](../nsxpcproxycreating.md)

# remoteObjectProxyWithErrorHandler(_:)

<sub>Instance Method</sub>

Returns a proxy object that invokes the error handling block if an error occurs on the connection.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func remoteObjectProxyWithErrorHandler(_ handler: @escaping @Sendable (any Error) -> Void) -> Any
```

## Parameters

- `handler` — The error handling block that the proxy object should call when an error occurs while waiting for a reply.

## Discussion

If the message sent to the proxy has a reply handler, then either the error handler or the reply handler is called exactly once.

The resulting proxy object conforms to the `NSXPCProxyCreating` protocol.
