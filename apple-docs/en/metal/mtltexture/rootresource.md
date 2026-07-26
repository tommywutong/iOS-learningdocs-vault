---
title: rootResource
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+（10.0 起废弃）, iPadOS 8.0+（10.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）, macOS 10.11+（10.12 起废弃）, tvOS（10.0 起废弃）, visionOS 1.0+（1.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/metal/mtltexture/rootresource
source_url: 'https://developer.apple.com/documentation/metal/mtltexture/rootresource'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtltexture/rootresource.json'
content_hash: 'sha256:cbe9b89137e9797c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLTexture](../mtltexture.md)

# rootResource

<sub>Instance Property</sub>

The resource that owns the storage for this texture.

> [!warning] Deprecated
> Use [parentTexture](parent.md) or [buffer](buffer.md) instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var rootResource: (any MTLResource)? { get }
```

## Discussion

If the value is `nil`, then this texture image owns its own data. Otherwise, this value is the [MTLResource](../mtlresource.md) instance used to create the texture. For example, it might be a texture that uses the contents of an [MTLBuffer](../mtlbuffer.md) object or a texture view that reinterprets the contents of another [MTLTexture](../mtltexture.md).

## See Also

### Getting information about ancestor resources

- [parentTexture](parent.md) — The parent texture used to create this texture, if any.
- [parentRelativeLevel](parentrelativelevel.md) — The base level of the parent texture used to create this texture.
- [parentRelativeSlice](parentrelativeslice.md) — The base slice of the parent texture used to create this texture.
- [buffer](buffer.md) — The source buffer used to create this texture, if any.
- [bufferOffset](bufferoffset.md) — The offset in the source buffer where the texture’s data comes from.
- [bufferBytesPerRow](bufferbytesperrow.md) — The number of bytes in each row of the texture’s source buffer.
