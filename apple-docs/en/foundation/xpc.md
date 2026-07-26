---
title: XPC
framework: Foundation
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/xpc
source_url: 'https://developer.apple.com/documentation/foundation/xpc'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/xpc.json'
content_hash: 'sha256:6a201de82ec4d6c5'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# XPC

<sub>API Collection</sub>

Manage secure interprocess communication.

## Topics

### XPC Client

- [NSXPCProxyCreating](nsxpcproxycreating.md) — Methods for creating new proxy objects.
- [NSXPCConnection](nsxpcconnection.md) — A bidirectional communication channel between two processes.
- [NSXPCInterface](nsxpcinterface.md) — An interface that may be sent to an exported object or remote object proxy.
- [NSXPCCoder](nsxpccoder.md) — A coder that encodes and decodes objects that your app sends over an XPC connection.

### XPC Services

- [NSXPCListener](nsxpclistener.md) — A listener that waits for new incoming connections, configures them, and accepts or rejects them.
- [NSXPCListenerDelegate](nsxpclistenerdelegate.md) — The protocol that delegates to the XPC listener use to accept or reject new connections.
- [NSXPCListenerEndpoint](nsxpclistenerendpoint.md) — An object that names a specific XPC listener.

## See Also

### Low-Level Utilities

- [Object Runtime](object-runtime.md) — Get low-level support for basic Objective-C features, Cocoa design patterns, and Swift integration.
- [Processes and Threads](processes-and-threads.md) — Manage your app’s interaction with the host operating system and other processes, and implement low-level concurrency features.
- [Streams, Sockets, and Ports](streams-sockets-and-ports.md) — Use low-level Unix features to manage input and output among files, processes, and the network.
