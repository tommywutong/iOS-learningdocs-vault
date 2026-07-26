---
title: 'setThreadgroupMemoryLength(_:offset:index:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.5+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlrendercommandencoder/setthreadgroupmemorylength(_:offset:index:)'
source_url: 'https://developer.apple.com/documentation/metal/mtlrendercommandencoder/setthreadgroupmemorylength(_:offset:index:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlrendercommandencoder/setthreadgroupmemorylength%28_%3Aoffset%3Aindex%3A%29.json'
content_hash: 'sha256:61b6f13367974591'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLRenderCommandEncoder](../mtlrendercommandencoder.md)

# setThreadgroupMemoryLength(_:offset:index:)

<sub>Instance Method</sub>

Configures the size of a threadgroup memory buffer for an entry in the fragment or tile shader argument table.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func setThreadgroupMemoryLength(_ length: Int, offset: Int, index: Int)
```

## Parameters

- `length` — The threadgroup memory length, in bytes.

- `offset` — An integer that represents the location, in bytes, from the start of the buffer at `index` where the threadgroup memory begins.

- `index` — An integer that represents an entry in the buffer argument table.

## Discussion

You can only change the threadgroup memory’s size between tile dispatches (see [- dispatchThreadsPerTile:](<dispatchthreadspertile(__).md>)).

> [!important] Important
> Exceeding the threadgroup memory allocation for the render pass can trigger a debug error.

## See Also

### Configuring persistent threadgroup memory

- [- setObjectThreadgroupMemoryLength:atIndex:](<setobjectthreadgroupmemorylength(__index_).md>) — Configures the size of a threadgroup memory buffer for an entry in the object argument table.
