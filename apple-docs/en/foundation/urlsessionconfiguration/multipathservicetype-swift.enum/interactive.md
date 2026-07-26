---
title: URLSessionConfiguration.MultipathServiceType.interactive
framework: Foundation
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/urlsessionconfiguration/multipathservicetype-swift.enum/interactive
source_url: 'https://developer.apple.com/documentation/foundation/urlsessionconfiguration/multipathservicetype-swift.enum/interactive'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlsessionconfiguration/multipathservicetype-swift.enum/interactive.json'
content_hash: 'sha256:af231595f6e02bd4'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [URLSessionConfiguration](../../urlsessionconfiguration.md) · [MultipathServiceType](../multipathservicetype-swift.enum.md)

# URLSessionConfiguration.MultipathServiceType.interactive

<sub>Case</sub>

A service whereby Multipath TCP attempts to use the lowest-latency interface.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
case interactive
```

## Discussion

Specify this option for latency-sensitive, low-volume connections that might use cellular data. You must also set the [Multipath Entitlement](../../../bundleresources/entitlements/com.apple.developer.networking.multipath.md) in the Xcode Capabilities pane for your app.

## See Also

### Service types

- [NSURLSessionMultipathServiceTypeNone](none.md) — The default service type indicating that Multipath TCP should not be used.
- [NSURLSessionMultipathServiceTypeHandover](handover.md) — A Multipath TCP service that provides seamless handover between Wi-Fi and cellular in order to preserve the connection.
- [NSURLSessionMultipathServiceTypeAggregate](aggregate.md) — A service that aggregates the capacities of other Multipath options in an attempt to increase throughput and minimize latency.
