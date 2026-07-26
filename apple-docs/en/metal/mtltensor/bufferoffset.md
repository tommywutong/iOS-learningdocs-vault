---
title: bufferOffset
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtltensor/bufferoffset
source_url: 'https://developer.apple.com/documentation/metal/mtltensor/bufferoffset'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtltensor/bufferoffset.json'
content_hash: 'sha256:567dba6949e04112'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLTensor](../mtltensor.md)

# bufferOffset

<sub>Instance Property</sub>

An offset, in bytes, into the buffer instance this tensor shares its storage with, or zero if this tensor does not wrap an underlying buffer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var bufferOffset: Int { get }
```
