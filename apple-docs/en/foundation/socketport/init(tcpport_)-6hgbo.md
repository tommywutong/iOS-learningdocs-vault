---
title: 'init(tcpPort:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/socketport/init(tcpport:)-6hgbo'
source_url: 'https://developer.apple.com/documentation/foundation/socketport/init(tcpport:)-6hgbo'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/socketport/init%28tcpport%3A%29-6hgbo.json'
content_hash: 'sha256:0b9619c76e4a772b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [SocketPort](../socketport.md)

# init(tcpPort:)

<sub>Initializer</sub>

Initializes the receiver as a local TCP/IP socket of type `SOCK_STREAM`, listening on a specified port number.

<sub>macOS</sub>

```swift
convenience init?(tcpPort port: UInt16)
```

## Parameters

- `port` — The port number for the newly created socket port to listen on. If `port` is 0, the system will assign a port number.

## Return Value

An initialized local TCP/IP socket of type `SOCK_STREAM`, listening on port `port`.

## Discussion

This method creates an IPv4 port, not an IPv6 port.

## See Also

### Creating Instances

- [- init](<init().md>) — Initializes the receiver as a local TCP/IP socket of type `SOCK_STREAM`.
- [- initWithProtocolFamily:socketType:protocol:address:](<init(protocolfamily_sockettype_protocol_address_).md>) — Initializes the receiver as a local socket with the provided arguments.
- [- initWithProtocolFamily:socketType:protocol:socket:](<init(protocolfamily_sockettype_protocol_socket_).md>) — Initializes the receiver with a previously created local socket.
- [- initRemoteWithTCPPort:host:](<init(remotewithtcpport_host_).md>) — Initializes the receiver as a TCP/IP socket of type `SOCK_STREAM` that can connect to a remote host on a specified port.
- [- initRemoteWithProtocolFamily:socketType:protocol:address:](<init(remotewithprotocolfamily_sockettype_protocol_address_).md>) — Initializes the receiver as a remote socket with the provided arguments.
