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
doc_path: /documentation/corefoundation/cfarraycallbacks/equal
source_url: 'https://developer.apple.com/documentation/corefoundation/cfarraycallbacks/equal'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfarraycallbacks/equal.json'
content_hash: 'sha256:7c064e7d3fe953ad'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Foundation](../../corefoundation.md) · [CFArrayCallBacks](../cfarraycallbacks.md)

# equal

<sub>Instance Property</sub>

The callback used to compare values in the array for equality for some operations. If `NULL`, the collection will use pointer equality to compare values in the collection. See [CFArrayEqualCallBack](../cfarrayequalcallback.md) for a description of this callback.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var equal: CFArrayEqualCallBack!
```
