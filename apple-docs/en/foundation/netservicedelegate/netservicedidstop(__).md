---
title: 'netServiceDidStop(_:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.2+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/netservicedelegate/netservicedidstop(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/netservicedelegate/netservicedidstop(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/netservicedelegate/netservicedidstop%28_%3A%29.json'
content_hash: 'sha256:89d3ff2ec693e96a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NetServiceDelegate](../netservicedelegate.md)

# netServiceDidStop(_:)

<sub>Instance Method</sub>

Informs the delegate that a [- publish](<../netservice/publish().md>) or [- resolveWithTimeout:](<../netservice/resolve(withtimeout_).md>) request was stopped.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
optional func netServiceDidStop(_ sender: NetService)
```

## Parameters

- `sender` — The service that stopped.

## See Also

### Using Network Services

- [- netServiceWillPublish:](<netservicewillpublish(__).md>) — Notifies the delegate that the network is ready to publish the service.
- [- netService:didNotPublish:](<netservice(__didnotpublish_).md>) — Notifies the delegate that a service could not be published.
- [- netServiceDidPublish:](<netservicedidpublish(__).md>) — Notifies the delegate that a service was successfully published.
- [- netServiceWillResolve:](<netservicewillresolve(__).md>) — Notifies the delegate that the network is ready to resolve the service.
- [- netService:didNotResolve:](<netservice(__didnotresolve_).md>) — Informs the delegate that an error occurred during resolution of a given service.
- [- netServiceDidResolveAddress:](<netservicedidresolveaddress(__).md>) — Informs the delegate that the address for a given service was resolved.
- [- netService:didUpdateTXTRecordData:](<netservice(__didupdatetxtrecord_).md>) — Notifies the delegate that the TXT record for a given service has been updated.
