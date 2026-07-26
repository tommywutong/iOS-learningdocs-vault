---
title: networkServiceType
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/urlrequest/networkservicetype-swift.property
source_url: 'https://developer.apple.com/documentation/foundation/urlrequest/networkservicetype-swift.property'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlrequest/networkservicetype-swift.property.json'
content_hash: 'sha256:ad8a311daf6279b7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URLRequest](../urlrequest.md)

# networkServiceType

<sub>Instance Property</sub>

The type of network service for all tasks within network sessions to enable Cellular Network Slicing.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var networkServiceType: URLRequest.NetworkServiceType { get set }
```

## Discussion

There are two steps to enable Cellular Network Slicing:

- Set the entitlements in your property list for [5G Network Slicing App Category](../../bundleresources/entitlements/com.apple.developer.networking.slicing.appcategory.md) and [5G Network Slicing Traffic Category](../../bundleresources/entitlements/com.apple.developer.networking.slicing.trafficcategory.md). If you don’t entitle your app by specifying both these entitlements, your apps network connections won’t be using Cellular Network Slicing, even if supported by the carrier.
- At the time of network flow creation, set this to the appropriate [NetworkServiceType](../nsurlrequest/networkservicetype-swift.enum.md) for your application type.

## See Also

### Accessing the service type

- [NetworkServiceType](networkservicetype-swift.typealias.md) — An alias for the network service type.
- [NetworkServiceType](../nsurlrequest/networkservicetype-swift.enum.md) — Constants that specify how a request uses network resources.
