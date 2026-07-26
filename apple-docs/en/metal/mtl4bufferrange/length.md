---
title: length
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtl4bufferrange/length
source_url: 'https://developer.apple.com/documentation/metal/mtl4bufferrange/length'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtl4bufferrange/length.json'
content_hash: 'sha256:97596e6c1956f6de'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTL4BufferRange](../mtl4bufferrange.md)

# length

<sub>Instance Property</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var length: UInt64
```

## Discussion

Length of the region which begins at the given address. If the length is not known, a value of (uint64_t)-1 represents the range from the given address to the end of the buffer.
