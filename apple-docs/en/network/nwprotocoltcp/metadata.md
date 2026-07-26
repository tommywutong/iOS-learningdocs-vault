---
title: NWProtocolTCP.Metadata
framework: Network
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 12.0+, macOS 10.14+, tvOS 12.0+, visionOS 1.0+, watchOS 5.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/network/nwprotocoltcp/metadata
source_url: 'https://developer.apple.com/documentation/network/nwprotocoltcp/metadata'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nwprotocoltcp/metadata.json'
content_hash: 'sha256:1493af45223541c1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Network](../../network.md) · [NWProtocolTCP](../nwprotocoltcp.md)

# NWProtocolTCP.Metadata

<sub>Class</sub>

A handle you can use to inspect a connection’s TCP state.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class Metadata
```

## Relationships

- **Inherits From**: [NWProtocolMetadata](../nwprotocolmetadata.md)

- **Conforms To**: [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Inspecting TCP State

- [availableSendBuffer](metadata/availablesendbuffer.md) — The number of available bytes in the TCP send buffer.
- [availableReceiveBuffer](metadata/availablereceivebuffer.md) — The number of available bytes in the TCP receive buffer.

### Instance Methods

- [setMaximumPacingRateBytesPerSecond(_:)](<metadata/setmaximumpacingratebytespersecond(__).md>) — Set the maximum pacing rate for this TCP connection, in bytes per second. _(beta)_
