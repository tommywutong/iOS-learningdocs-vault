---
title: QUIC.Stream
framework: Network
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/network/quic/stream
source_url: 'https://developer.apple.com/documentation/network/quic/stream'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/quic/stream.json'
content_hash: 'sha256:808f72bc1df72e27'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Network](../../network.md) · [QUIC](../quic.md)

# QUIC.Stream

<sub>Class</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
final class Stream<ApplicationProtocol> where ApplicationProtocol : NetworkProtocolOptions
```

## Relationships

- **Inherits From**: [NetworkChannel](../networkchannel.md)

- **Conforms To**: [CustomDebugStringConvertible](../../swift/customdebugstringconvertible.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [Identifiable](../../swift/identifiable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Instance Properties

- [directionality](stream/directionality.md) — The directionality of this stream, either bidirectional or unidirectional.
- [initiator](stream/initiator.md) — The initiator of this QUIC stream, either client or server.
- [parent](stream/parent.md)
- [streamApplicationErrorCode](stream/streamapplicationerrorcode.md) — The QUIC application error code to send for the stream, or received from the peer.
- [streamID](stream/streamid.md) — The QUIC stream identifier.
