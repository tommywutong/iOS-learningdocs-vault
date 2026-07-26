---
title: assumesHTTP3Capable
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 14.5+, iPadOS 14.5+, Mac Catalyst 14.5+, macOS 11.3+, tvOS 14.5+, visionOS 1.0+, watchOS 7.4+]
languages: [swift, swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsurlrequest/assumeshttp3capable
source_url: 'https://developer.apple.com/documentation/foundation/nsurlrequest/assumeshttp3capable'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsurlrequest/assumeshttp3capable.json'
content_hash: 'sha256:081db33b3c0b4891'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSURLRequest](../nsurlrequest.md)

# assumesHTTP3Capable

<sub>Instance Property</sub>

A Boolean value that indicates whether the server is assumed to support HTTP/3.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var assumesHTTP3Capable: Bool { get }
```

## Discussion

When `YES`, enables QUIC racing without HTTP/3 service discovery. Defaults to `NO`. The default may be `YES` in a future OS update.
