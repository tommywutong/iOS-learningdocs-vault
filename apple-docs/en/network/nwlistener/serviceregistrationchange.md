---
title: NWListener.ServiceRegistrationChange
framework: Network
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 12.0+, macOS 10.14+, tvOS 12.0+, visionOS 1.0+, watchOS 5.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/network/nwlistener/serviceregistrationchange
source_url: 'https://developer.apple.com/documentation/network/nwlistener/serviceregistrationchange'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nwlistener/serviceregistrationchange.json'
content_hash: 'sha256:7e8b558ffa72de0d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Network](../../network.md) · [NWListener](../nwlistener.md)

# NWListener.ServiceRegistrationChange

<sub>Enumeration</sub>

Changes to how a network listener’s service is advertised.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
enum ServiceRegistrationChange
```

## Relationships

- **Conforms To**: [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Changes

- [NWListener.ServiceRegistrationChange.add(_:)](<serviceregistrationchange/add(__).md>) — The service is now advertising a new endpoint.
- [NWListener.ServiceRegistrationChange.remove(_:)](<serviceregistrationchange/remove(__).md>) — The service is no longer advertising a specific endpoint.

## See Also

### Advertising Bonjour Services

- [NSBonjourServices](../../bundleresources/information-property-list/nsbonjourservices.md) — Bonjour service types browsed by the app.
- [NSLocalNetworkUsageDescription](../../bundleresources/information-property-list/nslocalnetworkusagedescription.md) — A message that tells people why the app is requesting access to the local network.
- [service](service-swift.property.md) — A Bonjour service that advertises the listener on the local network.
- [Service](service-swift.struct.md) — A description used to advertise the Bonjour service that a listener provides.
- [serviceRegistrationUpdateHandler](serviceregistrationupdatehandler.md) — A handler that receives updates for the service endpoint being advertised.
