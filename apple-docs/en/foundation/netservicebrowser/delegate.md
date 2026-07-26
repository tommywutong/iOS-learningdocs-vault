---
title: delegate
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+（27.0 起废弃）, iPadOS 2.0+（27.0 起废弃）, Mac Catalyst 13.1+（27.0 起废弃）, macOS 10.2+（27.0 起废弃）, tvOS 9.0+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/foundation/netservicebrowser/delegate
source_url: 'https://developer.apple.com/documentation/foundation/netservicebrowser/delegate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/netservicebrowser/delegate.json'
content_hash: 'sha256:15c145b43c20e479'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NetServiceBrowser](../netservicebrowser.md)

# delegate

<sub>Instance Property</sub>

The delegate object for this instance.

> [!warning] Deprecated
> Use nw_browser_t in Network framework instead

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
unowned(unsafe) var delegate: (any NetServiceBrowserDelegate)? { get set }
```

## See Also

### Configuring Network Service Browsers

- [includesPeerToPeer](includespeertopeer.md) — Whether to browse over peer-to-peer Bluetooth and Wi-Fi, if available. _(deprecated)_
