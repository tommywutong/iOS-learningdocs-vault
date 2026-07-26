---
title: URLSessionConfiguration.MultipathServiceType.aggregate
framework: Foundation
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/urlsessionconfiguration/multipathservicetype-swift.enum/aggregate
source_url: 'https://developer.apple.com/documentation/foundation/urlsessionconfiguration/multipathservicetype-swift.enum/aggregate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlsessionconfiguration/multipathservicetype-swift.enum/aggregate.json'
content_hash: 'sha256:ee88ee4be74bec81'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [URLSessionConfiguration](../../urlsessionconfiguration.md) · [MultipathServiceType](../multipathservicetype-swift.enum.md)

# URLSessionConfiguration.MultipathServiceType.aggregate

<sub>Case</sub>

A service that aggregates the capacities of other Multipath options in an attempt to increase throughput and minimize latency.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
case aggregate
```

## Discussion

This option is available only for experimentation. Specify it for connections that use cellular data. You must also set the [Multipath Entitlement](../../../bundleresources/entitlements/com.apple.developer.networking.multipath.md) in the Xcode Capabilities pane for your app.

To enable the aggregation mode, open the Settings app on your development iPhone and navigate to Developer, and then turn on Multipath Networking.

Multipath Aggregation requires an iOS device in Developer mode with a cellular connection running iOS 11.0 or later.

> [!note] Note
> Setting this option will use a considerable amount of cellular data.

## See Also

### Service types

- [NSURLSessionMultipathServiceTypeNone](none.md) — The default service type indicating that Multipath TCP should not be used.
- [NSURLSessionMultipathServiceTypeHandover](handover.md) — A Multipath TCP service that provides seamless handover between Wi-Fi and cellular in order to preserve the connection.
- [NSURLSessionMultipathServiceTypeInteractive](interactive.md) — A service whereby Multipath TCP attempts to use the lowest-latency interface.
