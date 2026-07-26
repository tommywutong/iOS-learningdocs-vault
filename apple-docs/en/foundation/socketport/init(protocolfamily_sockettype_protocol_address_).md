---
title: 'init(protocolFamily:socketType:protocol:address:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/socketport/init(protocolfamily:sockettype:protocol:address:)'
source_url: 'https://developer.apple.com/documentation/foundation/socketport/init(protocolfamily:sockettype:protocol:address:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/socketport/init%28protocolfamily%3Asockettype%3Aprotocol%3Aaddress%3A%29.json'
content_hash: 'sha256:0e29daf7c33d484c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [SocketPort](../socketport.md)

# init(protocolFamily:socketType:protocol:address:)

<sub>Initializer</sub>

Initializes the receiver as a local socket with the provided arguments.

<sub>macOS</sub>

```swift
init?(protocolFamily family: Int32, socketType type: Int32, protocol: Int32, address: Data)
```

## Parameters

- `family` — The protocol family for the socket port. Possible values are defined in `<sys/socket.h>`, such as `AF_LOCAL`, `AF_INET`, and `AF_INET6`.

- `type` — The type of socket.

- `protocol` — The specific protocol to use from the protocol family.

- `address` — The family-specific socket address for the receiver copied into an `NSData` object.

## Return Value

A local socket port initialized with the provided arguments.

## Discussion

The receiver must be added to a run loop before it can accept connections or receive messages. Incoming messages are passed to the receiver’s delegate method handlePortMessage:.

To create a standard TCP/IP socket, use [- initWithTCPPort:](<init(tcpport_)-6hgbo.md>).

## See Also

### Creating Instances

- [- init](<init().md>) — Initializes the receiver as a local TCP/IP socket of type `SOCK_STREAM`.
- [- initWithTCPPort:](<init(tcpport_)-6hgbo.md>) — Initializes the receiver as a local TCP/IP socket of type `SOCK_STREAM`, listening on a specified port number.
- [- initWithProtocolFamily:socketType:protocol:socket:](<init(protocolfamily_sockettype_protocol_socket_).md>) — Initializes the receiver with a previously created local socket.
- [- initRemoteWithTCPPort:host:](<init(remotewithtcpport_host_).md>) — Initializes the receiver as a TCP/IP socket of type `SOCK_STREAM` that can connect to a remote host on a specified port.
- [- initRemoteWithProtocolFamily:socketType:protocol:address:](<init(remotewithprotocolfamily_sockettype_protocol_address_).md>) — Initializes the receiver as a remote socket with the provided arguments.
