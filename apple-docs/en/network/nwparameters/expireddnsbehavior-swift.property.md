---
title: expiredDNSBehavior
framework: Network
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 12.0+, macOS 10.14+, tvOS 12.0+, visionOS 1.0+, watchOS 5.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/network/nwparameters/expireddnsbehavior-swift.property
source_url: 'https://developer.apple.com/documentation/network/nwparameters/expireddnsbehavior-swift.property'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nwparameters/expireddnsbehavior-swift.property.json'
content_hash: 'sha256:b1c7dd752bd2e21b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Network](../../network.md) · [NWParameters](../nwparameters.md)

# expiredDNSBehavior

<sub>Instance Property</sub>

A behavior that defines how expired DNS answers will be used.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
final var expiredDNSBehavior: NWParameters.ExpiredDNSBehavior { get set }
```

## See Also

### Customizing Connection Options

- [multipathServiceType](multipathservicetype-swift.property.md) — An option to allow connections to use multipath protocols.
- [MultipathServiceType](multipathservicetype-swift.enum.md) — Modes in which a connection can support multipath protocols.
- [serviceClass](serviceclass-swift.property.md) — The traffic characteristics network connections send and receive.
- [ServiceClass](serviceclass-swift.enum.md) — Indicates how the system prioritizes transmitted traffic by your latency and throughput needs.
- [allowFastOpen](allowfastopen.md) — A Boolean that enables sending application data with protocol handshakes.
- [ExpiredDNSBehavior](expireddnsbehavior-swift.enum.md) — Options for configuring how expired DNS answers should be used.
- [requiresDNSSECValidation](requiresdnssecvalidation.md) — A Boolean value that determines whether a connection requires DNSSEC validation when resolving endpoints.
- [preferNoProxies](prefernoproxies.md) — A Boolean that indicates that connections should ignore proxies when they are enabled on the system.
- [includePeerToPeer](includepeertopeer.md) — A Boolean that enables peer-to-peer link technologies for connections and listeners.
- [allowLocalEndpointReuse](allowlocalendpointreuse.md) — A Boolean that allows reusing local addresses and ports across connections.
- [acceptLocalOnly](acceptlocalonly.md) — A Boolean that restricts listeners to only accepting connections from the local link.
