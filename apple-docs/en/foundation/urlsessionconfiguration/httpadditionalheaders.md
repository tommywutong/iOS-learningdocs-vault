---
title: httpAdditionalHeaders
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/urlsessionconfiguration/httpadditionalheaders
source_url: 'https://developer.apple.com/documentation/foundation/urlsessionconfiguration/httpadditionalheaders'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlsessionconfiguration/httpadditionalheaders.json'
content_hash: 'sha256:70571421bde49d50'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URLSessionConfiguration](../urlsessionconfiguration.md)

# httpAdditionalHeaders

<sub>Instance Property</sub>

A dictionary of additional headers to send with requests.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var httpAdditionalHeaders: [AnyHashable : Any]? { get set }
```

## Discussion

This property specifies additional headers that are added to all tasks within sessions based on this configuration. For example, you might set the `User-Agent` header so that it is automatically included in every request your app makes through sessions based on this configuration.

An [URLSession](../urlsession.md) object is designed to handle various aspects of the HTTP protocol for you. As a result, you should not modify the following headers:

- `Authorization`
- `Connection`
- `Host`
- `Proxy-Authenticate`
- `Proxy-Authorization`
- `WWW-Authenticate`

Additionally, if the length of your upload body data can be determined automatically—for example, if you provide the body content with an [NSData](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/PropertyLists/OldStylePlists/OldStylePLists.html#//apple_ref/doc/uid/20001012-47169) object—the value of `Content-Length` is set for you.

If the same header appears in both this array and the request object (where applicable), the request object’s value takes precedence.

The default value is an empty array.

## See Also

### Setting general properties

- [identifier](identifier.md) — The background session identifier of the configuration object.
- [networkServiceType](networkservicetype.md) — The type of network service for all tasks within network sessions to enable Cellular Network Slicing.
- [allowsCellularAccess](allowscellularaccess.md) — A Boolean value that determines whether connections should be made over a cellular network.
- [timeoutIntervalForRequest](timeoutintervalforrequest.md) — The timeout interval to use when waiting for additional data.
- [timeoutIntervalForResource](timeoutintervalforresource.md) — The maximum amount of time that a resource request should be allowed to take.
- [sharedContainerIdentifier](sharedcontaineridentifier.md) — The identifier for the shared container into which files in background URL sessions should be downloaded.
- [waitsForConnectivity](waitsforconnectivity.md) — A Boolean value that indicates whether the session should wait for connectivity to become available, or fail immediately.
- [usesClassicLoadingMode](usesclassicloadingmode.md)
