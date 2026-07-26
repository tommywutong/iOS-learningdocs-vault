---
title: 'netServiceBrowser(_:didNotSearch:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.2+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/netservicebrowserdelegate/netservicebrowser(_:didnotsearch:)'
source_url: 'https://developer.apple.com/documentation/foundation/netservicebrowserdelegate/netservicebrowser(_:didnotsearch:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/netservicebrowserdelegate/netservicebrowser%28_%3Adidnotsearch%3A%29.json'
content_hash: 'sha256:3f75e4a99f077a41'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NetServiceBrowserDelegate](../netservicebrowserdelegate.md)

# netServiceBrowser(_:didNotSearch:)

<sub>Instance Method</sub>

Tells the delegate that a search was not successful.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
optional func netServiceBrowser(_ browser: NetServiceBrowser, didNotSearch errorDict: [String : NSNumber])
```

## Parameters

- `browser` — Sender of this delegate message.

- `errorDict` — Dictionary with the reasons the search was unsuccessful. Use the dictionary keys [NSNetServicesErrorCode](../netservice/errorcode-swift.type.property.md) and [NSNetServicesErrorDomain](../netservice/errordomain.md) to retrieve the error information from the dictionary.

## See Also

### Using Network Service Browsers

- [- netServiceBrowser:didFindDomain:moreComing:](<netservicebrowser(__didfinddomain_morecoming_).md>) — Tells the delegate the sender found a domain.
- [- netServiceBrowser:didRemoveDomain:moreComing:](<netservicebrowser(__didremovedomain_morecoming_).md>) — Tells the delegate the a domain has disappeared or has become unavailable.
- [- netServiceBrowser:didFindService:moreComing:](<netservicebrowser(__didfind_morecoming_).md>) — Tells the delegate the sender found a service.
- [- netServiceBrowser:didRemoveService:moreComing:](<netservicebrowser(__didremove_morecoming_).md>) — Tells the delegate a service has disappeared or has become unavailable.
- [- netServiceBrowserWillSearch:](<netservicebrowserwillsearch(__).md>) — Tells the delegate that a search is commencing.
- [- netServiceBrowserDidStopSearch:](<netservicebrowserdidstopsearch(__).md>) — Tells the delegate that a search was stopped.
