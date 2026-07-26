---
title: copyDescription
framework: Core Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/cfsocketcontext/copydescription
source_url: 'https://developer.apple.com/documentation/corefoundation/cfsocketcontext/copydescription'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfsocketcontext/copydescription.json'
content_hash: 'sha256:8c3da1859f8372ac'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Foundation](../../corefoundation.md) · [CFSocketContext](../cfsocketcontext.md)

# copyDescription

<sub>Instance Property</sub>

A copy description callback for your program-defined `info` pointer. Can be `NULL`.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var copyDescription: ((UnsafeRawPointer?) -> Unmanaged<CFString>?)!
```
