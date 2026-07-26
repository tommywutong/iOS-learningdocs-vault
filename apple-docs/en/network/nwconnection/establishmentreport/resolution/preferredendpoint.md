---
title: preferredEndpoint
framework: Network
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/network/nwconnection/establishmentreport/resolution/preferredendpoint
source_url: 'https://developer.apple.com/documentation/network/nwconnection/establishmentreport/resolution/preferredendpoint'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nwconnection/establishmentreport/resolution/preferredendpoint.json'
content_hash: 'sha256:4fc8f5d91880564b'
translated: false
---

> Navigation: [Technologies](../../../../technologies.md) · [Network](../../../../network.md) · [NWConnection](../../../nwconnection.md) · [EstablishmentReport](../../establishmentreport.md) · [Resolution](../resolution.md)

# preferredEndpoint

<sub>Instance Property</sub>

The resolved endpoint that the connection used for its first connection attempt.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let preferredEndpoint: NWEndpoint
```

## See Also

### Examining Resolved Endpoints

- [successfulEndpoint](successfulendpoint.md) — The resolved endpoint that led to the established connection.
- [endpointCount](endpointcount.md) — The number of endpoints resolved in this step.
