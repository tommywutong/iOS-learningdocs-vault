---
title: NSXPCListenerDelegate
framework: Foundation
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsxpclistenerdelegate
source_url: 'https://developer.apple.com/documentation/foundation/nsxpclistenerdelegate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsxpclistenerdelegate.json'
content_hash: 'sha256:f7eaef2c156affae'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSXPCListenerDelegate

<sub>Protocol</sub>

The protocol that delegates to the XPC listener use to accept or reject new connections.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
protocol NSXPCListenerDelegate : NSObjectProtocol
```

## Relationships

- **Inherits From**: [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Instance Methods

- [- listener:shouldAcceptNewConnection:](<nsxpclistenerdelegate/listener(__shouldacceptnewconnection_).md>) — Accepts or rejects a new connection to the listener.

## See Also

### XPC Services

- [NSXPCListener](nsxpclistener.md) — A listener that waits for new incoming connections, configures them, and accepts or rejects them.
- [NSXPCListenerEndpoint](nsxpclistenerendpoint.md) — An object that names a specific XPC listener.
