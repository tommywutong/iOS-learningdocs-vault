---
title: copyDescription
framework: Core Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/cfstreamclientcontext/copydescription
source_url: 'https://developer.apple.com/documentation/corefoundation/cfstreamclientcontext/copydescription'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfstreamclientcontext/copydescription.json'
content_hash: 'sha256:e7d647df32c2c244'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Foundation](../../corefoundation.md) · [CFStreamClientContext](../cfstreamclientcontext.md)

# copyDescription

<sub>Instance Property</sub>

A copy description callback for your program-defined `info` pointer. Can be `NULL`.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var copyDescription: ((UnsafeMutableRawPointer?) -> Unmanaged<CFString>?)!
```
