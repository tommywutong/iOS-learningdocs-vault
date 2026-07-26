---
title: searchForRegistrationDomains()
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+（27.0 起废弃）, iPadOS 2.0+（27.0 起废弃）, Mac Catalyst 13.1+（27.0 起废弃）, macOS 10.2+（27.0 起废弃）, tvOS 9.0+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/foundation/netservicebrowser/searchforregistrationdomains()
source_url: 'https://developer.apple.com/documentation/foundation/netservicebrowser/searchforregistrationdomains()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/netservicebrowser/searchforregistrationdomains%28%29.json'
content_hash: 'sha256:31ae2673d908f266'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NetServiceBrowser](../netservicebrowser.md)

# searchForRegistrationDomains()

<sub>Instance Method</sub>

Initiates a search for domains in which the host may register services.

> [!warning] Deprecated
> Use nw_browser_t in Network framework instead

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func searchForRegistrationDomains()
```

## Discussion

This method returns immediately, sending a [- netServiceBrowserWillSearch:](<../netservicebrowserdelegate/netservicebrowserwillsearch(__).md>) message to the delegate if the network was ready to initiate the search. The delegate receives a subsequent [- netServiceBrowser:didFindDomain:moreComing:](<../netservicebrowserdelegate/netservicebrowser(__didfinddomain_morecoming_).md>) message for each domain discovered.

Most network service browser clients do not have to use this method—it is sufficient to publish a service with the empty string, which registers it in any available registration domains automatically.

## See Also

### Related Documentation

- [- netServiceBrowserWillSearch:](<../netservicebrowserdelegate/netservicebrowserwillsearch(__).md>) — Tells the delegate that a search is commencing.
- [- netServiceBrowser:didFindDomain:moreComing:](<../netservicebrowserdelegate/netservicebrowser(__didfinddomain_morecoming_).md>) — Tells the delegate the sender found a domain.

### Using Network Service Browsers

- [- searchForBrowsableDomains](<searchforbrowsabledomains().md>) — Initiates a search for domains visible to the host. This method returns immediately. _(deprecated)_
- [- searchForServicesOfType:inDomain:](<searchforservices(oftype_indomain_).md>) — Starts a search for services of a particular type within a specific domain. _(deprecated)_
- [- stop](<stop().md>) — Halts a currently running search or resolution. _(deprecated)_
