---
title: QUIC
framework: Network
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/network/quic
source_url: 'https://developer.apple.com/documentation/network/quic'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/quic.json'
content_hash: 'sha256:e1ed17c0af2a7c57'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Network](../network.md)

# QUIC

<sub>Structure</sub>

The system definition of the QUIC protocol.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct QUIC
```

## Overview

Conforms to MultiplexProtocol, exposing configuration for a multiplexing instance of QUIC, which in turn exposes the ability to handle multiple streams of data over QUIC.

## Relationships

- **Conforms To**: [MultiplexProtocol](multiplexprotocol.md), [NetworkProtocolOptions](networkprotocoloptions.md)

## Topics

### Classes

- [Datagrams](quic/datagrams.md)
- [Stream](quic/stream.md)

### Structures

- [TLS](quic/tls-swift.struct.md) — The set of TLS options available when using QUIC.

### Initializers

- [init(alpn:)](<quic/init(alpn_).md>) — Create a QUIC protocol for use in a protocol stack.
- [init(alpn:_:)](<quic/init(alpn___).md>)

### Instance Properties

- [tls](quic/tls-swift.property.md) — Configure TLS when used within QUIC.

### Instance Methods

- [idleTimeout(_:)](<quic/idletimeout(__).md>) — Set the idle timeout for the QUIC connection, in milliseconds.
- [initialMaxBidirectionalStreams(_:)](<quic/initialmaxbidirectionalstreams(__).md>) — Set the initial_max_streams_bidi transport parameter on a QUIC connection.
- [initialMaxData(_:)](<quic/initialmaxdata(__).md>) — Set the initial_max_data transport parameter on a QUIC connection.
- [initialMaxStreamDataBidirectionalLocal(_:)](<quic/initialmaxstreamdatabidirectionallocal(__).md>) — Set the initial_max_stream_data_bidi_local transport parameter on a QUIC connection.
- [initialMaxStreamDataBidirectionalRemote(_:)](<quic/initialmaxstreamdatabidirectionalremote(__).md>) — Set the initial_max_stream_data_bidi_remote transport parameter on a QUIC connection.
- [initialMaxStreamDataUnidirectional(_:)](<quic/initialmaxstreamdataunidirectional(__).md>) — Set the initial_max_stream_data_uni transport parameter on a QUIC connection.
- [initialMaxUnidirectionalStreams(_:)](<quic/initialmaxunidirectionalstreams(__).md>) — Set the initial_max_stream_data_uni transport parameter on a QUIC connection.
- [maxDatagramFrameSize(_:)](<quic/maxdatagramframesize(__).md>) — Set the max_datagram_frame_size transport parameter on a QUIC connection.
- [maxUDPPayloadSize(_:)](<quic/maxudppayloadsize(__).md>) — Set the maximum length of a QUIC packet that you are willing to receive on a connection, in bytes.
