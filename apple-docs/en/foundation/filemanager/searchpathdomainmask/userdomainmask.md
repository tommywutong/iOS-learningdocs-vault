---
title: userDomainMask
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/filemanager/searchpathdomainmask/userdomainmask
source_url: 'https://developer.apple.com/documentation/foundation/filemanager/searchpathdomainmask/userdomainmask'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/filemanager/searchpathdomainmask/userdomainmask.json'
content_hash: 'sha256:cc1bfcf84f37b561'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [FileManager](../../filemanager.md) · [SearchPathDomainMask](../searchpathdomainmask.md)

# userDomainMask

<sub>Type Property</sub>

The user’s home directory—the place to install user’s personal items (`~`).

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var userDomainMask: FileManager.SearchPathDomainMask { get }
```

## See Also

### Specifying Search Path Domains

- [NSLocalDomainMask](localdomainmask.md) — The place to install items available to everyone on this machine.
- [NSNetworkDomainMask](networkdomainmask.md) — The place to install items available on the network (`/Network`).
- [NSSystemDomainMask](systemdomainmask.md) — A directory for system files provided by Apple (`/System`) .
- [NSAllDomainsMask](alldomainsmask.md) — All domains.
