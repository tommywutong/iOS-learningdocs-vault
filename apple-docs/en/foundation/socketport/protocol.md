---
title: protocol
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/socketport/protocol
source_url: 'https://developer.apple.com/documentation/foundation/socketport/protocol'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/socketport/protocol.json'
content_hash: 'sha256:f4839898a3434d39'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [SocketPort](../socketport.md)

# protocol

<sub>Instance Property</sub>

The protocol that the receiver uses for communication.

<sub>macOS</sub>

```swift
var `protocol`: Int32 { get }
```

## See Also

### Getting Information

- [address](address.md) — The receiver’s socket address structure stored inside an [NSData](../nsdata.md) object.
- [protocolFamily](protocolfamily.md) — The protocol family that the receiver uses for communication.
- [socket](socket.md) — The receiver’s native socket identifier on the platform.
- [socketType](sockettype.md) — The receiver’s socket type.
