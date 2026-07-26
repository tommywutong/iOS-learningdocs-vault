---
title: searchForBrowsableDomains()
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+（27.0 起废弃）, iPadOS 2.0+（27.0 起废弃）, Mac Catalyst 13.1+（27.0 起废弃）, macOS 10.2+（27.0 起废弃）, tvOS 9.0+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/foundation/netservicebrowser/searchforbrowsabledomains()
source_url: 'https://developer.apple.com/documentation/foundation/netservicebrowser/searchforbrowsabledomains()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/netservicebrowser/searchforbrowsabledomains%28%29.json'
content_hash: 'sha256:362a0486acfe0038'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NetServiceBrowser](../netservicebrowser.md)

# searchForBrowsableDomains()

<sub>Instance Method</sub>

Initiates a search for domains visible to the host. This method returns immediately.

> [!warning] Deprecated
> Use nw_browser_t in Network framework instead

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func searchForBrowsableDomains()
```

## Discussion

The delegate receives a [- netServiceBrowser:didFindDomain:moreComing:](<../netservicebrowserdelegate/netservicebrowser(__didfinddomain_morecoming_).md>) message for each domain discovered.

## See Also

### Using Network Service Browsers

- [- searchForRegistrationDomains](<searchforregistrationdomains().md>) — Initiates a search for domains in which the host may register services. _(deprecated)_
- [- searchForServicesOfType:inDomain:](<searchforservices(oftype_indomain_).md>) — Starts a search for services of a particular type within a specific domain. _(deprecated)_
- [- stop](<stop().md>) — Halts a currently running search or resolution. _(deprecated)_
