---
title: 'netServiceBrowser(_:didFind:moreComing:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.2+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/netservicebrowserdelegate/netservicebrowser(_:didfind:morecoming:)'
source_url: 'https://developer.apple.com/documentation/foundation/netservicebrowserdelegate/netservicebrowser(_:didfind:morecoming:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/netservicebrowserdelegate/netservicebrowser%28_%3Adidfind%3Amorecoming%3A%29.json'
content_hash: 'sha256:5f9be63a191d3cf0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NetServiceBrowserDelegate](../netservicebrowserdelegate.md)

# netServiceBrowser(_:didFind:moreComing:)

<sub>Instance Method</sub>

Tells the delegate the sender found a service.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
optional func netServiceBrowser(_ browser: NetServiceBrowser, didFind service: NetService, moreComing: Bool)
```

## Parameters

- `browser` — Sender of this delegate message.

- `service` — Network service found by `netServiceBrowser`. The delegate can use this object to connect to and use the service.

- `moreComing` — [true](../../swift/true.md) when `netServiceBrowser` is waiting for additional services. [false](../../swift/false.md) when there are no additional services.

## Discussion

The delegate uses this message to compile a list of available services. It should wait until `moreServicesComing` is [false](../../swift/false.md) to do a bulk update of user interface elements.

### Special Considerations

If the delegate chooses to resolve `netService`, it should retain `netService` and set itself as that service’s delegate. The delegate should, therefore, release that service when it receives the [- netServiceDidResolveAddress:](<../netservicedelegate/netservicedidresolveaddress(__).md>) or [- netService:didNotResolve:](<../netservicedelegate/netservice(__didnotresolve_).md>) delegate messages of the  [NetService](../netservice.md) class.

## See Also

### Related Documentation

- [- searchForServicesOfType:inDomain:](<../netservicebrowser/searchforservices(oftype_indomain_).md>) — Starts a search for services of a particular type within a specific domain. _(deprecated)_

### Using Network Service Browsers

- [- netServiceBrowser:didFindDomain:moreComing:](<netservicebrowser(__didfinddomain_morecoming_).md>) — Tells the delegate the sender found a domain.
- [- netServiceBrowser:didRemoveDomain:moreComing:](<netservicebrowser(__didremovedomain_morecoming_).md>) — Tells the delegate the a domain has disappeared or has become unavailable.
- [- netServiceBrowser:didRemoveService:moreComing:](<netservicebrowser(__didremove_morecoming_).md>) — Tells the delegate a service has disappeared or has become unavailable.
- [- netServiceBrowserWillSearch:](<netservicebrowserwillsearch(__).md>) — Tells the delegate that a search is commencing.
- [- netServiceBrowser:didNotSearch:](<netservicebrowser(__didnotsearch_).md>) — Tells the delegate that a search was not successful.
- [- netServiceBrowserDidStopSearch:](<netservicebrowserdidstopsearch(__).md>) — Tells the delegate that a search was stopped.
