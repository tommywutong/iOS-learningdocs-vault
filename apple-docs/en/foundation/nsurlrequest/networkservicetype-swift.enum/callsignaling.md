---
title: NSURLRequest.NetworkServiceType.callSignaling
framework: Foundation
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.12+, tvOS 10.0+, visionOS 1.0+, watchOS 3.0+]
languages: [swift, swift, swift, swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsurlrequest/networkservicetype-swift.enum/callsignaling
source_url: 'https://developer.apple.com/documentation/foundation/nsurlrequest/networkservicetype-swift.enum/callsignaling'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsurlrequest/networkservicetype-swift.enum/callsignaling.json'
content_hash: 'sha256:78119d2597f031b0'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [NSURLRequest](../../nsurlrequest.md) · [NetworkServiceType](../networkservicetype-swift.enum.md)

# NSURLRequest.NetworkServiceType.callSignaling

<sub>Case</sub>

A service for low-loss tolerant, inelastic flow, jitter tolerant, short but bursty rate, and variable size connections.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case callSignaling
```

## Discussion

Use this for establishing, maintaining, and tearing down a VoIP call.

## See Also

### Network service types

- [NSURLNetworkServiceTypeDefault](default.md) — A service type for standard network traffic.
- [NSURLNetworkServiceTypeVideo](video.md) — A service type for low-delay tolerant, very low-loss tolerant, inelastic flow, and constant packet rate connections.
- [NSURLNetworkServiceTypeBackground](background.md) — A service type for high-delay tolerant, high-loss tolerant, elastic flow, and variable size connections.
- [NSURLNetworkServiceTypeVoice](voice.md) — A service type for low-delay tolerant, very low-loss tolerant, inelastic flow, and constant packet rate connections.
- [NSURLNetworkServiceTypeResponsiveData](responsivedata.md) — A service type for medium-delay tolerant, elastic and inelastic flow, bursty, and long-lived connections.
- [NSURLNetworkServiceTypeAVStreaming](avstreaming.md) — A service type for medium-delay tolerant, low-medium-loss tolerant, elastic flow, constant packet interval, and variable rate and size connections.
- [NSURLNetworkServiceTypeResponsiveAV](responsiveav.md) — A service type for low-delay tolerant, low-to-medium-loss tolerant, elastic flow, variable packet interval, rate, size responsive and time-sensitive connections.
- [NSURLNetworkServiceTypeVoIP](voip.md) — A service type for VoIP traffic. _(deprecated)_
