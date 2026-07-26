---
title: keepaliveIdle
framework: Network
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 12.0+, macOS 10.14+, tvOS 12.0+, visionOS 1.0+, watchOS 5.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/network/nwprotocoltcp/options/keepaliveidle
source_url: 'https://developer.apple.com/documentation/network/nwprotocoltcp/options/keepaliveidle'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nwprotocoltcp/options/keepaliveidle.json'
content_hash: 'sha256:c5584a5515394171'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Network](../../../network.md) · [NWProtocolTCP](../../nwprotocoltcp.md) · [Options](../options.md)

# keepaliveIdle

<sub>Instance Property</sub>

The number of seconds of idleness that TCP waits before sending keepalive probes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var keepaliveIdle: Int { get set }
```

## See Also

### Configuring Keepalives

- [enableKeepalive](enablekeepalive.md) — A Boolean that enables TCP keepalives.
- [keepaliveCount](keepalivecount.md) — The number of keepalive probes that TCP sends before terminating the connection.
- [keepaliveInterval](keepaliveinterval.md) — The number of seconds that TCP waits between sending keepalive probes.
