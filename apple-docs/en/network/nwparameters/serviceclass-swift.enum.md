---
title: NWParameters.ServiceClass
framework: Network
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 12.0+, macOS 10.14+, tvOS 12.0+, visionOS 1.0+, watchOS 5.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/network/nwparameters/serviceclass-swift.enum
source_url: 'https://developer.apple.com/documentation/network/nwparameters/serviceclass-swift.enum'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nwparameters/serviceclass-swift.enum.json'
content_hash: 'sha256:9ca62404be17f970'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Network](../../network.md) · [NWParameters](../nwparameters.md)

# NWParameters.ServiceClass

<sub>Enumeration</sub>

Indicates how the system prioritizes transmitted traffic by your latency and throughput needs.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
enum ServiceClass
```

## Overview

Use `ServiceClass` to tell the system and compatible networks how to handle your outgoing packets on Wi-Fi, Ethernet, or cellular. You describe whether your traffic favors low latency or high throughput. It prioritizes data packets transmitted on an underlying transport according to the throughput and latency characteristics of the use case. `ServiceClass` doesn’t necessarily affect the priority of packets received from a data transport, which may be set by the network. The default [NWParameters.ServiceClass.bestEffort](serviceclass-swift.enum/besteffort.md) category should be used when their isn’t a specific need or test results that indicates another service class would be helpful.

For more information on using `ServiceClass` with Wi-Fi Aware, refer to [WAAccessCategory](../../wifiaware/waaccesscategory.md).

## Relationships

- **Conforms To**: [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Service Classes

- [NWParameters.ServiceClass.bestEffort](serviceclass-swift.enum/besteffort.md) — The default service type.
- [NWParameters.ServiceClass.background](serviceclass-swift.enum/background.md) — A service type for high-delay tolerant, high-loss tolerant, elastic flow, and variable size connections.
- [NWParameters.ServiceClass.interactiveVideo](serviceclass-swift.enum/interactivevideo.md) — A service type for low-delay tolerant, very low-loss tolerant, inelastic flow, and constant packet rate connections.
- [NWParameters.ServiceClass.interactiveVoice](serviceclass-swift.enum/interactivevoice.md) — A service type for low-delay tolerant, very low-loss tolerant, inelastic flow, and constant packet rate connections.
- [NWParameters.ServiceClass.responsiveData](serviceclass-swift.enum/responsivedata.md) — A service type for medium-delay tolerant, inelastic flow, and bursty connections.
- [NWParameters.ServiceClass.signaling](serviceclass-swift.enum/signaling.md) — A service type for low-loss tolerant, inelastic flow, jitter tolerant, bursty but short rate, and variable size connections.

## See Also

### Customizing Connection Options

- [multipathServiceType](multipathservicetype-swift.property.md) — An option to allow connections to use multipath protocols.
- [MultipathServiceType](multipathservicetype-swift.enum.md) — Modes in which a connection can support multipath protocols.
- [serviceClass](serviceclass-swift.property.md) — The traffic characteristics network connections send and receive.
- [allowFastOpen](allowfastopen.md) — A Boolean that enables sending application data with protocol handshakes.
- [expiredDNSBehavior](expireddnsbehavior-swift.property.md) — A behavior that defines how expired DNS answers will be used.
- [ExpiredDNSBehavior](expireddnsbehavior-swift.enum.md) — Options for configuring how expired DNS answers should be used.
- [requiresDNSSECValidation](requiresdnssecvalidation.md) — A Boolean value that determines whether a connection requires DNSSEC validation when resolving endpoints.
- [preferNoProxies](prefernoproxies.md) — A Boolean that indicates that connections should ignore proxies when they are enabled on the system.
- [includePeerToPeer](includepeertopeer.md) — A Boolean that enables peer-to-peer link technologies for connections and listeners.
- [allowLocalEndpointReuse](allowlocalendpointreuse.md) — A Boolean that allows reusing local addresses and ports across connections.
- [acceptLocalOnly](acceptlocalonly.md) — A Boolean that restricts listeners to only accepting connections from the local link.
