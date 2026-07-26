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
doc_path: /documentation/corefoundation/cfdictionarykeycallbacks/equal
source_url: 'https://developer.apple.com/documentation/corefoundation/cfdictionarykeycallbacks/equal'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfdictionarykeycallbacks/equal.json'
content_hash: 'sha256:255ce144adb6bea0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Foundation](../../corefoundation.md) · [CFDictionaryKeyCallBacks](../cfdictionarykeycallbacks.md)

# equal

<sub>Instance Property</sub>

The callback used to compare keys in the dictionary for equality. If `NULL`, the collection will use pointer equality to compare keys in the collection. See [CFDictionaryEqualCallBack](../cfdictionaryequalcallback.md) for a description of this callback.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var equal: CFDictionaryEqualCallBack!
```
