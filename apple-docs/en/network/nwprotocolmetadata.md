---
title: NWProtocolMetadata
framework: Network
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 12.0+, macOS 10.14+, tvOS 12.0+, visionOS 1.0+, watchOS 5.0+]
languages: [swift, swift, swift]
beta: false
deprecated: false
doc_path: /documentation/network/nwprotocolmetadata
source_url: 'https://developer.apple.com/documentation/network/nwprotocolmetadata'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nwprotocolmetadata.json'
content_hash: 'sha256:f84de16e7c354a1c'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Network](../network.md)

# NWProtocolMetadata

<sub>Class</sub>

The abstract superclass for specifying metadata about a network protocol.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class NWProtocolMetadata
```

## Overview

You can use metadata when sending and receiving messages, as well as when inspecting connection properties.

## Relationships

- **Inherited By**: [Message](nwprotocolframer/message.md), [Metadata](nwprotocolip/metadata.md), [Metadata](nwprotocolquic/metadata.md), [Metadata](nwprotocoltcp/metadata.md), [Metadata](nwprotocoltls/metadata.md), [Metadata](nwprotocoludp/metadata.md), [Metadata](nwprotocolwebsocket/metadata.md)

- **Conforms To**: [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## See Also

### Inspecting Connections

- [metadata(definition:)](<nwconnection/metadata(definition_).md>) — Retrieves the connection-wide metadata for a specific protocol.
- [endpoint](nwconnection/endpoint.md) — The remote endpoint with which the connection was initialized.
- [parameters](nwconnection/parameters.md) — The parameters with which the connection was initialized.
- [queue](nwconnection/queue.md) — The queue on which connection events are delivered.
