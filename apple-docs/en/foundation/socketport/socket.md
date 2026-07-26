---
title: socket
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/socketport/socket
source_url: 'https://developer.apple.com/documentation/foundation/socketport/socket'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/socketport/socket.json'
content_hash: 'sha256:09d3d3112a2334bb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [SocketPort](../socketport.md)

# socket

<sub>Instance Property</sub>

The receiver’s native socket identifier on the platform.

<sub>macOS</sub>

```swift
var socket: SocketNativeHandle { get }
```

## Discussion

In macOS, the native socket identifier is an integer file descriptor.

## See Also

### Getting Information

- [address](address.md) — The receiver’s socket address structure stored inside an [NSData](../nsdata.md) object.
- [protocol](protocol.md) — The protocol that the receiver uses for communication.
- [protocolFamily](protocolfamily.md) — The protocol family that the receiver uses for communication.
- [socketType](sockettype.md) — The receiver’s socket type.
