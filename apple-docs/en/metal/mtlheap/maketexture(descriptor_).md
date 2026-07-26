---
title: 'makeTexture(descriptor:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 10.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlheap/maketexture(descriptor:)'
source_url: 'https://developer.apple.com/documentation/metal/mtlheap/maketexture(descriptor:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlheap/maketexture%28descriptor%3A%29.json'
content_hash: 'sha256:9acb5b6d849213d4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLHeap](../mtlheap.md)

# makeTexture(descriptor:)

<sub>Instance Method</sub>

Creates a texture on the heap.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func makeTexture(descriptor: MTLTextureDescriptor) -> (any MTLTexture)?
```

## Parameters

- `descriptor` — A descriptor object that describes the properties of the texture.

## Return Value

A new texture object backed by heap memory, or `nil` if the heap memory is full.

## Discussion

You can call the method with the following restrictions:

- The heap’s type needs to be [MTLHeapTypeAutomatic](../mtlheaptype/automatic.md)
- The texture’s CPU cache mode option needs to match the heap’s [cpuCacheMode](cpucachemode.md) property
- The texture’s storage mode option needs to be [MTLStorageModeMemoryless](../mtlstoragemode/memoryless.md), or match the heap’s [storageMode](storagemode.md) property

## See Also

### Creating textures from a heap

- [- newTextureWithDescriptor:offset:](<maketexture(descriptor_offset_).md>) — Creates a texture at a specified offset on the heap.
