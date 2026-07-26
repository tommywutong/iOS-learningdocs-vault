---
title: serviceRegistrationUpdateHandler
framework: Network
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 12.0+, macOS 10.14+, tvOS 12.0+, visionOS 1.0+, watchOS 5.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/network/nwlistener/serviceregistrationupdatehandler
source_url: 'https://developer.apple.com/documentation/network/nwlistener/serviceregistrationupdatehandler'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nwlistener/serviceregistrationupdatehandler.json'
content_hash: 'sha256:b248b03cbf058e1c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Network](../../network.md) · [NWListener](../nwlistener.md)

# serviceRegistrationUpdateHandler

<sub>Instance Property</sub>

A handler that receives updates for the service endpoint being advertised.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@preconcurrency final var serviceRegistrationUpdateHandler: (@Sendable (NWListener.ServiceRegistrationChange) -> Void)? { get set }
```

## See Also

### Advertising Bonjour Services

- [NSBonjourServices](../../bundleresources/information-property-list/nsbonjourservices.md) — Bonjour service types browsed by the app.
- [NSLocalNetworkUsageDescription](../../bundleresources/information-property-list/nslocalnetworkusagedescription.md) — A message that tells people why the app is requesting access to the local network.
- [service](service-swift.property.md) — A Bonjour service that advertises the listener on the local network.
- [Service](service-swift.struct.md) — A description used to advertise the Bonjour service that a listener provides.
- [ServiceRegistrationChange](serviceregistrationchange.md) — Changes to how a network listener’s service is advertised.
