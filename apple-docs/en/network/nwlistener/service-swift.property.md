---
title: service
framework: Network
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 12.0+, macOS 10.14+, tvOS 12.0+, visionOS 1.0+, watchOS 5.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/network/nwlistener/service-swift.property
source_url: 'https://developer.apple.com/documentation/network/nwlistener/service-swift.property'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nwlistener/service-swift.property.json'
content_hash: 'sha256:f6368fbfdc6abcee'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Network](../../network.md) · [NWListener](../nwlistener.md)

# service

<sub>Instance Property</sub>

A Bonjour service that advertises the listener on the local network.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
final var service: NWListener.Service? { get set }
```

## See Also

### Advertising Bonjour Services

- [NSBonjourServices](../../bundleresources/information-property-list/nsbonjourservices.md) — Bonjour service types browsed by the app.
- [NSLocalNetworkUsageDescription](../../bundleresources/information-property-list/nslocalnetworkusagedescription.md) — A message that tells people why the app is requesting access to the local network.
- [Service](service-swift.struct.md) — A description used to advertise the Bonjour service that a listener provides.
- [serviceRegistrationUpdateHandler](serviceregistrationupdatehandler.md) — A handler that receives updates for the service endpoint being advertised.
- [ServiceRegistrationChange](serviceregistrationchange.md) — Changes to how a network listener’s service is advertised.
