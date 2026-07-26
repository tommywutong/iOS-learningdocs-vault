---
title: NSURLRequest.NetworkServiceType.voip
framework: Foundation
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 4.0+（13.0 起废弃）, iPadOS 4.0+（13.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）, macOS 10.7+（10.15 起废弃）, tvOS 9.0+（13.0 起废弃）, visionOS 1.0+（1.0 起废弃）, watchOS 2.0+（6.0 起废弃）]
languages: [swift, swift, swift, swift, swift, occ, occ]
beta: false
deprecated: true
doc_path: /documentation/foundation/nsurlrequest/networkservicetype-swift.enum/voip
source_url: 'https://developer.apple.com/documentation/foundation/nsurlrequest/networkservicetype-swift.enum/voip'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsurlrequest/networkservicetype-swift.enum/voip.json'
content_hash: 'sha256:989aedf6c053920a'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [NSURLRequest](../../nsurlrequest.md) · [NetworkServiceType](../networkservicetype-swift.enum.md)

# NSURLRequest.NetworkServiceType.voip

<sub>Case</sub>

A service type for VoIP traffic.

> [!warning] Deprecated
> This service type has been depreciated, use service type [NSURLNetworkServiceTypeVoice](voice.md) instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case voip
```

## Discussion

With the VoIP service type, the kernel continues to listen for incoming traffic while your app is in the background, then wakes up your app whenever new data arrives. Set this _only_ for connections that are communicate with a VoIP service.

## See Also

### Network service types

- [NSURLNetworkServiceTypeDefault](default.md) — A service type for standard network traffic.
- [NSURLNetworkServiceTypeVideo](video.md) — A service type for low-delay tolerant, very low-loss tolerant, inelastic flow, and constant packet rate connections.
- [NSURLNetworkServiceTypeBackground](background.md) — A service type for high-delay tolerant, high-loss tolerant, elastic flow, and variable size connections.
- [NSURLNetworkServiceTypeVoice](voice.md) — A service type for low-delay tolerant, very low-loss tolerant, inelastic flow, and constant packet rate connections.
- [NSURLNetworkServiceTypeCallSignaling](callsignaling.md) — A service for low-loss tolerant, inelastic flow, jitter tolerant, short but bursty rate, and variable size connections.
- [NSURLNetworkServiceTypeResponsiveData](responsivedata.md) — A service type for medium-delay tolerant, elastic and inelastic flow, bursty, and long-lived connections.
- [NSURLNetworkServiceTypeAVStreaming](avstreaming.md) — A service type for medium-delay tolerant, low-medium-loss tolerant, elastic flow, constant packet interval, and variable rate and size connections.
- [NSURLNetworkServiceTypeResponsiveAV](responsiveav.md) — A service type for low-delay tolerant, low-to-medium-loss tolerant, elastic flow, variable packet interval, rate, size responsive and time-sensitive connections.
