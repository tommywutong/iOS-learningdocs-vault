---
title: NSURLRequest.NetworkServiceType.background
framework: Foundation
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, swift, swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsurlrequest/networkservicetype-swift.enum/background
source_url: 'https://developer.apple.com/documentation/foundation/nsurlrequest/networkservicetype-swift.enum/background'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsurlrequest/networkservicetype-swift.enum/background.json'
content_hash: 'sha256:b8a4e2f714443e0f'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [NSURLRequest](../../nsurlrequest.md) · [NetworkServiceType](../networkservicetype-swift.enum.md)

# NSURLRequest.NetworkServiceType.background

<sub>Case</sub>

A service type for high-delay tolerant, high-loss tolerant, elastic flow, and variable size connections.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case background
```

## Discussion

An example of this service type is prefetching content so that it’s available when the user chooses to view it.

## See Also

### Network service types

- [NSURLNetworkServiceTypeDefault](default.md) — A service type for standard network traffic.
- [NSURLNetworkServiceTypeVideo](video.md) — A service type for low-delay tolerant, very low-loss tolerant, inelastic flow, and constant packet rate connections.
- [NSURLNetworkServiceTypeVoice](voice.md) — A service type for low-delay tolerant, very low-loss tolerant, inelastic flow, and constant packet rate connections.
- [NSURLNetworkServiceTypeCallSignaling](callsignaling.md) — A service for low-loss tolerant, inelastic flow, jitter tolerant, short but bursty rate, and variable size connections.
- [NSURLNetworkServiceTypeResponsiveData](responsivedata.md) — A service type for medium-delay tolerant, elastic and inelastic flow, bursty, and long-lived connections.
- [NSURLNetworkServiceTypeAVStreaming](avstreaming.md) — A service type for medium-delay tolerant, low-medium-loss tolerant, elastic flow, constant packet interval, and variable rate and size connections.
- [NSURLNetworkServiceTypeResponsiveAV](responsiveav.md) — A service type for low-delay tolerant, low-to-medium-loss tolerant, elastic flow, variable packet interval, rate, size responsive and time-sensitive connections.
- [NSURLNetworkServiceTypeVoIP](voip.md) — A service type for VoIP traffic. _(deprecated)_
