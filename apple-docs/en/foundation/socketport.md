---
title: SocketPort
framework: Foundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/socketport
source_url: 'https://developer.apple.com/documentation/foundation/socketport'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/socketport.json'
content_hash: 'sha256:62c2f785585b4a6e'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# SocketPort

<sub>Class</sub>

A port that represents a BSD socket.

<sub>macOS</sub>

```swift
class SocketPort
```

## Overview

A [SocketPort](socketport.md) object can be used as an endpoint for distributed object connections. Companion classes, [NSMachPort](nsmachport.md) and [MessagePort](messageport.md), allow for local (on the same machine) communication only. The [SocketPort](socketport.md) class allows for both local and remote communication, but may be more expensive than the others for the local case.

> [!note] Note
> The [SocketPort](socketport.md) class conforms to the [NSCoding](nscoding.md) protocol, but only supports coding by an [NSPortCoder](nsportcoder.md). [Port](port.md) and its other subclasses do not support archiving.

## Relationships

- **Inherits From**: [Port](port.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCoding](nscoding.md), [NSCopying](nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Creating Instances

- [- init](<socketport/init().md>) — Initializes the receiver as a local TCP/IP socket of type `SOCK_STREAM`.
- [- initWithTCPPort:](<socketport/init(tcpport_)-6hgbo.md>) — Initializes the receiver as a local TCP/IP socket of type `SOCK_STREAM`, listening on a specified port number.
- [- initWithProtocolFamily:socketType:protocol:address:](<socketport/init(protocolfamily_sockettype_protocol_address_).md>) — Initializes the receiver as a local socket with the provided arguments.
- [- initWithProtocolFamily:socketType:protocol:socket:](<socketport/init(protocolfamily_sockettype_protocol_socket_).md>) — Initializes the receiver with a previously created local socket.
- [- initRemoteWithTCPPort:host:](<socketport/init(remotewithtcpport_host_).md>) — Initializes the receiver as a TCP/IP socket of type `SOCK_STREAM` that can connect to a remote host on a specified port.
- [- initRemoteWithProtocolFamily:socketType:protocol:address:](<socketport/init(remotewithprotocolfamily_sockettype_protocol_address_).md>) — Initializes the receiver as a remote socket with the provided arguments.

### Getting Information

- [address](socketport/address.md) — The receiver’s socket address structure stored inside an [NSData](nsdata.md) object.
- [protocol](socketport/protocol.md) — The protocol that the receiver uses for communication.
- [protocolFamily](socketport/protocolfamily.md) — The protocol family that the receiver uses for communication.
- [socket](socketport/socket.md) — The receiver’s native socket identifier on the platform.
- [socketType](socketport/sockettype.md) — The receiver’s socket type.

### Initializers

- [init(TCPPort:)](<socketport/init(tcpport_)-17uiq.md>)

## See Also

### Sockets

- [Host](host.md) — A representation of an individual host on the network. _(deprecated)_
- [Port](port.md) — An abstract class that represents a communication channel.
