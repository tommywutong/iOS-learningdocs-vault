---
title: allowsConstrainedNetworkAccess
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsmutableurlrequest/allowsconstrainednetworkaccess
source_url: 'https://developer.apple.com/documentation/foundation/nsmutableurlrequest/allowsconstrainednetworkaccess'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsmutableurlrequest/allowsconstrainednetworkaccess.json'
content_hash: 'sha256:62471807e730eea1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSMutableURLRequest](../nsmutableurlrequest.md)

# allowsConstrainedNetworkAccess

<sub>Instance Property</sub>

A Boolean value that indicates whether connections may use the network when the user has specified Low Data Mode.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var allowsConstrainedNetworkAccess: Bool { get set }
```

## Discussion

In iOS 13 and later, users can set their device to use Low Data Mode as one of the Cellular Data Options in the Settings app. Users can turn on Low Data Mode to reduce your app’s network data usage. This property controls the request’s behavior when the user has turned Low Data Mode on. If there are no nonconstrained network interfaces available and the request’s [allowsConstrainedNetworkAccess](allowsconstrainednetworkaccess.md) property is [false](../../swift/false.md), any connection created from the request fails. In this case, the error provided when the connection fails has a [networkUnavailableReason](../urlerror/networkunavailablereason-swift.property.md) property whose value is [NSURLErrorNetworkUnavailableReasonConstrained](../nsurlerrornetworkunavailablereason/nsurlerrornetworkunavailablereasonconstrained.md).

Setting this property on a request overrides the [allowsConstrainedNetworkAccess](../urlsessionconfiguration/allowsconstrainednetworkaccess.md) property of [URLSessionConfiguration](../urlsessionconfiguration.md). For example, if the session configuration’s [allowsConstrainedNetworkAccess](../urlsessionconfiguration/allowsconstrainednetworkaccess.md) value is [false](../../swift/false.md), and you create a task from a request whose [allowsConstrainedNetworkAccess](allowsconstrainednetworkaccess.md) is [true](../../swift/true.md), the task treats the value as [true](../../swift/true.md).

Limit your app’s of use of constrained network access to user-initiated tasks, and put off discretionary tasks until a nonconstrained interface becomes available.

## See Also

### Supporting limited modes

- [allowsExpensiveNetworkAccess](allowsexpensivenetworkaccess.md) — A Boolean value that indicates whether connections may use a network interface that the system considers expensive.
