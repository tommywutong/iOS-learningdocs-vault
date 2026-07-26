---
title: 'setTextureView(buffer:descriptor:offset:bytesPerRow:index:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtltextureviewpool/settextureview(buffer:descriptor:offset:bytesperrow:index:)'
source_url: 'https://developer.apple.com/documentation/metal/mtltextureviewpool/settextureview(buffer:descriptor:offset:bytesperrow:index:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtltextureviewpool/settextureview%28buffer%3Adescriptor%3Aoffset%3Abytesperrow%3Aindex%3A%29.json'
content_hash: 'sha256:b71cba45f62c2a74'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLTextureViewPool](../mtltextureviewpool.md)

# setTextureView(buffer:descriptor:offset:bytesPerRow:index:)

<sub>Instance Method</sub>

Creates a new lightweight texture view of a buffer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func setTextureView(buffer: any MTLBuffer, descriptor: MTLTextureDescriptor, offset: Int, bytesPerRow: Int, index: Int) -> MTLResourceID
```

## Parameters

- `buffer` — An [MTLBuffer](../mtlbuffer.md) instance for which to create a new texture view.

- `descriptor` — A descriptor specifying properties of the texture view to create.

- `offset` — A byte offset, within the `buffer` parameter, at which the data for the texture view starts.

- `bytesPerRow` — The number of bytes between adjacent rows of pixels in the source buffer’s memory.

- `index` — An index of a slot in the table into which this method writes the new texture view.

## Return Value

The [MTLResourceID](../mtlresourceid.md) of a new buffer view in this pool.

## Discussion

This method creates a lightweight texture view over a buffer, according to a descriptor you provide. It then associates the texture view with a slot in this texture view pool at the index you specify.
