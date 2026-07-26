---
title: networkServiceType
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsurlrequest/networkservicetype-swift.property
source_url: 'https://developer.apple.com/documentation/foundation/nsurlrequest/networkservicetype-swift.property'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsurlrequest/networkservicetype-swift.property.json'
content_hash: 'sha256:e054d3d3e46662ba'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSURLRequest](../nsurlrequest.md)

# networkServiceType

<sub>Instance Property</sub>

The network service type of the request.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var networkServiceType: NSURLRequest.NetworkServiceType { get }
```

## Discussion

The network service type provides a hint to the operating system about what the underlying traffic is used for. This hint enhances the system’s ability to prioritize traffic, determine how quickly it needs to wake up the cellular or Wi-Fi radio, and so on. By providing accurate information, you improve the ability of the system to optimally balance battery life, performance, and other considerations.

## See Also

### Related Documentation

- [networkServiceType](../nsmutableurlrequest/networkservicetype.md) — The network service type of the connection.

### Accessing the service type

- [NetworkServiceType](networkservicetype-swift.enum.md) — Constants that specify how a request uses network resources.
