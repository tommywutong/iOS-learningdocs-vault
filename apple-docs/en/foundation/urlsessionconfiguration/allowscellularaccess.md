---
title: allowsCellularAccess
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/urlsessionconfiguration/allowscellularaccess
source_url: 'https://developer.apple.com/documentation/foundation/urlsessionconfiguration/allowscellularaccess'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlsessionconfiguration/allowscellularaccess.json'
content_hash: 'sha256:d00d609ac07e57f7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URLSessionConfiguration](../urlsessionconfiguration.md)

# allowsCellularAccess

<sub>Instance Property</sub>

A Boolean value that determines whether connections should be made over a cellular network.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var allowsCellularAccess: Bool { get set }
```

## Discussion

This property controls whether tasks in sessions based on this session configuration are allowed to make connections over a cellular network.

The default value is [true](../../swift/true.md).

For more information, read [Restrict Cellular Networking Correctly](https://developer.apple.com/library/archive/documentation/NetworkingInternetWeb/Conceptual/NetworkingOverview/Platform-SpecificNetworkingTechnologies/Platform-SpecificNetworkingTechnologies.html#//apple_ref/doc/uid/TP40010220-CH212-SW9).

## See Also

### Setting general properties

- [identifier](identifier.md) — The background session identifier of the configuration object.
- [HTTPAdditionalHeaders](httpadditionalheaders.md) — A dictionary of additional headers to send with requests.
- [networkServiceType](networkservicetype.md) — The type of network service for all tasks within network sessions to enable Cellular Network Slicing.
- [timeoutIntervalForRequest](timeoutintervalforrequest.md) — The timeout interval to use when waiting for additional data.
- [timeoutIntervalForResource](timeoutintervalforresource.md) — The maximum amount of time that a resource request should be allowed to take.
- [sharedContainerIdentifier](sharedcontaineridentifier.md) — The identifier for the shared container into which files in background URL sessions should be downloaded.
- [waitsForConnectivity](waitsforconnectivity.md) — A Boolean value that indicates whether the session should wait for connectivity to become available, or fail immediately.
- [usesClassicLoadingMode](usesclassicloadingmode.md)
