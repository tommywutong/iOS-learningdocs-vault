---
title: buffer
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtltensor/buffer
source_url: 'https://developer.apple.com/documentation/metal/mtltensor/buffer'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtltensor/buffer.json'
content_hash: 'sha256:9a568fc49e1a2241'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLTensor](../mtltensor.md)

# buffer

<sub>Instance Property</sub>

A buffer instance this tensor shares its storage with or `nil` if this tensor does not wrap an underlying buffer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var buffer: (any MTLBuffer)? { get }
```
