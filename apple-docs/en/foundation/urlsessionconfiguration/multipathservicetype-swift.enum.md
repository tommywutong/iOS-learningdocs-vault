---
title: URLSessionConfiguration.MultipathServiceType
framework: Foundation
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/urlsessionconfiguration/multipathservicetype-swift.enum
source_url: 'https://developer.apple.com/documentation/foundation/urlsessionconfiguration/multipathservicetype-swift.enum'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlsessionconfiguration/multipathservicetype-swift.enum.json'
content_hash: 'sha256:42ce66d584d9c1c7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URLSessionConfiguration](../urlsessionconfiguration.md)

# URLSessionConfiguration.MultipathServiceType

<sub>Enumeration</sub>

Constants that specify the type of service that Multipath TCP uses.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
enum MultipathServiceType
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Service types

- [NSURLSessionMultipathServiceTypeNone](multipathservicetype-swift.enum/none.md) — The default service type indicating that Multipath TCP should not be used.
- [NSURLSessionMultipathServiceTypeHandover](multipathservicetype-swift.enum/handover.md) — A Multipath TCP service that provides seamless handover between Wi-Fi and cellular in order to preserve the connection.
- [NSURLSessionMultipathServiceTypeInteractive](multipathservicetype-swift.enum/interactive.md) — A service whereby Multipath TCP attempts to use the lowest-latency interface.
- [NSURLSessionMultipathServiceTypeAggregate](multipathservicetype-swift.enum/aggregate.md) — A service that aggregates the capacities of other Multipath options in an attempt to increase throughput and minimize latency.

### Initializers

- [init(rawValue:)](<multipathservicetype-swift.enum/init(rawvalue_).md>)

## See Also

### Supporting Multipath TCP

- [Improving network reliability using Multipath TCP](../improving-network-reliability-using-multipath-tcp.md) — Use the available radios in iOS devices to improve your app’s network reliability and performance.
- [multipathServiceType](multipathservicetype-swift.property.md) — A service type that specifies the Multipath TCP connection policy for transmitting data over Wi-Fi and cellular interfaces.
- [Multipath Entitlement](../../bundleresources/entitlements/com.apple.developer.networking.multipath.md) — A Boolean value indicating whether your app may use Multipath protocols to seamlessly transition between Wi-Fi and cellular networks.
