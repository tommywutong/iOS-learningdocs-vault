---
title: NWParameters.ServiceClass.background
framework: Network
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 12.0+, macOS 10.14+, tvOS 12.0+, visionOS 1.0+, watchOS 5.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/network/nwparameters/serviceclass-swift.enum/background
source_url: 'https://developer.apple.com/documentation/network/nwparameters/serviceclass-swift.enum/background'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nwparameters/serviceclass-swift.enum/background.json'
content_hash: 'sha256:daaf0beb0aa2e03b'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Network](../../../network.md) · [NWParameters](../../nwparameters.md) · [ServiceClass](../serviceclass-swift.enum.md)

# NWParameters.ServiceClass.background

<sub>Case</sub>

A service type for high-delay tolerant, high-loss tolerant, elastic flow, and variable size connections.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case background
```

## Discussion

Use this service type when, for example, you’re managing traffic that prefetches content and makes it available when the person chooses to view it.

## See Also

### Service Classes

- [NWParameters.ServiceClass.bestEffort](besteffort.md) — The default service type.
- [NWParameters.ServiceClass.interactiveVideo](interactivevideo.md) — A service type for low-delay tolerant, very low-loss tolerant, inelastic flow, and constant packet rate connections.
- [NWParameters.ServiceClass.interactiveVoice](interactivevoice.md) — A service type for low-delay tolerant, very low-loss tolerant, inelastic flow, and constant packet rate connections.
- [NWParameters.ServiceClass.responsiveData](responsivedata.md) — A service type for medium-delay tolerant, inelastic flow, and bursty connections.
- [NWParameters.ServiceClass.signaling](signaling.md) — A service type for low-loss tolerant, inelastic flow, jitter tolerant, bursty but short rate, and variable size connections.
