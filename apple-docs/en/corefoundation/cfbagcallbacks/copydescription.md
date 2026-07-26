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
doc_path: /documentation/corefoundation/cfbagcallbacks/copydescription
source_url: 'https://developer.apple.com/documentation/corefoundation/cfbagcallbacks/copydescription'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfbagcallbacks/copydescription.json'
content_hash: 'sha256:bc662f9c3471c712'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Foundation](../../corefoundation.md) · [CFBagCallBacks](../cfbagcallbacks.md)

# copyDescription

<sub>Instance Property</sub>

The callback used to create a descriptive string representation of each value in the collection. If `NULL`, the collection will create a simple description of each value. See [CFBagCopyDescriptionCallBack](../cfbagcopydescriptioncallback.md) for a description of this callback.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var copyDescription: CFBagCopyDescriptionCallBack!
```
