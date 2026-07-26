---
title: init()
framework: Network
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 12.0+, macOS 10.14+, tvOS 12.0+, visionOS 1.0+, watchOS 5.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/network/nwprotocoltcp/options/init()
source_url: 'https://developer.apple.com/documentation/network/nwprotocoltcp/options/init()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nwprotocoltcp/options/init%28%29.json'
content_hash: 'sha256:39afa239833278a1'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Network](../../../network.md) · [NWProtocolTCP](../../nwprotocoltcp.md) · [Options](../options.md)

# init()

<sub>Initializer</sub>

Initializes a default set of TCP connection options.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init()
```

## See Also

### Customizing TCP Options

- [enableFastOpen](enablefastopen.md) — A Boolean that enables TCP Fast Open on a connection.
- [maximumSegmentSize](maximumsegmentsize.md) — TCP’s maximum segment size in bytes.
- [noDelay](nodelay.md) — A Boolean that disables Nagle’s algorithm for TCP.
- [noOptions](nooptions.md) — A Boolean that sets TCP into no-options mode.
- [noPush](nopush.md) — A Boolean that sets TCP into no-push mode.
- [retransmitFinDrop](retransmitfindrop.md) — A Boolean that causes TCP to drop its connection after not receiving an ACK packet after a FIN packet.
- [disableAckStretching](disableackstretching.md) — A Boolean that disables TCP acknowledgment stretching.
- [disableECN](disableecn.md) — A Boolean that disables negotiation of Explicit Congestion Notification markings.
