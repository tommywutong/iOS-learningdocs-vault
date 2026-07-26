---
title: multipathServiceType
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/urlsessionconfiguration/multipathservicetype-swift.property
source_url: 'https://developer.apple.com/documentation/foundation/urlsessionconfiguration/multipathservicetype-swift.property'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlsessionconfiguration/multipathservicetype-swift.property.json'
content_hash: 'sha256:4230cafa651ff181'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URLSessionConfiguration](../urlsessionconfiguration.md)

# multipathServiceType

<sub>Instance Property</sub>

A service type that specifies the Multipath TCP connection policy for transmitting data over Wi-Fi and cellular interfaces.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var multipathServiceType: URLSessionConfiguration.MultipathServiceType { get set }
```

## Discussion

Multipath TCP, defined by the IETF in [RFC 6824](https://tools.ietf.org/html/rfc6824), is an extension to TCP that permits multiple interfaces to transmit a single data stream. This capability allows a seamless handover from Wi-Fi to cellular, aimed at making both interfaces more efficient and improving the user experience.

The [multipathServiceType](multipathservicetype-swift.property.md) property defines which policy the Multipath TCP stack uses to schedule traffic across Wi-Fi and cellular interfaces. The default value is `none`, meaning Multipath TCP is disabled. You can also select handover mode, which provides seamless handover between Wi-Fi and cellular.

Multipath TCP requires server support. Resources for Linux-based systems are available at [https://mptcp.dev](https://mptcp.dev).

## See Also

### Supporting Multipath TCP

- [Improving network reliability using Multipath TCP](../improving-network-reliability-using-multipath-tcp.md) — Use the available radios in iOS devices to improve your app’s network reliability and performance.
- [MultipathServiceType](multipathservicetype-swift.enum.md) — Constants that specify the type of service that Multipath TCP uses.
- [Multipath Entitlement](../../bundleresources/entitlements/com.apple.developer.networking.multipath.md) — A Boolean value indicating whether your app may use Multipath protocols to seamlessly transition between Wi-Fi and cellular networks.
