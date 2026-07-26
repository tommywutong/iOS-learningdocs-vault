---
title: allowsPersistentDNS
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift, swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsurlrequest/allowspersistentdns
source_url: 'https://developer.apple.com/documentation/foundation/nsurlrequest/allowspersistentdns'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsurlrequest/allowspersistentdns.json'
content_hash: 'sha256:6379255269a61af8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSURLRequest](../nsurlrequest.md)

# allowsPersistentDNS

<sub>Instance Property</sub>

A Boolean value that indicates whether storing and usage of DNS answers in a persistent per-process cache is allowed.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var allowsPersistentDNS: Bool { get }
```

## Discussion

This should only be set for hostnames whose resolutions are not expected to change across networks. Defaults to `NO`.
