---
title: protocolFamily
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/socketport/protocolfamily
source_url: 'https://developer.apple.com/documentation/foundation/socketport/protocolfamily'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/socketport/protocolfamily.json'
content_hash: 'sha256:6e2f96ee4f934002'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [SocketPort](../socketport.md)

# protocolFamily

<sub>Instance Property</sub>

The protocol family that the receiver uses for communication.

<sub>macOS</sub>

```swift
var protocolFamily: Int32 { get }
```

## Discussion

Possible values are defined in `<sys/socket.h>`, such as `AF_LOCAL`, `AF_INET`, and `AF_INET6`.

## See Also

### Getting Information

- [address](address.md) — The receiver’s socket address structure stored inside an [NSData](../nsdata.md) object.
- [protocol](protocol.md) — The protocol that the receiver uses for communication.
- [socket](socket.md) — The receiver’s native socket identifier on the platform.
- [socketType](sockettype.md) — The receiver’s socket type.
