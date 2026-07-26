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
doc_path: /documentation/corefoundation/cfdictionarykeycallbacks/copydescription
source_url: 'https://developer.apple.com/documentation/corefoundation/cfdictionarykeycallbacks/copydescription'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfdictionarykeycallbacks/copydescription.json'
content_hash: 'sha256:cd83c6bd3922a46d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Foundation](../../corefoundation.md) · [CFDictionaryKeyCallBacks](../cfdictionarykeycallbacks.md)

# copyDescription

<sub>Instance Property</sub>

The callback used to create a descriptive string representation of each key in the dictionary. If `NULL`, the collection will create a simple description of each key. See [CFDictionaryCopyDescriptionCallBack](../cfdictionarycopydescriptioncallback.md) for a description of this callback.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var copyDescription: CFDictionaryCopyDescriptionCallBack!
```
