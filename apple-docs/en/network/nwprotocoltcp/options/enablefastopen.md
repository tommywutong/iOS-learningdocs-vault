---
title: enableFastOpen
framework: Network
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 12.0+, macOS 10.14+, tvOS 12.0+, visionOS 1.0+, watchOS 5.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/network/nwprotocoltcp/options/enablefastopen
source_url: 'https://developer.apple.com/documentation/network/nwprotocoltcp/options/enablefastopen'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nwprotocoltcp/options/enablefastopen.json'
content_hash: 'sha256:10565c92f9c62304'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Network](../../../network.md) · [NWProtocolTCP](../../nwprotocoltcp.md) · [Options](../options.md)

# enableFastOpen

<sub>Instance Property</sub>

A Boolean that enables TCP Fast Open on a connection.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var enableFastOpen: Bool { get set }
```

## Discussion

If TCP Fast Open is enabled and TLS is running on top of TCP, the TLS handshake will automatically be used as the TCP early data. If there is no protocol running on top of TCP, you should also enable fast open on the connection parameters and send idempotent data.

## See Also

### Related Documentation

- [allowFastOpen](../../nwparameters/allowfastopen.md) — A Boolean that enables sending application data with protocol handshakes.
- [NWConnection.SendCompletion.idempotent](../../nwconnection/sendcompletion/idempotent.md) — Mark the sent data as idempotent—data that can be sent multiple times.

### Customizing TCP Options

- [init()](<init().md>) — Initializes a default set of TCP connection options.
- [maximumSegmentSize](maximumsegmentsize.md) — TCP’s maximum segment size in bytes.
- [noDelay](nodelay.md) — A Boolean that disables Nagle’s algorithm for TCP.
- [noOptions](nooptions.md) — A Boolean that sets TCP into no-options mode.
- [noPush](nopush.md) — A Boolean that sets TCP into no-push mode.
- [retransmitFinDrop](retransmitfindrop.md) — A Boolean that causes TCP to drop its connection after not receiving an ACK packet after a FIN packet.
- [disableAckStretching](disableackstretching.md) — A Boolean that disables TCP acknowledgment stretching.
- [disableECN](disableecn.md) — A Boolean that disables negotiation of Explicit Congestion Notification markings.
