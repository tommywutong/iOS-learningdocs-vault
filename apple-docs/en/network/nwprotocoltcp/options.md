---
title: NWProtocolTCP.Options
framework: Network
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 12.0+, macOS 10.14+, tvOS 12.0+, visionOS 1.0+, watchOS 5.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/network/nwprotocoltcp/options
source_url: 'https://developer.apple.com/documentation/network/nwprotocoltcp/options'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nwprotocoltcp/options.json'
content_hash: 'sha256:e0c5af7aeb7fefa3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Network](../../network.md) · [NWProtocolTCP](../nwprotocoltcp.md)

# NWProtocolTCP.Options

<sub>Class</sub>

A container of options for configuring how TCP is used on a connection.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class Options
```

## Relationships

- **Inherits From**: [NWProtocolOptions](../nwprotocoloptions.md)

- **Conforms To**: [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Customizing TCP Options

- [init()](<options/init().md>) — Initializes a default set of TCP connection options.
- [enableFastOpen](options/enablefastopen.md) — A Boolean that enables TCP Fast Open on a connection.
- [maximumSegmentSize](options/maximumsegmentsize.md) — TCP’s maximum segment size in bytes.
- [noDelay](options/nodelay.md) — A Boolean that disables Nagle’s algorithm for TCP.
- [noOptions](options/nooptions.md) — A Boolean that sets TCP into no-options mode.
- [noPush](options/nopush.md) — A Boolean that sets TCP into no-push mode.
- [retransmitFinDrop](options/retransmitfindrop.md) — A Boolean that causes TCP to drop its connection after not receiving an ACK packet after a FIN packet.
- [disableAckStretching](options/disableackstretching.md) — A Boolean that disables TCP acknowledgment stretching.
- [disableECN](options/disableecn.md) — A Boolean that disables negotiation of Explicit Congestion Notification markings.

### Configuring Keepalives

- [enableKeepalive](options/enablekeepalive.md) — A Boolean that enables TCP keepalives.
- [keepaliveIdle](options/keepaliveidle.md) — The number of seconds of idleness that TCP waits before sending keepalive probes.
- [keepaliveCount](options/keepalivecount.md) — The number of keepalive probes that TCP sends before terminating the connection.
- [keepaliveInterval](options/keepaliveinterval.md) — The number of seconds that TCP waits between sending keepalive probes.

### Setting Timeouts

- [connectionTimeout](options/connectiontimeout.md) — The number of seconds that TCP waits before timing out its handshake.
- [connectionDropTime](options/connectiondroptime.md) — The timeout, in seconds, for TCP retransmission attempts.
- [persistTimeout](options/persisttimeout.md) — The TCP persist timeout, in seconds, as defined by RFC 6429.

## See Also

### Creating TCP Connections

- [definition](definition.md) — The system definition of the Transport Control Protocol.
