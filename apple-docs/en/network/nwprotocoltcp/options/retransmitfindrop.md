---
title: retransmitFinDrop
framework: Network
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 12.0+, macOS 10.14+, tvOS 12.0+, visionOS 1.0+, watchOS 5.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/network/nwprotocoltcp/options/retransmitfindrop
source_url: 'https://developer.apple.com/documentation/network/nwprotocoltcp/options/retransmitfindrop'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nwprotocoltcp/options/retransmitfindrop.json'
content_hash: 'sha256:00dd2143de086690'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Network](../../../network.md) · [NWProtocolTCP](../../nwprotocoltcp.md) · [Options](../options.md)

# retransmitFinDrop

<sub>Instance Property</sub>

A Boolean that causes TCP to drop its connection after not receiving an ACK packet after a FIN packet.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var retransmitFinDrop: Bool { get set }
```

## See Also

### Customizing TCP Options

- [init()](<init().md>) — Initializes a default set of TCP connection options.
- [enableFastOpen](enablefastopen.md) — A Boolean that enables TCP Fast Open on a connection.
- [maximumSegmentSize](maximumsegmentsize.md) — TCP’s maximum segment size in bytes.
- [noDelay](nodelay.md) — A Boolean that disables Nagle’s algorithm for TCP.
- [noOptions](nooptions.md) — A Boolean that sets TCP into no-options mode.
- [noPush](nopush.md) — A Boolean that sets TCP into no-push mode.
- [disableAckStretching](disableackstretching.md) — A Boolean that disables TCP acknowledgment stretching.
- [disableECN](disableecn.md) — A Boolean that disables negotiation of Explicit Congestion Notification markings.
