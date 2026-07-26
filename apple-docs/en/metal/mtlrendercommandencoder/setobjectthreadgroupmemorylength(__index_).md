---
title: 'setObjectThreadgroupMemoryLength(_:index:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlrendercommandencoder/setobjectthreadgroupmemorylength(_:index:)'
source_url: 'https://developer.apple.com/documentation/metal/mtlrendercommandencoder/setobjectthreadgroupmemorylength(_:index:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlrendercommandencoder/setobjectthreadgroupmemorylength%28_%3Aindex%3A%29.json'
content_hash: 'sha256:43acd1d57c3b0cea'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLRenderCommandEncoder](../mtlrendercommandencoder.md)

# setObjectThreadgroupMemoryLength(_:index:)

<sub>Instance Method</sub>

Configures the size of a threadgroup memory buffer for an entry in the object argument table.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func setObjectThreadgroupMemoryLength(_ length: Int, index: Int)
```

## Parameters

- `length` — The threadgroup memory length, in bytes.

- `index` — An integer that represents an entry in the object argument table.

## See Also

### Configuring persistent threadgroup memory

- [- setThreadgroupMemoryLength:offset:atIndex:](<setthreadgroupmemorylength(__offset_index_).md>) — Configures the size of a threadgroup memory buffer for an entry in the fragment or tile shader argument table.
