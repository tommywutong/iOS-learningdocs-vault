---
title: keepaliveCount
framework: Network
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 12.0+, macOS 10.14+, tvOS 12.0+, visionOS 1.0+, watchOS 5.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/network/nwprotocoltcp/options/keepalivecount
source_url: 'https://developer.apple.com/documentation/network/nwprotocoltcp/options/keepalivecount'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nwprotocoltcp/options/keepalivecount.json'
content_hash: 'sha256:81949009327d4b51'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Network](../../../network.md) · [NWProtocolTCP](../../nwprotocoltcp.md) · [Options](../options.md)

# keepaliveCount

<sub>Instance Property</sub>

The number of keepalive probes that TCP sends before terminating the connection.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var keepaliveCount: Int { get set }
```

## See Also

### Configuring Keepalives

- [enableKeepalive](enablekeepalive.md) — A Boolean that enables TCP keepalives.
- [keepaliveIdle](keepaliveidle.md) — The number of seconds of idleness that TCP waits before sending keepalive probes.
- [keepaliveInterval](keepaliveinterval.md) — The number of seconds that TCP waits between sending keepalive probes.
