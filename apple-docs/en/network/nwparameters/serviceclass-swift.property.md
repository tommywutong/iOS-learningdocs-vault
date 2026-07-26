---
title: serviceClass
framework: Network
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 12.0+, macOS 10.14+, tvOS 12.0+, visionOS 1.0+, watchOS 5.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/network/nwparameters/serviceclass-swift.property
source_url: 'https://developer.apple.com/documentation/network/nwparameters/serviceclass-swift.property'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nwparameters/serviceclass-swift.property.json'
content_hash: 'sha256:40d8afc8a1139da6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Network](../../network.md) · [NWParameters](../nwparameters.md)

# serviceClass

<sub>Instance Property</sub>

The traffic characteristics network connections send and receive.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
final var serviceClass: NWParameters.ServiceClass { get set }
```

## Discussion

The `serviceClass` you use tells the system and compatible networks how to prioritize transmitted packets on Wi-Fi, Ethernet, or cellular for a given connection. Describe whether your traffic favors low latency (for immediacy), or high throughput (for bulk transfers), and the transport may schedule your outgoing packets to reflect that tradeoff.

Use [NWParameters.ServiceClass.bestEffort](serviceclass-swift.enum/besteffort.md) by default. Choose a different class only when you have a specific requirement or measurement showing that another choice improves your results on the networks your app uses.

Certain cellular networks also offer Network Slicing, which can use `serviceClass` to isolate traffic based on its expected characteristics.

## Enabling Network Slicing

There are two steps to enable Cellular Network Slicing:

- Set the entitlements in your property list for [5G Network Slicing App Category](../../bundleresources/entitlements/com.apple.developer.networking.slicing.appcategory.md) and [5G Network Slicing Traffic Category](../../bundleresources/entitlements/com.apple.developer.networking.slicing.trafficcategory.md). If you don’t entitle your app by specifying both these entitlements, your apps network connections won’t be using Cellular Network Slicing, even if supported by the carrier.
- Set this to the appropriate [ServiceClass](serviceclass-swift.enum.md).

## See Also

### Customizing Connection Options

- [multipathServiceType](multipathservicetype-swift.property.md) — An option to allow connections to use multipath protocols.
- [MultipathServiceType](multipathservicetype-swift.enum.md) — Modes in which a connection can support multipath protocols.
- [ServiceClass](serviceclass-swift.enum.md) — Indicates how the system prioritizes transmitted traffic by your latency and throughput needs.
- [allowFastOpen](allowfastopen.md) — A Boolean that enables sending application data with protocol handshakes.
- [expiredDNSBehavior](expireddnsbehavior-swift.property.md) — A behavior that defines how expired DNS answers will be used.
- [ExpiredDNSBehavior](expireddnsbehavior-swift.enum.md) — Options for configuring how expired DNS answers should be used.
- [requiresDNSSECValidation](requiresdnssecvalidation.md) — A Boolean value that determines whether a connection requires DNSSEC validation when resolving endpoints.
- [preferNoProxies](prefernoproxies.md) — A Boolean that indicates that connections should ignore proxies when they are enabled on the system.
- [includePeerToPeer](includepeertopeer.md) — A Boolean that enables peer-to-peer link technologies for connections and listeners.
- [allowLocalEndpointReuse](allowlocalendpointreuse.md) — A Boolean that allows reusing local addresses and ports across connections.
- [acceptLocalOnly](acceptlocalonly.md) — A Boolean that restricts listeners to only accepting connections from the local link.
