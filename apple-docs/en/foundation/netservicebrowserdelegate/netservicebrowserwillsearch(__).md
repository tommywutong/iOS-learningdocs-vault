---
title: 'netServiceBrowserWillSearch(_:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.2+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/netservicebrowserdelegate/netservicebrowserwillsearch(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/netservicebrowserdelegate/netservicebrowserwillsearch(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/netservicebrowserdelegate/netservicebrowserwillsearch%28_%3A%29.json'
content_hash: 'sha256:edbdf27d5aeee65f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NetServiceBrowserDelegate](../netservicebrowserdelegate.md)

# netServiceBrowserWillSearch(_:)

<sub>Instance Method</sub>

Tells the delegate that a search is commencing.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
optional func netServiceBrowserWillSearch(_ browser: NetServiceBrowser)
```

## Parameters

- `browser` — Sender of this delegate message.

## Discussion

This message is sent to the delegate only if the underlying network layer is ready to begin a search. The delegate can use this notification to prepare its data structures to receive data.

## See Also

### Using Network Service Browsers

- [- netServiceBrowser:didFindDomain:moreComing:](<netservicebrowser(__didfinddomain_morecoming_).md>) — Tells the delegate the sender found a domain.
- [- netServiceBrowser:didRemoveDomain:moreComing:](<netservicebrowser(__didremovedomain_morecoming_).md>) — Tells the delegate the a domain has disappeared or has become unavailable.
- [- netServiceBrowser:didFindService:moreComing:](<netservicebrowser(__didfind_morecoming_).md>) — Tells the delegate the sender found a service.
- [- netServiceBrowser:didRemoveService:moreComing:](<netservicebrowser(__didremove_morecoming_).md>) — Tells the delegate a service has disappeared or has become unavailable.
- [- netServiceBrowser:didNotSearch:](<netservicebrowser(__didnotsearch_).md>) — Tells the delegate that a search was not successful.
- [- netServiceBrowserDidStopSearch:](<netservicebrowserdidstopsearch(__).md>) — Tells the delegate that a search was stopped.
