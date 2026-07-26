---
title: 'netService(_:didUpdateTXTRecord:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.2+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/netservicedelegate/netservice(_:didupdatetxtrecord:)'
source_url: 'https://developer.apple.com/documentation/foundation/netservicedelegate/netservice(_:didupdatetxtrecord:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/netservicedelegate/netservice%28_%3Adidupdatetxtrecord%3A%29.json'
content_hash: 'sha256:54ce5516fdcc0372'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NetServiceDelegate](../netservicedelegate.md)

# netService(_:didUpdateTXTRecord:)

<sub>Instance Method</sub>

Notifies the delegate that the TXT record for a given service has been updated.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
optional func netService(_ sender: NetService, didUpdateTXTRecord data: Data)
```

## Parameters

- `sender` — The service whose TXT record was updated.

- `data` — The new TXT record.

## See Also

### Related Documentation

- [- startMonitoring](<../netservice/startmonitoring().md>) — Starts the monitoring of TXT-record updates for the receiver. _(deprecated)_

### Using Network Services

- [- netServiceWillPublish:](<netservicewillpublish(__).md>) — Notifies the delegate that the network is ready to publish the service.
- [- netService:didNotPublish:](<netservice(__didnotpublish_).md>) — Notifies the delegate that a service could not be published.
- [- netServiceDidPublish:](<netservicedidpublish(__).md>) — Notifies the delegate that a service was successfully published.
- [- netServiceWillResolve:](<netservicewillresolve(__).md>) — Notifies the delegate that the network is ready to resolve the service.
- [- netService:didNotResolve:](<netservice(__didnotresolve_).md>) — Informs the delegate that an error occurred during resolution of a given service.
- [- netServiceDidResolveAddress:](<netservicedidresolveaddress(__).md>) — Informs the delegate that the address for a given service was resolved.
- [- netServiceDidStop:](<netservicedidstop(__).md>) — Informs the delegate that a [- publish](<../netservice/publish().md>) or [- resolveWithTimeout:](<../netservice/resolve(withtimeout_).md>) request was stopped.
