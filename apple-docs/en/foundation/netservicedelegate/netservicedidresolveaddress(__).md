---
title: 'netServiceDidResolveAddress(_:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.2+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/netservicedelegate/netservicedidresolveaddress(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/netservicedelegate/netservicedidresolveaddress(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/netservicedelegate/netservicedidresolveaddress%28_%3A%29.json'
content_hash: 'sha256:db628e6e60888505'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NetServiceDelegate](../netservicedelegate.md)

# netServiceDidResolveAddress(_:)

<sub>Instance Method</sub>

Informs the delegate that the address for a given service was resolved.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
optional func netServiceDidResolveAddress(_ sender: NetService)
```

## Parameters

- `sender` — The service that was resolved.

## Discussion

The delegate can use the [addresses](../netservice/addresses.md) method to retrieve the service’s address. If the delegate needs only one address, it can stop the resolution process using [- stop](<../netservice/stop().md>). Otherwise, the resolution will continue until the timeout specified in [- resolveWithTimeout:](<../netservice/resolve(withtimeout_).md>) is reached.

## See Also

### Related Documentation

- [addresses](../netservice/addresses.md) — A read-only array containing `NSData` objects, each of which contains a socket address for the service. _(deprecated)_

### Using Network Services

- [- netServiceWillPublish:](<netservicewillpublish(__).md>) — Notifies the delegate that the network is ready to publish the service.
- [- netService:didNotPublish:](<netservice(__didnotpublish_).md>) — Notifies the delegate that a service could not be published.
- [- netServiceDidPublish:](<netservicedidpublish(__).md>) — Notifies the delegate that a service was successfully published.
- [- netServiceWillResolve:](<netservicewillresolve(__).md>) — Notifies the delegate that the network is ready to resolve the service.
- [- netService:didNotResolve:](<netservice(__didnotresolve_).md>) — Informs the delegate that an error occurred during resolution of a given service.
- [- netService:didUpdateTXTRecordData:](<netservice(__didupdatetxtrecord_).md>) — Notifies the delegate that the TXT record for a given service has been updated.
- [- netServiceDidStop:](<netservicedidstop(__).md>) — Informs the delegate that a [- publish](<../netservice/publish().md>) or [- resolveWithTimeout:](<../netservice/resolve(withtimeout_).md>) request was stopped.
