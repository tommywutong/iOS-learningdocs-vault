---
title: 'searchForServices(ofType:inDomain:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+（27.0 起废弃）, iPadOS 2.0+（27.0 起废弃）, Mac Catalyst 13.1+（27.0 起废弃）, macOS 10.2+（27.0 起废弃）, tvOS 9.0+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/foundation/netservicebrowser/searchforservices(oftype:indomain:)'
source_url: 'https://developer.apple.com/documentation/foundation/netservicebrowser/searchforservices(oftype:indomain:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/netservicebrowser/searchforservices%28oftype%3Aindomain%3A%29.json'
content_hash: 'sha256:e8cdc595072c2227'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NetServiceBrowser](../netservicebrowser.md)

# searchForServices(ofType:inDomain:)

<sub>Instance Method</sub>

Starts a search for services of a particular type within a specific domain.

> [!warning] Deprecated
> Use nw_browser_t in Network framework instead

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func searchForServices(ofType type: String, inDomain domainString: String)
```

## Parameters

- `type` — Type of the service to search for.

- `domainString` — Domain name in which to perform the search.

## Discussion

This method returns immediately, sending a [- netServiceBrowserWillSearch:](<../netservicebrowserdelegate/netservicebrowserwillsearch(__).md>) message to the delegate if the network was ready to initiate the search.The delegate receives subsequent [- netServiceBrowser:didFindService:moreComing:](<../netservicebrowserdelegate/netservicebrowser(__didfind_morecoming_).md>) messages for each service discovered.

The `serviceType` argument must contain both the service type and transport layer information. To ensure that the mDNS responder searches for services, rather than hosts, make sure to prefix both the service name and transport layer name with an underscore character (”_”). For example, to search for an HTTP service on TCP, you would use the type string “`_http._tcp.`”. Note that the period character at the end is required.

The `domainName` argument can be an explicit domain name, the generic local domain `@"local."` (note trailing period, which indicates an absolute name), or the empty string (`@""`), which indicates the default registration domains. Usually, you pass in an empty string. Note that it is acceptable to use an empty string for the `domainName` argument when publishing or browsing a service, but do not rely on this for resolution.

## See Also

### Related Documentation

- [- netServiceBrowser:didFindService:moreComing:](<../netservicebrowserdelegate/netservicebrowser(__didfind_morecoming_).md>) — Tells the delegate the sender found a service.
- [- netServiceBrowserWillSearch:](<../netservicebrowserdelegate/netservicebrowserwillsearch(__).md>) — Tells the delegate that a search is commencing.

### Using Network Service Browsers

- [- searchForBrowsableDomains](<searchforbrowsabledomains().md>) — Initiates a search for domains visible to the host. This method returns immediately. _(deprecated)_
- [- searchForRegistrationDomains](<searchforregistrationdomains().md>) — Initiates a search for domains in which the host may register services. _(deprecated)_
- [- stop](<stop().md>) — Halts a currently running search or resolution. _(deprecated)_
