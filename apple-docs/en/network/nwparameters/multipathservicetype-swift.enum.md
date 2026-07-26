---
title: NWParameters.MultipathServiceType
framework: Network
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 12.0+, macOS 10.14+, tvOS 12.0+, visionOS 1.0+, watchOS 5.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/network/nwparameters/multipathservicetype-swift.enum
source_url: 'https://developer.apple.com/documentation/network/nwparameters/multipathservicetype-swift.enum'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nwparameters/multipathservicetype-swift.enum.json'
content_hash: 'sha256:c769a8bec14780b2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Network](../../network.md) · [NWParameters](../nwparameters.md)

# NWParameters.MultipathServiceType

<sub>Enumeration</sub>

Modes in which a connection can support multipath protocols.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
enum MultipathServiceType
```

## Relationships

- **Conforms To**: [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Multipath Service Types

- [NWParameters.MultipathServiceType.disabled](multipathservicetype-swift.enum/disabled.md) — Disable multipath.
- [NWParameters.MultipathServiceType.handover](multipathservicetype-swift.enum/handover.md) — Enable multipath, but only use other interfaces when the primary interface is lost.
- [NWParameters.MultipathServiceType.interactive](multipathservicetype-swift.enum/interactive.md) — Enable multipath to use other interfaces when the primary interface encounters loss or delay.
- [NWParameters.MultipathServiceType.aggregate](multipathservicetype-swift.enum/aggregate.md) — Enable multipath to maximize bandwidth across multiple interfaces.

## See Also

### Customizing Connection Options

- [multipathServiceType](multipathservicetype-swift.property.md) — An option to allow connections to use multipath protocols.
- [serviceClass](serviceclass-swift.property.md) — The traffic characteristics network connections send and receive.
- [ServiceClass](serviceclass-swift.enum.md) — Indicates how the system prioritizes transmitted traffic by your latency and throughput needs.
- [allowFastOpen](allowfastopen.md) — A Boolean that enables sending application data with protocol handshakes.
- [expiredDNSBehavior](expireddnsbehavior-swift.property.md) — A behavior that defines how expired DNS answers will be used.
- [ExpiredDNSBehavior](expireddnsbehavior-swift.enum.md) — Options for configuring how expired DNS answers should be used.
- [requiresDNSSECValidation](requiresdnssecvalidation.md) — A Boolean value that determines whether a connection requires DNSSEC validation when resolving endpoints.
- [preferNoProxies](prefernoproxies.md) — A Boolean that indicates that connections should ignore proxies when they are enabled on the system.
- [includePeerToPeer](includepeertopeer.md) — A Boolean that enables peer-to-peer link technologies for connections and listeners.
- [allowLocalEndpointReuse](allowlocalendpointreuse.md) — A Boolean that allows reusing local addresses and ports across connections.
- [acceptLocalOnly](acceptlocalonly.md) — A Boolean that restricts listeners to only accepting connections from the local link.
