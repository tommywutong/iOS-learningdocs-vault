---
title: NSURLRequest.NetworkServiceType
framework: Foundation
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, swift, swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsurlrequest/networkservicetype-swift.enum
source_url: 'https://developer.apple.com/documentation/foundation/nsurlrequest/networkservicetype-swift.enum'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsurlrequest/networkservicetype-swift.enum.json'
content_hash: 'sha256:f5b20417a7e6c662'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSURLRequest](../nsurlrequest.md)

# NSURLRequest.NetworkServiceType

<sub>Enumeration</sub>

Constants that specify how a request uses network resources.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
enum NetworkServiceType
```

## Overview

The network service type provides a hint to the operating system about the nature and use of the underlying traffic. This hint enhances the system’s ability to prioritize traffic, determine how quickly it needs to wake up the cellular or Wi-Fi radio, and so on. By providing accurate information, you improve the system’s ability to optimally balance battery life, performance, and other considerations.

Make connections using the [NSURLNetworkServiceTypeDefault](networkservicetype-swift.enum/default.md) service type.

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Network service types

- [NSURLNetworkServiceTypeDefault](networkservicetype-swift.enum/default.md) — A service type for standard network traffic.
- [NSURLNetworkServiceTypeVideo](networkservicetype-swift.enum/video.md) — A service type for low-delay tolerant, very low-loss tolerant, inelastic flow, and constant packet rate connections.
- [NSURLNetworkServiceTypeBackground](networkservicetype-swift.enum/background.md) — A service type for high-delay tolerant, high-loss tolerant, elastic flow, and variable size connections.
- [NSURLNetworkServiceTypeVoice](networkservicetype-swift.enum/voice.md) — A service type for low-delay tolerant, very low-loss tolerant, inelastic flow, and constant packet rate connections.
- [NSURLNetworkServiceTypeCallSignaling](networkservicetype-swift.enum/callsignaling.md) — A service for low-loss tolerant, inelastic flow, jitter tolerant, short but bursty rate, and variable size connections.
- [NSURLNetworkServiceTypeResponsiveData](networkservicetype-swift.enum/responsivedata.md) — A service type for medium-delay tolerant, elastic and inelastic flow, bursty, and long-lived connections.
- [NSURLNetworkServiceTypeAVStreaming](networkservicetype-swift.enum/avstreaming.md) — A service type for medium-delay tolerant, low-medium-loss tolerant, elastic flow, constant packet interval, and variable rate and size connections.
- [NSURLNetworkServiceTypeResponsiveAV](networkservicetype-swift.enum/responsiveav.md) — A service type for low-delay tolerant, low-to-medium-loss tolerant, elastic flow, variable packet interval, rate, size responsive and time-sensitive connections.
- [NSURLNetworkServiceTypeVoIP](networkservicetype-swift.enum/voip.md) — A service type for VoIP traffic. _(deprecated)_

### Initializers

- [init(rawValue:)](<networkservicetype-swift.enum/init(rawvalue_).md>)

## See Also

### Accessing the service type

- [networkServiceType](../nsmutableurlrequest/networkservicetype.md) — The network service type of the connection.
