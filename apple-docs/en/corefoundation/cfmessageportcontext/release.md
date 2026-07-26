---
title: release
framework: Core Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/cfmessageportcontext/release
source_url: 'https://developer.apple.com/documentation/corefoundation/cfmessageportcontext/release'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfmessageportcontext/release.json'
content_hash: 'sha256:4101497e3fa3eb9e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Foundation](../../corefoundation.md) · [CFMessagePortContext](../cfmessageportcontext.md)

# release

<sub>Instance Property</sub>

A release callback for your program-defined `info` pointer. Can be `NULL`.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var release: ((UnsafeRawPointer?) -> Void)!
```
