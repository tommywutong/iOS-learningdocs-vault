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
doc_path: /documentation/corefoundation/cfmachportcontext/retain
source_url: 'https://developer.apple.com/documentation/corefoundation/cfmachportcontext/retain'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfmachportcontext/retain.json'
content_hash: 'sha256:a4528f5e6af88696'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Foundation](../../corefoundation.md) · [CFMachPortContext](../cfmachportcontext.md)

# retain

<sub>Instance Property</sub>

A retain callback for your program-defined `info` pointer. Can be `NULL`.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var retain: ((UnsafeRawPointer?) -> UnsafeRawPointer?)!
```
