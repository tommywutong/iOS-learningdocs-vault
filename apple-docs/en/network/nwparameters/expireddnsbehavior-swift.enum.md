---
title: NWParameters.ExpiredDNSBehavior
framework: Network
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 12.0+, macOS 10.14+, tvOS 12.0+, visionOS 1.0+, watchOS 5.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/network/nwparameters/expireddnsbehavior-swift.enum
source_url: 'https://developer.apple.com/documentation/network/nwparameters/expireddnsbehavior-swift.enum'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nwparameters/expireddnsbehavior-swift.enum.json'
content_hash: 'sha256:0d0309c87dfaa7d1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Network](../../network.md) · [NWParameters](../nwparameters.md)

# NWParameters.ExpiredDNSBehavior

<sub>Enumeration</sub>

Options for configuring how expired DNS answers should be used.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
enum ExpiredDNSBehavior
```

## Relationships

- **Conforms To**: [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Behaviors

- [NWParameters.ExpiredDNSBehavior.systemDefault](expireddnsbehavior-swift.enum/systemdefault.md) — Let the system determine whether or not to allow expired DNS answers.
- [NWParameters.ExpiredDNSBehavior.allow](expireddnsbehavior-swift.enum/allow.md) — Explicitly allow the use of expired DNS answers.
- [NWParameters.ExpiredDNSBehavior.prohibit](expireddnsbehavior-swift.enum/prohibit.md) — Explicitly prohibit the use of expired DNS answers.

### Enumeration Cases

- [NWParameters.ExpiredDNSBehavior.persistent](expireddnsbehavior-swift.enum/persistent.md)

## See Also

### Customizing Connection Options

- [multipathServiceType](multipathservicetype-swift.property.md) — An option to allow connections to use multipath protocols.
- [MultipathServiceType](multipathservicetype-swift.enum.md) — Modes in which a connection can support multipath protocols.
- [serviceClass](serviceclass-swift.property.md) — The traffic characteristics network connections send and receive.
- [ServiceClass](serviceclass-swift.enum.md) — Indicates how the system prioritizes transmitted traffic by your latency and throughput needs.
- [allowFastOpen](allowfastopen.md) — A Boolean that enables sending application data with protocol handshakes.
- [expiredDNSBehavior](expireddnsbehavior-swift.property.md) — A behavior that defines how expired DNS answers will be used.
- [requiresDNSSECValidation](requiresdnssecvalidation.md) — A Boolean value that determines whether a connection requires DNSSEC validation when resolving endpoints.
- [preferNoProxies](prefernoproxies.md) — A Boolean that indicates that connections should ignore proxies when they are enabled on the system.
- [includePeerToPeer](includepeertopeer.md) — A Boolean that enables peer-to-peer link technologies for connections and listeners.
- [allowLocalEndpointReuse](allowlocalendpointreuse.md) — A Boolean that allows reusing local addresses and ports across connections.
- [acceptLocalOnly](acceptlocalonly.md) — A Boolean that restricts listeners to only accepting connections from the local link.
