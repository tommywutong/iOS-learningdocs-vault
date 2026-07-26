---
title: 'setObjectThreadgroupMemoryLength(_:index:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtl4rendercommandencoder/setobjectthreadgroupmemorylength(_:index:)'
source_url: 'https://developer.apple.com/documentation/metal/mtl4rendercommandencoder/setobjectthreadgroupmemorylength(_:index:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtl4rendercommandencoder/setobjectthreadgroupmemorylength%28_%3Aindex%3A%29.json'
content_hash: 'sha256:284865a5e8780f51'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTL4RenderCommandEncoder](../mtl4rendercommandencoder.md)

# setObjectThreadgroupMemoryLength(_:index:)

<sub>Instance Method</sub>

Configures the size of a threadgroup memory buffer for a threadgroup argument in the object shader function.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func setObjectThreadgroupMemoryLength(_ length: Int, index: Int)
```

## Parameters

- `length` — The size of the threadgroup memory, in bytes.

- `index` — An integer that corresponds to the index of the argument you annotate with attribute `[[threadgroup(index)]]` in the shader function.

## See Also

### Configuring persistent threadgroup memory

- [- setThreadgroupMemoryLength:offset:atIndex:](<setthreadgroupmemorylength(__offset_index_).md>) — Configures the size of a threadgroup memory buffer for a threadgroup argument in the fragment and tile shader functions.
