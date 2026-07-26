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
doc_path: /documentation/corefoundation/cfdictionaryvaluecallbacks/equal
source_url: 'https://developer.apple.com/documentation/corefoundation/cfdictionaryvaluecallbacks/equal'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfdictionaryvaluecallbacks/equal.json'
content_hash: 'sha256:142a9a99ea4a6e1c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Foundation](../../corefoundation.md) · [CFDictionaryValueCallBacks](../cfdictionaryvaluecallbacks.md)

# equal

<sub>Instance Property</sub>

The callback used to compare values in the dictionary for equality. If `NULL`, the collection will use pointer equality to compare values in the collection. See [CFDictionaryEqualCallBack](../cfdictionaryequalcallback.md) for a description of this callback.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var equal: CFDictionaryEqualCallBack!
```
