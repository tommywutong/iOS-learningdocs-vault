---
title: hash
framework: Core Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/cfsetcallbacks/hash
source_url: 'https://developer.apple.com/documentation/corefoundation/cfsetcallbacks/hash'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfsetcallbacks/hash.json'
content_hash: 'sha256:f4117f9529944c97'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Foundation](../../corefoundation.md) · [CFSetCallBacks](../cfsetcallbacks.md)

# hash

<sub>Instance Property</sub>

The callback used to compute a hash code for values in a collection. If `NULL`, the collection computes a hash code by converting the pointer value to an integer. See [CFSetHashCallBack](../cfsethashcallback.md) for a description of this callback.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var hash: CFSetHashCallBack!
```
