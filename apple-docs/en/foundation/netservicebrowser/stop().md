---
title: stop()
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+（27.0 起废弃）, iPadOS 2.0+（27.0 起废弃）, Mac Catalyst 13.1+（27.0 起废弃）, macOS 10.2+（27.0 起废弃）, tvOS 9.0+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/foundation/netservicebrowser/stop()
source_url: 'https://developer.apple.com/documentation/foundation/netservicebrowser/stop()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/netservicebrowser/stop%28%29.json'
content_hash: 'sha256:405f5c0440d1362a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NetServiceBrowser](../netservicebrowser.md)

# stop()

<sub>Instance Method</sub>

Halts a currently running search or resolution.

> [!warning] Deprecated
> Use nw_browser_t in Network framework instead

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func stop()
```

## Discussion

This method sends a [- netServiceBrowserDidStopSearch:](<../netservicebrowserdelegate/netservicebrowserdidstopsearch(__).md>) message to the delegate and causes the browser to discard any pending search results.

## See Also

### Related Documentation

- [- netServiceBrowserDidStopSearch:](<../netservicebrowserdelegate/netservicebrowserdidstopsearch(__).md>) — Tells the delegate that a search was stopped.

### Using Network Service Browsers

- [- searchForBrowsableDomains](<searchforbrowsabledomains().md>) — Initiates a search for domains visible to the host. This method returns immediately. _(deprecated)_
- [- searchForRegistrationDomains](<searchforregistrationdomains().md>) — Initiates a search for domains in which the host may register services. _(deprecated)_
- [- searchForServicesOfType:inDomain:](<searchforservices(oftype_indomain_).md>) — Starts a search for services of a particular type within a specific domain. _(deprecated)_
