---
title: NWProtocolIP.ECN
framework: Network
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 12.0+, macOS 10.14+, tvOS 12.0+, visionOS 1.0+, watchOS 5.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/network/nwprotocolip/ecn
source_url: 'https://developer.apple.com/documentation/network/nwprotocolip/ecn'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nwprotocolip/ecn.json'
content_hash: 'sha256:b08a782c837554bb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Network](../../network.md) · [NWProtocolIP](../nwprotocolip.md)

# NWProtocolIP.ECN

<sub>Enumeration</sub>

Flag values for Explicit Congestion Notifications in IP packets.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
enum ECN
```

## Relationships

- **Conforms To**: [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md)

## Topics

### ECN Flags

- [NWProtocolIP.ECN.nonECT](ecn/nonect.md) — Non-ECN Capable Transport.
- [NWProtocolIP.ECN.ect0](ecn/ect0.md) — ECN Capable Transport (flag 0).
- [NWProtocolIP.ECN.ect1](ecn/ect1.md) — ECN Capable Transport (flag 1).
- [NWProtocolIP.ECN.ce](ecn/ce.md) — Congestion Experienced.

## See Also

### Sending IP Options

- [init()](<metadata/init().md>) — Initializes an IP packet configuration with default settings.
- [ecn](metadata/ecn.md) — A specific Explicit Congestion Notification flag value to set on an IP packet.
- [serviceClass](metadata/serviceclass.md) — A specific service class to mark on an IP packet.
