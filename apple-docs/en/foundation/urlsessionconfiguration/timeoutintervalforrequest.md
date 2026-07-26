---
title: timeoutIntervalForRequest
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/urlsessionconfiguration/timeoutintervalforrequest
source_url: 'https://developer.apple.com/documentation/foundation/urlsessionconfiguration/timeoutintervalforrequest'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlsessionconfiguration/timeoutintervalforrequest.json'
content_hash: 'sha256:c66b905376b42058'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URLSessionConfiguration](../urlsessionconfiguration.md)

# timeoutIntervalForRequest

<sub>Instance Property</sub>

The timeout interval to use when waiting for additional data.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var timeoutIntervalForRequest: TimeInterval { get set }
```

## Discussion

This property determines the request timeout interval for all tasks within sessions based on this configuration. The request timeout interval controls how long (in seconds) a task should wait for additional data to arrive before giving up. The timer associated with this value is reset whenever new data arrives. When the request timer reaches the specified interval without receiving any new data, it triggers a timeout.

The default value is `60`.

> [!important] Important
> Any upload or download tasks created by a background session are automatically retried if the original request fails due to a timeout. To configure how long an upload or download task should be allowed to be retried or transferred, use the [timeoutIntervalForResource](timeoutintervalforresource.md) property.

## See Also

### Setting general properties

- [identifier](identifier.md) — The background session identifier of the configuration object.
- [HTTPAdditionalHeaders](httpadditionalheaders.md) — A dictionary of additional headers to send with requests.
- [networkServiceType](networkservicetype.md) — The type of network service for all tasks within network sessions to enable Cellular Network Slicing.
- [allowsCellularAccess](allowscellularaccess.md) — A Boolean value that determines whether connections should be made over a cellular network.
- [timeoutIntervalForResource](timeoutintervalforresource.md) — The maximum amount of time that a resource request should be allowed to take.
- [sharedContainerIdentifier](sharedcontaineridentifier.md) — The identifier for the shared container into which files in background URL sessions should be downloaded.
- [waitsForConnectivity](waitsforconnectivity.md) — A Boolean value that indicates whether the session should wait for connectivity to become available, or fail immediately.
- [usesClassicLoadingMode](usesclassicloadingmode.md)
