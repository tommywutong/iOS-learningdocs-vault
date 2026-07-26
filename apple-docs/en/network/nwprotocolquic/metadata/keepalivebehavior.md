---
title: NWProtocolQUIC.Metadata.KeepAliveBehavior
framework: Network
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/network/nwprotocolquic/metadata/keepalivebehavior
source_url: 'https://developer.apple.com/documentation/network/nwprotocolquic/metadata/keepalivebehavior'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nwprotocolquic/metadata/keepalivebehavior.json'
content_hash: 'sha256:d21050457369ab1e'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Network](../../../network.md) · [NWProtocolQUIC](../../nwprotocolquic.md) · [Metadata](../metadata.md)

# NWProtocolQUIC.Metadata.KeepAliveBehavior

<sub>Enumeration</sub>

A QUIC connection keepalive behavior.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
enum KeepAliveBehavior
```

## Relationships

- **Conforms To**: [Sendable](../../../swift/sendable.md), [SendableMetatype](../../../swift/sendablemetatype.md)

## Topics

### Keepalive Behaviors

- [NWProtocolQUIC.Metadata.KeepAliveBehavior.on](keepalivebehavior/on.md) — Keepalives are enabled with the default timeout.
- [NWProtocolQUIC.Metadata.KeepAliveBehavior.off](keepalivebehavior/off.md) — Keepalives are disabled.
- [NWProtocolQUIC.Metadata.KeepAliveBehavior.seconds(_:)](<keepalivebehavior/seconds(__).md>) — Keepalives are enabled with a custom timeout, in seconds.

## See Also

### Configuring Keepalives

- [keepAlive](keepalive.md) — The QUIC connection keepalive behavior.
