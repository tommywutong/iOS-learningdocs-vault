---
title: equal
framework: Core Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/cfbagcallbacks/equal
source_url: 'https://developer.apple.com/documentation/corefoundation/cfbagcallbacks/equal'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfbagcallbacks/equal.json'
content_hash: 'sha256:52b2a066a5e7ad94'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Foundation](../../corefoundation.md) · [CFBagCallBacks](../cfbagcallbacks.md)

# equal

<sub>Instance Property</sub>

The callback used to compare values in the collection for equality for some operations. If `NULL`, the collection will use pointer equality to compare values in the collection. See [CFBagEqualCallBack](../cfbagequalcallback.md) for a description of this callback.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var equal: CFBagEqualCallBack!
```
