---
title: buffer
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, macOS 10.12+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtltexture/buffer
source_url: 'https://developer.apple.com/documentation/metal/mtltexture/buffer'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtltexture/buffer.json'
content_hash: 'sha256:db8d3d839b186d25'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLTexture](../mtltexture.md)

# buffer

<sub>Instance Property</sub>

The source buffer used to create this texture, if any.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var buffer: (any MTLBuffer)? { get }
```

## Discussion

When this value is `nil`, another [MTLTexture](../mtltexture.md) instance provides texture data.

## See Also

### Related Documentation

- [- newTextureWithDescriptor:offset:bytesPerRow:](<../mtlbuffer/maketexture(descriptor_offset_bytesperrow_).md>) — Creates a texture that shares its storage with the buffer.

### Getting information about ancestor resources

- [parentTexture](parent.md) — The parent texture used to create this texture, if any.
- [parentRelativeLevel](parentrelativelevel.md) — The base level of the parent texture used to create this texture.
- [parentRelativeSlice](parentrelativeslice.md) — The base slice of the parent texture used to create this texture.
- [bufferOffset](bufferoffset.md) — The offset in the source buffer where the texture’s data comes from.
- [bufferBytesPerRow](bufferbytesperrow.md) — The number of bytes in each row of the texture’s source buffer.
- [rootResource](rootresource.md) — The resource that owns the storage for this texture. _(deprecated)_
