---
title: 'netServiceBrowser(_:didFindDomain:moreComing:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.2+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/netservicebrowserdelegate/netservicebrowser(_:didfinddomain:morecoming:)'
source_url: 'https://developer.apple.com/documentation/foundation/netservicebrowserdelegate/netservicebrowser(_:didfinddomain:morecoming:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/netservicebrowserdelegate/netservicebrowser%28_%3Adidfinddomain%3Amorecoming%3A%29.json'
content_hash: 'sha256:a49061f6c1148a88'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NetServiceBrowserDelegate](../netservicebrowserdelegate.md)

# netServiceBrowser(_:didFindDomain:moreComing:)

<sub>Instance Method</sub>

Tells the delegate the sender found a domain.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
optional func netServiceBrowser(_ browser: NetServiceBrowser, didFindDomain domainString: String, moreComing: Bool)
```

## Parameters

- `browser` — Sender of this delegate message.

- `domainString` — Name of the domain found by `netServiceBrowser`.

- `moreComing` — [true](../../swift/true.md) when `netServiceBrowser` is waiting for additional domains. [false](../../swift/false.md) when there are no additional domains.

## Discussion

The delegate uses this message to compile a list of available domains. It should wait until `moreDomainsComing` is [false](../../swift/false.md) to do a bulk update of user interface elements.

## See Also

### Related Documentation

- [- searchForBrowsableDomains](<../netservicebrowser/searchforbrowsabledomains().md>) — Initiates a search for domains visible to the host. This method returns immediately. _(deprecated)_
- [Bonjour Overview](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/NetServices/Introduction.html#//apple_ref/doc/uid/10000119i)
- [NSNetServices and CFNetServices Programming Guide](https://developer.apple.com/library/archive/documentation/Networking/Conceptual/NSNetServiceProgGuide/Introduction.html#//apple_ref/doc/uid/TP40002736)
- [- searchForRegistrationDomains](<../netservicebrowser/searchforregistrationdomains().md>) — Initiates a search for domains in which the host may register services. _(deprecated)_

### Using Network Service Browsers

- [- netServiceBrowser:didRemoveDomain:moreComing:](<netservicebrowser(__didremovedomain_morecoming_).md>) — Tells the delegate the a domain has disappeared or has become unavailable.
- [- netServiceBrowser:didFindService:moreComing:](<netservicebrowser(__didfind_morecoming_).md>) — Tells the delegate the sender found a service.
- [- netServiceBrowser:didRemoveService:moreComing:](<netservicebrowser(__didremove_morecoming_).md>) — Tells the delegate a service has disappeared or has become unavailable.
- [- netServiceBrowserWillSearch:](<netservicebrowserwillsearch(__).md>) — Tells the delegate that a search is commencing.
- [- netServiceBrowser:didNotSearch:](<netservicebrowser(__didnotsearch_).md>) — Tells the delegate that a search was not successful.
- [- netServiceBrowserDidStopSearch:](<netservicebrowserdidstopsearch(__).md>) — Tells the delegate that a search was stopped.
