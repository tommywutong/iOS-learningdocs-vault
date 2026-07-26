---
title: CFSocketSignature
framework: Core Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/cfsocketsignature
source_url: 'https://developer.apple.com/documentation/corefoundation/cfsocketsignature'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfsocketsignature.json'
content_hash: 'sha256:20fdb7ca027cbb61'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFSocketSignature

<sub>Structure</sub>

A structure that fully specifies the communication protocol and connection address of a CFSocket object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct CFSocketSignature
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md)

## Topics

### Initializers

- [init()](<cfsocketsignature/init().md>)
- [init(protocolFamily:socketType:protocol:address:)](<cfsocketsignature/init(protocolfamily_sockettype_protocol_address_).md>)

### Instance Properties

- [address](cfsocketsignature/address.md) — A CFData object holding the contents of a `struct sockaddr` appropriate for the given protocol family (`struct sockaddr_in` or `struct sockaddr_in6`, for example), identifying the address of the socket.
- [protocol](cfsocketsignature/protocol.md) — The protocol type of the socket.
- [protocolFamily](cfsocketsignature/protocolfamily.md) — The protocol family of the socket.
- [socketType](cfsocketsignature/sockettype.md) — The socket type of the socket.

## See Also

### Data Types

- [CFSocketContext](cfsocketcontext.md) — A structure that contains program-defined data and callbacks with which you can configure a CFSocket object’s behavior.
- [CFSocketNativeHandle](cfsocketnativehandle.md) — Type for the platform-specific native socket handle.
