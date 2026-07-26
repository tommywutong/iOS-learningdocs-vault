---
title: connectionDropTime
framework: Network
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 12.0+, macOS 10.14+, tvOS 12.0+, visionOS 1.0+, watchOS 5.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/network/nwprotocoltcp/options/connectiondroptime
source_url: 'https://developer.apple.com/documentation/network/nwprotocoltcp/options/connectiondroptime'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nwprotocoltcp/options/connectiondroptime.json'
content_hash: 'sha256:0e71e17f1e04595b'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Network](../../../network.md) · [NWProtocolTCP](../../nwprotocoltcp.md) · [Options](../options.md)

# connectionDropTime

<sub>Instance Property</sub>

The timeout, in seconds, for TCP retransmission attempts.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var connectionDropTime: Int { get set }
```

## See Also

### Setting Timeouts

- [connectionTimeout](connectiontimeout.md) — The number of seconds that TCP waits before timing out its handshake.
- [persistTimeout](persisttimeout.md) — The TCP persist timeout, in seconds, as defined by RFC 6429.
