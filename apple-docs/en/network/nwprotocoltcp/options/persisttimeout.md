---
title: persistTimeout
framework: Network
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 12.0+, macOS 10.14+, tvOS 12.0+, visionOS 1.0+, watchOS 5.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/network/nwprotocoltcp/options/persisttimeout
source_url: 'https://developer.apple.com/documentation/network/nwprotocoltcp/options/persisttimeout'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nwprotocoltcp/options/persisttimeout.json'
content_hash: 'sha256:9d3a8f3ebe33465c'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Network](../../../network.md) · [NWProtocolTCP](../../nwprotocoltcp.md) · [Options](../options.md)

# persistTimeout

<sub>Instance Property</sub>

The TCP persist timeout, in seconds, as defined by RFC 6429.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var persistTimeout: Int { get set }
```

## See Also

### Setting Timeouts

- [connectionTimeout](connectiontimeout.md) — The number of seconds that TCP waits before timing out its handshake.
- [connectionDropTime](connectiondroptime.md) — The timeout, in seconds, for TCP retransmission attempts.
