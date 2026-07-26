---
title: NSXPCProxyCreating
framework: Foundation
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsxpcproxycreating
source_url: 'https://developer.apple.com/documentation/foundation/nsxpcproxycreating'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsxpcproxycreating.json'
content_hash: 'sha256:cd60442716c5a6c0'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSXPCProxyCreating

<sub>Protocol</sub>

Methods for creating new proxy objects.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
protocol NSXPCProxyCreating
```

## Overview

[NSXPCConnection](nsxpcconnection.md) implements this protocol. All objects returned from the methods in this protocol also implement the protocol. This allows creation of new proxies from other proxies.

## Relationships

- **Conforming Types**: [NSXPCConnection](nsxpcconnection.md)

## Topics

### Instance Methods

- [- remoteObjectProxy](<nsxpcproxycreating/remoteobjectproxy().md>) — Returns a proxy object with no error handling block.
- [- remoteObjectProxyWithErrorHandler:](<nsxpcproxycreating/remoteobjectproxywitherrorhandler(__).md>) — Returns a proxy object that invokes the error handling block if an error occurs on the connection.
- [- synchronousRemoteObjectProxyWithErrorHandler:](<nsxpcproxycreating/synchronousremoteobjectproxywitherrorhandler(__).md>) — Returns a proxy that makes a synchronous IPC call instead of the default async behavior.

## See Also

### XPC Client

- [NSXPCConnection](nsxpcconnection.md) — A bidirectional communication channel between two processes.
- [NSXPCInterface](nsxpcinterface.md) — An interface that may be sent to an exported object or remote object proxy.
- [NSXPCCoder](nsxpccoder.md) — A coder that encodes and decodes objects that your app sends over an XPC connection.
