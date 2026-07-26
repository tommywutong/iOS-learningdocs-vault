---
title: 'netServiceBrowserDidStopSearch(_:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.2+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/netservicebrowserdelegate/netservicebrowserdidstopsearch(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/netservicebrowserdelegate/netservicebrowserdidstopsearch(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/netservicebrowserdelegate/netservicebrowserdidstopsearch%28_%3A%29.json'
content_hash: 'sha256:84184cf9ecba8ab5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NetServiceBrowserDelegate](../netservicebrowserdelegate.md)

# netServiceBrowserDidStopSearch(_:)

<sub>Instance Method</sub>

Tells the delegate that a search was stopped.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
optional func netServiceBrowserDidStopSearch(_ browser: NetServiceBrowser)
```

## Parameters

- `browser` — Sender of this delegate message.

## Discussion

When `netServiceBrowser` receives a [- stop](<../netservicebrowser/stop().md>) message from its client, `netServiceBrowser` sends a `netServiceBrowserDidStopSearch:` message to its delegate. The delegate then performs any necessary cleanup.

## See Also

### Related Documentation

- [- stop](<../netservicebrowser/stop().md>) — Halts a currently running search or resolution. _(deprecated)_

### Using Network Service Browsers

- [- netServiceBrowser:didFindDomain:moreComing:](<netservicebrowser(__didfinddomain_morecoming_).md>) — Tells the delegate the sender found a domain.
- [- netServiceBrowser:didRemoveDomain:moreComing:](<netservicebrowser(__didremovedomain_morecoming_).md>) — Tells the delegate the a domain has disappeared or has become unavailable.
- [- netServiceBrowser:didFindService:moreComing:](<netservicebrowser(__didfind_morecoming_).md>) — Tells the delegate the sender found a service.
- [- netServiceBrowser:didRemoveService:moreComing:](<netservicebrowser(__didremove_morecoming_).md>) — Tells the delegate a service has disappeared or has become unavailable.
- [- netServiceBrowserWillSearch:](<netservicebrowserwillsearch(__).md>) — Tells the delegate that a search is commencing.
- [- netServiceBrowser:didNotSearch:](<netservicebrowser(__didnotsearch_).md>) — Tells the delegate that a search was not successful.
