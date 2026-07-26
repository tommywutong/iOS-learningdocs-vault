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
doc_path: /documentation/corefoundation/cfsetcallbacks/equal
source_url: 'https://developer.apple.com/documentation/corefoundation/cfsetcallbacks/equal'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfsetcallbacks/equal.json'
content_hash: 'sha256:97edcd24ed76d803'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Foundation](../../corefoundation.md) · [CFSetCallBacks](../cfsetcallbacks.md)

# equal

<sub>Instance Property</sub>

The callback used to compare values in the collection for equality for some operations. If `NULL`, the collection will use pointer equality to compare values in the collection. See [CFSetEqualCallBack](../cfsetequalcallback.md) for a description of this callback.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var equal: CFSetEqualCallBack!
```
