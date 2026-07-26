---
title: allDomainsMask
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/filemanager/searchpathdomainmask/alldomainsmask
source_url: 'https://developer.apple.com/documentation/foundation/filemanager/searchpathdomainmask/alldomainsmask'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/filemanager/searchpathdomainmask/alldomainsmask.json'
content_hash: 'sha256:0b29a21ecda5adc5'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [FileManager](../../filemanager.md) · [SearchPathDomainMask](../searchpathdomainmask.md)

# allDomainsMask

<sub>Type Property</sub>

All domains.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var allDomainsMask: FileManager.SearchPathDomainMask { get }
```

## Discussion

Includes all of the above and future items.

## See Also

### Specifying Search Path Domains

- [NSUserDomainMask](userdomainmask.md) — The user’s home directory—the place to install user’s personal items (`~`).
- [NSLocalDomainMask](localdomainmask.md) — The place to install items available to everyone on this machine.
- [NSNetworkDomainMask](networkdomainmask.md) — The place to install items available on the network (`/Network`).
- [NSSystemDomainMask](systemdomainmask.md) — A directory for system files provided by Apple (`/System`) .
