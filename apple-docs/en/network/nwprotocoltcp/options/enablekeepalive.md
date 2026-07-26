---
title: enableKeepalive
framework: Network
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 12.0+, macOS 10.14+, tvOS 12.0+, visionOS 1.0+, watchOS 5.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/network/nwprotocoltcp/options/enablekeepalive
source_url: 'https://developer.apple.com/documentation/network/nwprotocoltcp/options/enablekeepalive'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nwprotocoltcp/options/enablekeepalive.json'
content_hash: 'sha256:fe327efe0a99ecfd'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Network](../../../network.md) · [NWProtocolTCP](../../nwprotocoltcp.md) · [Options](../options.md)

# enableKeepalive

<sub>Instance Property</sub>

A Boolean that enables TCP keepalives.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var enableKeepalive: Bool { get set }
```

## See Also

### Configuring Keepalives

- [keepaliveIdle](keepaliveidle.md) — The number of seconds of idleness that TCP waits before sending keepalive probes.
- [keepaliveCount](keepalivecount.md) — The number of keepalive probes that TCP sends before terminating the connection.
- [keepaliveInterval](keepaliveinterval.md) — The number of seconds that TCP waits between sending keepalive probes.
