---
title: 'makeTexture(descriptor:offset:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlheap/maketexture(descriptor:offset:)'
source_url: 'https://developer.apple.com/documentation/metal/mtlheap/maketexture(descriptor:offset:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlheap/maketexture%28descriptor%3Aoffset%3A%29.json'
content_hash: 'sha256:685e53420eaa4a14'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLHeap](../mtlheap.md)

# makeTexture(descriptor:offset:)

<sub>Instance Method</sub>

Creates a texture at a specified offset on the heap.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func makeTexture(descriptor: MTLTextureDescriptor, offset: Int) -> (any MTLTexture)?
```

## Parameters

- `descriptor` — A descriptor object that describes the properties of the texture.

- `offset` — The distance, in bytes, to place the texture relative to the start of the heap.

## Return Value

A new texture, or `nil` if the heap is not a placement heap.

## Discussion

You can call the method with the following restrictions:

- The heap’s type needs to be [MTLHeapTypePlacement](../mtlheaptype/placement.md)
- The texture’s CPU cache mode option needs to match the heap’s [cpuCacheMode](cpucachemode.md) property
- The texture’s storage mode option needs to be [MTLStorageModeMemoryless](../mtlstoragemode/memoryless.md), or match the heap’s [storageMode](storagemode.md) property

> [!important] Important
> Avoid potentially erratic behavior by aligning the texture correctly so that it doesn’t extend past the end of the heap.

Use the [- heapBufferSizeAndAlignWithLength:options:](<../mtldevice/heapbuffersizeandalign(length_options_).md>) to determine the correct size and alignment.

> [!note] Note
> The new texture can implicitly alias the underlying memory of other resources already in the heap within the overlapping half-open range of `[offset, offset + requiredSize)`.

## See Also

### Creating textures from a heap

- [- newTextureWithDescriptor:](<maketexture(descriptor_).md>) — Creates a texture on the heap.
