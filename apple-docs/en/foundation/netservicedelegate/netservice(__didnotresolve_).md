---
title: 'netService(_:didNotResolve:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.2+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/netservicedelegate/netservice(_:didnotresolve:)'
source_url: 'https://developer.apple.com/documentation/foundation/netservicedelegate/netservice(_:didnotresolve:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/netservicedelegate/netservice%28_%3Adidnotresolve%3A%29.json'
content_hash: 'sha256:50f15a2bc41a2261'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NetServiceDelegate](../netservicedelegate.md)

# netService(_:didNotResolve:)

<sub>Instance Method</sub>

Informs the delegate that an error occurred during resolution of a given service.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
optional func netService(_ sender: NetService, didNotResolve errorDict: [String : NSNumber])
```

## Parameters

- `sender` — The service that did not resolve.

- `errorDict` — A dictionary containing information about the problem. The dictionary contains the keys [NSNetServicesErrorCode](../netservice/errorcode-swift.type.property.md) and [NSNetServicesErrorDomain](../netservice/errordomain.md).

## Discussion

Clients may try to resolve again upon receiving this error. For example, a DNS rotary may yield different IP addresses on different resolution requests. A common error condition is that no addresses were resolved during the timeout period specified in [- resolveWithTimeout:](<../netservice/resolve(withtimeout_).md>).

## See Also

### Using Network Services

- [- netServiceWillPublish:](<netservicewillpublish(__).md>) — Notifies the delegate that the network is ready to publish the service.
- [- netService:didNotPublish:](<netservice(__didnotpublish_).md>) — Notifies the delegate that a service could not be published.
- [- netServiceDidPublish:](<netservicedidpublish(__).md>) — Notifies the delegate that a service was successfully published.
- [- netServiceWillResolve:](<netservicewillresolve(__).md>) — Notifies the delegate that the network is ready to resolve the service.
- [- netServiceDidResolveAddress:](<netservicedidresolveaddress(__).md>) — Informs the delegate that the address for a given service was resolved.
- [- netService:didUpdateTXTRecordData:](<netservice(__didupdatetxtrecord_).md>) — Notifies the delegate that the TXT record for a given service has been updated.
- [- netServiceDidStop:](<netservicedidstop(__).md>) — Informs the delegate that a [- publish](<../netservice/publish().md>) or [- resolveWithTimeout:](<../netservice/resolve(withtimeout_).md>) request was stopped.
