---
title: receiveTime
framework: Network
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 12.0+, macOS 10.14+, tvOS 12.0+, visionOS 1.0+, watchOS 5.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/network/nwprotocolip/metadata/receivetime
source_url: 'https://developer.apple.com/documentation/network/nwprotocolip/metadata/receivetime'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nwprotocolip/metadata/receivetime.json'
content_hash: 'sha256:409cdcfd48324a1e'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Network](../../../network.md) · [NWProtocolIP](../../nwprotocolip.md) · [Metadata](../metadata.md)

# receiveTime

<sub>Instance Property</sub>

The time at which a packet was received, in nanoseconds, based on `CLOCK_MONOTONIC_RAW`.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var receiveTime: UInt64 { get }
```

## See Also

### Related Documentation

- [shouldCalculateReceiveTime](../options/shouldcalculatereceivetime.md) — A Boolean that indicates whether a connection delivers receive timestamps for IP packets.
