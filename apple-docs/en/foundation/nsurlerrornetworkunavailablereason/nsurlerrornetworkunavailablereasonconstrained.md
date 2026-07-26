---
title: NSURLErrorNetworkUnavailableReasonConstrained
framework: Foundation
symbol_kind: case
role: symbol
role_heading: Enumeration Case
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsurlerrornetworkunavailablereason/nsurlerrornetworkunavailablereasonconstrained
source_url: 'https://developer.apple.com/documentation/foundation/nsurlerrornetworkunavailablereason/nsurlerrornetworkunavailablereasonconstrained'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsurlerrornetworkunavailablereason/nsurlerrornetworkunavailablereasonconstrained.json'
content_hash: 'sha256:7d9efa694858e46d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSURLErrorNetworkUnavailableReason](../nsurlerrornetworkunavailablereason.md)

# NSURLErrorNetworkUnavailableReasonConstrained

<sub>Enumeration Case</sub>

A reason that indicates network is unavailable because the user enabled “Low Data Mode” in the Settings app.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
NSURLErrorNetworkUnavailableReasonConstrained
```

## Discussion

This reason occurs when the following conditions are true:

- The only available network is cellular.
- The user has enabled “Low Data Mode” option in the Cellular Data Options section of the Settings app.
- The [URLSessionConfiguration](../urlsessionconfiguration.md) property [allowsConstrainedNetworkAccess](../urlsessionconfiguration/allowsconstrainednetworkaccess.md) is [false](../../swift/false.md).

## See Also

### Unavailability reasons

- [NSURLErrorNetworkUnavailableReasonCellular](nsurlerrornetworkunavailablereasoncellular.md) — A reason that indicates network is unavailable because the interface is cellular and cellular network is disabled.
- [NSURLErrorNetworkUnavailableReasonExpensive](nsurlerrornetworkunavailablereasonexpensive.md) — A reason that indicates network is unavailable because the system marked the interface as expensive.
