---
title: NWProtocolIP.Metadata
framework: Network
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 12.0+, macOS 10.14+, tvOS 12.0+, visionOS 1.0+, watchOS 5.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/network/nwprotocolip/metadata
source_url: 'https://developer.apple.com/documentation/network/nwprotocolip/metadata'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nwprotocolip/metadata.json'
content_hash: 'sha256:29c2a6269646dda9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Network](../../network.md) · [NWProtocolIP](../nwprotocolip.md)

# NWProtocolIP.Metadata

<sub>Class</sub>

Per-packet IP metadata you configure when sending and receiving packets.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class Metadata
```

## Relationships

- **Inherits From**: [NWProtocolMetadata](../nwprotocolmetadata.md)

- **Conforms To**: [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Sending IP Options

- [init()](<metadata/init().md>) — Initializes an IP packet configuration with default settings.
- [ecn](metadata/ecn.md) — A specific Explicit Congestion Notification flag value to set on an IP packet.
- [ECN](ecn.md) — Flag values for Explicit Congestion Notifications in IP packets.
- [serviceClass](metadata/serviceclass.md) — A specific service class to mark on an IP packet.

### Receiving IP Packets

- [receiveTime](metadata/receivetime.md) — The time at which a packet was received, in nanoseconds, based on `CLOCK_MONOTONIC_RAW`.

### Instance Methods

- [ecn(_:)](<metadata/ecn(__).md>)
- [serviceClass(_:)](<metadata/serviceclass(__).md>)
