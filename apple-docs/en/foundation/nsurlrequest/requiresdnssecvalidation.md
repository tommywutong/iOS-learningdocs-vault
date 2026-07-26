---
title: requiresDNSSECValidation
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 16.1+, iPadOS 16.1+, Mac Catalyst 16.1+, macOS 13.0+, tvOS 16.1+, visionOS 1.0+, watchOS 9.1+]
languages: [swift, swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsurlrequest/requiresdnssecvalidation
source_url: 'https://developer.apple.com/documentation/foundation/nsurlrequest/requiresdnssecvalidation'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsurlrequest/requiresdnssecvalidation.json'
content_hash: 'sha256:8b4a5f8a30668931'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSURLRequest](../nsurlrequest.md)

# requiresDNSSECValidation

<sub>Instance Property</sub>

A Boolean value that indicates whether a request requires DNSSEC validation during DNS lookup.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var requiresDNSSECValidation: Bool { get }
```

## Discussion

`YES` if the DNS lookup for this request should require DNSSEC validation. Defaults to `NO`.
