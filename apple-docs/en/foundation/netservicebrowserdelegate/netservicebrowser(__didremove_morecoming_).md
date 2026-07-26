---
title: 'netServiceBrowser(_:didRemove:moreComing:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.2+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/netservicebrowserdelegate/netservicebrowser(_:didremove:morecoming:)'
source_url: 'https://developer.apple.com/documentation/foundation/netservicebrowserdelegate/netservicebrowser(_:didremove:morecoming:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/netservicebrowserdelegate/netservicebrowser%28_%3Adidremove%3Amorecoming%3A%29.json'
content_hash: 'sha256:139fc7e4d7658c16'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NetServiceBrowserDelegate](../netservicebrowserdelegate.md)

# netServiceBrowser(_:didRemove:moreComing:)

<sub>Instance Method</sub>

Tells the delegate a service has disappeared or has become unavailable.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
optional func netServiceBrowser(_ browser: NetServiceBrowser, didRemove service: NetService, moreComing: Bool)
```

## Parameters

- `browser` — Sender of this delegate message.

- `service` — Network service that has become unavailable.

- `moreComing` — [true](../../swift/true.md) when `netServiceBrowser` is waiting for additional services. [false](../../swift/false.md) when there are no additional services.

## Discussion

The delegate uses this message to compile a list of unavailable services. It should wait until `moreServicesComing` is [false](../../swift/false.md) to do a bulk update of user interface elements.

## See Also

### Using Network Service Browsers

- [- netServiceBrowser:didFindDomain:moreComing:](<netservicebrowser(__didfinddomain_morecoming_).md>) — Tells the delegate the sender found a domain.
- [- netServiceBrowser:didRemoveDomain:moreComing:](<netservicebrowser(__didremovedomain_morecoming_).md>) — Tells the delegate the a domain has disappeared or has become unavailable.
- [- netServiceBrowser:didFindService:moreComing:](<netservicebrowser(__didfind_morecoming_).md>) — Tells the delegate the sender found a service.
- [- netServiceBrowserWillSearch:](<netservicebrowserwillsearch(__).md>) — Tells the delegate that a search is commencing.
- [- netServiceBrowser:didNotSearch:](<netservicebrowser(__didnotsearch_).md>) — Tells the delegate that a search was not successful.
- [- netServiceBrowserDidStopSearch:](<netservicebrowserdidstopsearch(__).md>) — Tells the delegate that a search was stopped.
