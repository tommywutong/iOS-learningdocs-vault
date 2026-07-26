---
title: address
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/socketport/address
source_url: 'https://developer.apple.com/documentation/foundation/socketport/address'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/socketport/address.json'
content_hash: 'sha256:ab0962842212742f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [SocketPort](../socketport.md)

# address

<sub>Instance Property</sub>

The receiver’s socket address structure stored inside an [NSData](../nsdata.md) object.

<sub>macOS</sub>

```swift
var address: Data { get }
```

## See Also

### Related Documentation

- [- initRemoteWithProtocolFamily:socketType:protocol:address:](<init(remotewithprotocolfamily_sockettype_protocol_address_).md>) — Initializes the receiver as a remote socket with the provided arguments.
- [- initWithProtocolFamily:socketType:protocol:address:](<init(protocolfamily_sockettype_protocol_address_).md>) — Initializes the receiver as a local socket with the provided arguments.

### Getting Information

- [protocol](protocol.md) — The protocol that the receiver uses for communication.
- [protocolFamily](protocolfamily.md) — The protocol family that the receiver uses for communication.
- [socket](socket.md) — The receiver’s native socket identifier on the platform.
- [socketType](sockettype.md) — The receiver’s socket type.
