---
title: NSURLRequest.NetworkServiceType.responsiveData
framework: Foundation
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, swift, swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsurlrequest/networkservicetype-swift.enum/responsivedata
source_url: 'https://developer.apple.com/documentation/foundation/nsurlrequest/networkservicetype-swift.enum/responsivedata'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsurlrequest/networkservicetype-swift.enum/responsivedata.json'
content_hash: 'sha256:522cf57463bad282'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [NSURLRequest](../../nsurlrequest.md) · [NetworkServiceType](../networkservicetype-swift.enum.md)

# NSURLRequest.NetworkServiceType.responsiveData

<sub>Case</sub>

A service type for medium-delay tolerant, elastic and inelastic flow, bursty, and long-lived connections.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case responsiveData
```

## Discussion

Use this service type for interactive situations where the user is anticipating a quick response, like instant messaging or completing a purchase.

## See Also

### Network service types

- [NSURLNetworkServiceTypeDefault](default.md) — A service type for standard network traffic.
- [NSURLNetworkServiceTypeVideo](video.md) — A service type for low-delay tolerant, very low-loss tolerant, inelastic flow, and constant packet rate connections.
- [NSURLNetworkServiceTypeBackground](background.md) — A service type for high-delay tolerant, high-loss tolerant, elastic flow, and variable size connections.
- [NSURLNetworkServiceTypeVoice](voice.md) — A service type for low-delay tolerant, very low-loss tolerant, inelastic flow, and constant packet rate connections.
- [NSURLNetworkServiceTypeCallSignaling](callsignaling.md) — A service for low-loss tolerant, inelastic flow, jitter tolerant, short but bursty rate, and variable size connections.
- [NSURLNetworkServiceTypeAVStreaming](avstreaming.md) — A service type for medium-delay tolerant, low-medium-loss tolerant, elastic flow, constant packet interval, and variable rate and size connections.
- [NSURLNetworkServiceTypeResponsiveAV](responsiveav.md) — A service type for low-delay tolerant, low-to-medium-loss tolerant, elastic flow, variable packet interval, rate, size responsive and time-sensitive connections.
- [NSURLNetworkServiceTypeVoIP](voip.md) — A service type for VoIP traffic. _(deprecated)_
