---
title: hostName
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+（27.0 起废弃）, iPadOS 2.0+（27.0 起废弃）, Mac Catalyst 13.1+（27.0 起废弃）, macOS 10.2+（27.0 起废弃）, tvOS 9.0+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/foundation/netservice/hostname
source_url: 'https://developer.apple.com/documentation/foundation/netservice/hostname'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/netservice/hostname.json'
content_hash: 'sha256:21d5eb660b73b0ad'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NetService](../netservice.md)

# hostName

<sub>Instance Property</sub>

A string containing the DNS hostname for this service.

> [!warning] Deprecated
> Use nw_connection_t or nw_listener_t in Network framework instead

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var hostName: String? { get }
```

## Discussion

This value is `nil` until the service has been resolved (when `addresses` is non-`nil`).
