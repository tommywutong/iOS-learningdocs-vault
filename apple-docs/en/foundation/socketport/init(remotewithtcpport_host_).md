---
title: 'init(remoteWithTCPPort:host:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/socketport/init(remotewithtcpport:host:)'
source_url: 'https://developer.apple.com/documentation/foundation/socketport/init(remotewithtcpport:host:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/socketport/init%28remotewithtcpport%3Ahost%3A%29.json'
content_hash: 'sha256:ec4414cd8c8399f9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [SocketPort](../socketport.md)

# init(remoteWithTCPPort:host:)

<sub>Initializer</sub>

Initializes the receiver as a TCP/IP socket of type `SOCK_STREAM` that can connect to a remote host on a specified port.

<sub>macOS</sub>

```swift
convenience init?(remoteWithTCPPort port: UInt16, host hostName: String?)
```

## Parameters

- `port` — The port to connect to.

- `hostName` — The host name to connect to. `hostName` may be either a host name or an IPv4-style address.

## Return Value

A TCP/IP socket port of type `SOCK_STREAM` that can connect to the remote host `hostName` on port `port`.

## Discussion

A connection is not opened to the remote host until data is sent.

## See Also

### Creating Instances

- [- init](<init().md>) — Initializes the receiver as a local TCP/IP socket of type `SOCK_STREAM`.
- [- initWithTCPPort:](<init(tcpport_)-6hgbo.md>) — Initializes the receiver as a local TCP/IP socket of type `SOCK_STREAM`, listening on a specified port number.
- [- initWithProtocolFamily:socketType:protocol:address:](<init(protocolfamily_sockettype_protocol_address_).md>) — Initializes the receiver as a local socket with the provided arguments.
- [- initWithProtocolFamily:socketType:protocol:socket:](<init(protocolfamily_sockettype_protocol_socket_).md>) — Initializes the receiver with a previously created local socket.
- [- initRemoteWithProtocolFamily:socketType:protocol:address:](<init(remotewithprotocolfamily_sockettype_protocol_address_).md>) — Initializes the receiver as a remote socket with the provided arguments.
