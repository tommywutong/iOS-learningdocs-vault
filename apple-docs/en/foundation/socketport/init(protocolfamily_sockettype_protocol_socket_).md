---
title: 'init(protocolFamily:socketType:protocol:socket:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/socketport/init(protocolfamily:sockettype:protocol:socket:)'
source_url: 'https://developer.apple.com/documentation/foundation/socketport/init(protocolfamily:sockettype:protocol:socket:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/socketport/init%28protocolfamily%3Asockettype%3Aprotocol%3Asocket%3A%29.json'
content_hash: 'sha256:2c27cbe23826a9d6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [SocketPort](../socketport.md)

# init(protocolFamily:socketType:protocol:socket:)

<sub>Initializer</sub>

Initializes the receiver with a previously created local socket.

<sub>macOS</sub>

```swift
init?(protocolFamily family: Int32, socketType type: Int32, protocol: Int32, socket sock: SocketNativeHandle)
```

## Parameters

- `family` — The protocol family for the provided socket. Possible values are defined in `<sys/socket.h>`, such as `AF_LOCAL`, `AF_INET`, and `AF_INET6`.

- `type` — The type of the provided socket.

- `protocol` — The specific protocol the provided socket uses.

- `sock` — The previously created socket.

## Return Value

A local socket port initialized with the provided socket.

## See Also

### Creating Instances

- [- init](<init().md>) — Initializes the receiver as a local TCP/IP socket of type `SOCK_STREAM`.
- [- initWithTCPPort:](<init(tcpport_)-6hgbo.md>) — Initializes the receiver as a local TCP/IP socket of type `SOCK_STREAM`, listening on a specified port number.
- [- initWithProtocolFamily:socketType:protocol:address:](<init(protocolfamily_sockettype_protocol_address_).md>) — Initializes the receiver as a local socket with the provided arguments.
- [- initRemoteWithTCPPort:host:](<init(remotewithtcpport_host_).md>) — Initializes the receiver as a TCP/IP socket of type `SOCK_STREAM` that can connect to a remote host on a specified port.
- [- initRemoteWithProtocolFamily:socketType:protocol:address:](<init(remotewithprotocolfamily_sockettype_protocol_address_).md>) — Initializes the receiver as a remote socket with the provided arguments.
