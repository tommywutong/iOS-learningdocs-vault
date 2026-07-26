---
title: waitsForConnectivity
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 11.0+, visionOS 1.0+, watchOS 4.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/urlsessionconfiguration/waitsforconnectivity
source_url: 'https://developer.apple.com/documentation/foundation/urlsessionconfiguration/waitsforconnectivity'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlsessionconfiguration/waitsforconnectivity.json'
content_hash: 'sha256:d636765208bf8fdf'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URLSessionConfiguration](../urlsessionconfiguration.md)

# waitsForConnectivity

<sub>Instance Property</sub>

A Boolean value that indicates whether the session should wait for connectivity to become available, or fail immediately.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var waitsForConnectivity: Bool { get set }
```

## Discussion

Connectivity might be temporarily unavailable for several reasons. For example, a device might only have a cellular connection when [allowsCellularAccess](allowscellularaccess.md) is set to `false`, or the device might require a VPN connection but none is available. If the value of this property is `true` and sufficient connectivity is unavailable, the session calls the [- URLSession:taskIsWaitingForConnectivity:](<../urlsessiontaskdelegate/urlsession(__taskiswaitingforconnectivity_).md>) method of [URLSessionTaskDelegate](../urlsessiontaskdelegate.md) and waits for connectivity. When connectivity becomes available, the task begins its work and ultimately calls the delegate or completion handler as usual.

If the value of the property is `false` and connectivity is unavailable, the connection fails immediately with an error, such as [NSURLErrorNotConnectedToInternet](../nsurlerrornotconnectedtointernet-swift.var.md).

This property is relevant only during the establishment of a connection. If a connection is established and then drops, the completion handler or delegate receives an error, such as [NSURLErrorNetworkConnectionLost](../nsurlerrornetworkconnectionlost-swift.var.md). For help dealing with dropped connections, see [Handling “The network connection was lost” Errors](https://developer.apple.com/library/archive/qa/qa1941/_index.html#//apple_ref/doc/uid/DTS40017602).

This property is ignored by background sessions, which always wait for connectivity.

## See Also

### Setting general properties

- [identifier](identifier.md) — The background session identifier of the configuration object.
- [HTTPAdditionalHeaders](httpadditionalheaders.md) — A dictionary of additional headers to send with requests.
- [networkServiceType](networkservicetype.md) — The type of network service for all tasks within network sessions to enable Cellular Network Slicing.
- [allowsCellularAccess](allowscellularaccess.md) — A Boolean value that determines whether connections should be made over a cellular network.
- [timeoutIntervalForRequest](timeoutintervalforrequest.md) — The timeout interval to use when waiting for additional data.
- [timeoutIntervalForResource](timeoutintervalforresource.md) — The maximum amount of time that a resource request should be allowed to take.
- [sharedContainerIdentifier](sharedcontaineridentifier.md) — The identifier for the shared container into which files in background URL sessions should be downloaded.
- [usesClassicLoadingMode](usesclassicloadingmode.md)
