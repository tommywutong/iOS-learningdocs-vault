---
title: NetServiceBrowserDelegate
framework: Foundation
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.2+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/netservicebrowserdelegate
source_url: 'https://developer.apple.com/documentation/foundation/netservicebrowserdelegate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/netservicebrowserdelegate.json'
content_hash: 'sha256:a0f99767afea9594'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NetServiceBrowserDelegate

<sub>Protocol</sub>

The interface a net service browser uses to inform a delegate about the state of service discovery.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
protocol NetServiceBrowserDelegate : NSObjectProtocol
```

## Overview

Delegates of [NetServiceBrowser](netservicebrowser.md) instances optionally implement these methods.

## Relationships

- **Inherits From**: [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Using Network Service Browsers

- [- netServiceBrowser:didFindDomain:moreComing:](<netservicebrowserdelegate/netservicebrowser(__didfinddomain_morecoming_).md>) — Tells the delegate the sender found a domain.
- [- netServiceBrowser:didRemoveDomain:moreComing:](<netservicebrowserdelegate/netservicebrowser(__didremovedomain_morecoming_).md>) — Tells the delegate the a domain has disappeared or has become unavailable.
- [- netServiceBrowser:didFindService:moreComing:](<netservicebrowserdelegate/netservicebrowser(__didfind_morecoming_).md>) — Tells the delegate the sender found a service.
- [- netServiceBrowser:didRemoveService:moreComing:](<netservicebrowserdelegate/netservicebrowser(__didremove_morecoming_).md>) — Tells the delegate a service has disappeared or has become unavailable.
- [- netServiceBrowserWillSearch:](<netservicebrowserdelegate/netservicebrowserwillsearch(__).md>) — Tells the delegate that a search is commencing.
- [- netServiceBrowser:didNotSearch:](<netservicebrowserdelegate/netservicebrowser(__didnotsearch_).md>) — Tells the delegate that a search was not successful.
- [- netServiceBrowserDidStopSearch:](<netservicebrowserdelegate/netservicebrowserdidstopsearch(__).md>) — Tells the delegate that a search was stopped.

## See Also

### Service Discovery

- [NetServiceBrowser](netservicebrowser.md) — A network service browser that finds published services on a network using multicast DNS. _(deprecated)_
