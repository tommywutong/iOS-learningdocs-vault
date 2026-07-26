---
title: init()
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/socketport/init()
source_url: 'https://developer.apple.com/documentation/foundation/socketport/init()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/socketport/init%28%29.json'
content_hash: 'sha256:a723b1e94aa26d3e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [SocketPort](../socketport.md)

# init()

<sub>Initializer</sub>

Initializes the receiver as a local TCP/IP socket of type `SOCK_STREAM`.

<sub>macOS</sub>

```swift
convenience init()
```

## Return Value

An initialized local TCP/IP socket port of type `SOCK_STREAM`.

## Discussion

The port number is selected by the system.

## See Also

### Related Documentation

- [Distributed Objects Programming Topics](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/DistrObjects/DistrObjects.html#//apple_ref/doc/uid/10000102i)

### Creating Instances

- [- initWithTCPPort:](<init(tcpport_)-6hgbo.md>) — Initializes the receiver as a local TCP/IP socket of type `SOCK_STREAM`, listening on a specified port number.
- [- initWithProtocolFamily:socketType:protocol:address:](<init(protocolfamily_sockettype_protocol_address_).md>) — Initializes the receiver as a local socket with the provided arguments.
- [- initWithProtocolFamily:socketType:protocol:socket:](<init(protocolfamily_sockettype_protocol_socket_).md>) — Initializes the receiver with a previously created local socket.
- [- initRemoteWithTCPPort:host:](<init(remotewithtcpport_host_).md>) — Initializes the receiver as a TCP/IP socket of type `SOCK_STREAM` that can connect to a remote host on a specified port.
- [- initRemoteWithProtocolFamily:socketType:protocol:address:](<init(remotewithprotocolfamily_sockettype_protocol_address_).md>) — Initializes the receiver as a remote socket with the provided arguments.
