---
title: identifier
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/urlsessionconfiguration/identifier
source_url: 'https://developer.apple.com/documentation/foundation/urlsessionconfiguration/identifier'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlsessionconfiguration/identifier.json'
content_hash: 'sha256:5745b25dd4be2321'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URLSessionConfiguration](../urlsessionconfiguration.md)

# identifier

<sub>Instance Property</sub>

The background session identifier of the configuration object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var identifier: String? { get }
```

## Discussion

The value of this property is set only when you use the [+ backgroundSessionConfigurationWithIdentifier:](<background(withidentifier_).md>) method to create the configuration object. The string uniquely identifies a background session object. In iOS, you use this string in cases where the app was terminated while transfers were occurring in the background. When the app relaunches, it uses the string to recreate the configuration and session objects associated with the transfers.

## See Also

### Setting general properties

- [HTTPAdditionalHeaders](httpadditionalheaders.md) — A dictionary of additional headers to send with requests.
- [networkServiceType](networkservicetype.md) — The type of network service for all tasks within network sessions to enable Cellular Network Slicing.
- [allowsCellularAccess](allowscellularaccess.md) — A Boolean value that determines whether connections should be made over a cellular network.
- [timeoutIntervalForRequest](timeoutintervalforrequest.md) — The timeout interval to use when waiting for additional data.
- [timeoutIntervalForResource](timeoutintervalforresource.md) — The maximum amount of time that a resource request should be allowed to take.
- [sharedContainerIdentifier](sharedcontaineridentifier.md) — The identifier for the shared container into which files in background URL sessions should be downloaded.
- [waitsForConnectivity](waitsforconnectivity.md) — A Boolean value that indicates whether the session should wait for connectivity to become available, or fail immediately.
- [usesClassicLoadingMode](usesclassicloadingmode.md)
