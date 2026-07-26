---
title: NSURLErrorNetworkUnavailableReasonExpensive
framework: Foundation
symbol_kind: case
role: symbol
role_heading: Enumeration Case
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsurlerrornetworkunavailablereason/nsurlerrornetworkunavailablereasonexpensive
source_url: 'https://developer.apple.com/documentation/foundation/nsurlerrornetworkunavailablereason/nsurlerrornetworkunavailablereasonexpensive'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsurlerrornetworkunavailablereason/nsurlerrornetworkunavailablereasonexpensive.json'
content_hash: 'sha256:5cda6355dce2f99e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSURLErrorNetworkUnavailableReason](../nsurlerrornetworkunavailablereason.md)

# NSURLErrorNetworkUnavailableReasonExpensive

<sub>Enumeration Case</sub>

A reason that indicates network is unavailable because the system marked the interface as expensive.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
NSURLErrorNetworkUnavailableReasonExpensive
```

## Discussion

The system determines what constitutes “expensive” based on the nature of the network interface and other factors. iOS 13 considers most cellular networks and personal hotspots expensive, but this may change in the future.

This reason occurs when the following conditions are true:

- The only available network interfaces are expensive.
- The [URLSessionConfiguration](../urlsessionconfiguration.md) property [allowsExpensiveNetworkAccess](../urlsessionconfiguration/allowsexpensivenetworkaccess.md) is [false](../../swift/false.md).

## See Also

### Unavailability reasons

- [NSURLErrorNetworkUnavailableReasonCellular](nsurlerrornetworkunavailablereasoncellular.md) — A reason that indicates network is unavailable because the interface is cellular and cellular network is disabled.
- [NSURLErrorNetworkUnavailableReasonConstrained](nsurlerrornetworkunavailablereasonconstrained.md) — A reason that indicates network is unavailable because the user enabled “Low Data Mode” in the Settings app.
