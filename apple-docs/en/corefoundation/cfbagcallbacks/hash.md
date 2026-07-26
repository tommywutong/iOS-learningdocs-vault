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
doc_path: /documentation/corefoundation/cfbagcallbacks/hash
source_url: 'https://developer.apple.com/documentation/corefoundation/cfbagcallbacks/hash'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfbagcallbacks/hash.json'
content_hash: 'sha256:0477ea508ed91779'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Foundation](../../corefoundation.md) · [CFBagCallBacks](../cfbagcallbacks.md)

# hash

<sub>Instance Property</sub>

The callback used to compute a hash code for values in a collection. If `NULL`, the collection computes a hash code by converting the pointer value to an integer. See [CFBagHashCallBack](../cfbaghashcallback.md) for a description of this callback.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var hash: CFBagHashCallBack!
```
