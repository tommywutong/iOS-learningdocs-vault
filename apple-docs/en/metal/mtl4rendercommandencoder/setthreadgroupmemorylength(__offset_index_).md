---
title: 'setThreadgroupMemoryLength(_:offset:index:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtl4rendercommandencoder/setthreadgroupmemorylength(_:offset:index:)'
source_url: 'https://developer.apple.com/documentation/metal/mtl4rendercommandencoder/setthreadgroupmemorylength(_:offset:index:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtl4rendercommandencoder/setthreadgroupmemorylength%28_%3Aoffset%3Aindex%3A%29.json'
content_hash: 'sha256:61dad8bed77941d7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTL4RenderCommandEncoder](../mtl4rendercommandencoder.md)

# setThreadgroupMemoryLength(_:offset:index:)

<sub>Instance Method</sub>

Configures the size of a threadgroup memory buffer for a threadgroup argument in the fragment and tile shader functions.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func setThreadgroupMemoryLength(_ length: Int, offset: Int, index: Int)
```

## Parameters

- `length` — The size of the threadgroup memory, in bytes.

- `offset` — An integer that represents the location, in bytes, from the start of the threadgroup memory buffer at `index` where the threadgroup memory begins.

- `index` — An integer that corresponds to the index of the argument you annotate with attribute `[[threadgroup(index)]]` in the shader function.

## See Also

### Configuring persistent threadgroup memory

- [- setObjectThreadgroupMemoryLength:atIndex:](<setobjectthreadgroupmemorylength(__index_).md>) — Configures the size of a threadgroup memory buffer for a threadgroup argument in the object shader function.
