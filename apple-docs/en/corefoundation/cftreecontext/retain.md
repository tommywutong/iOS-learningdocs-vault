---
title: retain
framework: Core Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/cftreecontext/retain
source_url: 'https://developer.apple.com/documentation/corefoundation/cftreecontext/retain'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cftreecontext/retain.json'
content_hash: 'sha256:e2c7392e43dfc2cb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Foundation](../../corefoundation.md) · [CFTreeContext](../cftreecontext.md)

# retain

<sub>Instance Property</sub>

The callback used to retain the `info` field. If this parameter is not a pointer to a function of the correct prototype, the behavior is undefined. This value may be `NULL`.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var retain: CFTreeRetainCallBack!
```
