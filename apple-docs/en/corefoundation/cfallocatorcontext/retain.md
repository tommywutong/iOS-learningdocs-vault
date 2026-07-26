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
doc_path: /documentation/corefoundation/cfallocatorcontext/retain
source_url: 'https://developer.apple.com/documentation/corefoundation/cfallocatorcontext/retain'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfallocatorcontext/retain.json'
content_hash: 'sha256:7aaa150e53487aae'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Foundation](../../corefoundation.md) · [CFAllocatorContext](../cfallocatorcontext.md)

# retain

<sub>Instance Property</sub>

A prototype for a function callback that retains the data pointed to by the `info` field. In implementing this function, retain the data you have defined for the allocator context in this field. (This might make sense only if the data is a Core Foundation object.) You may set this function pointer to `NULL`.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var retain: CFAllocatorRetainCallBack!
```
