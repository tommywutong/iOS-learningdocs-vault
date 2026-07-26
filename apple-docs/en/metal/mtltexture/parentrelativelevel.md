---
title: parentRelativeLevel
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtltexture/parentrelativelevel
source_url: 'https://developer.apple.com/documentation/metal/mtltexture/parentrelativelevel'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtltexture/parentrelativelevel.json'
content_hash: 'sha256:509c5b9a0f34a9f5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLTexture](../mtltexture.md)

# parentRelativeLevel

<sub>Instance Property</sub>

The base level of the parent texture used to create this texture.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var parentRelativeLevel: Int { get }
```

## Discussion

This property is only valid for textures created from a [parentTexture](parent.md) texture. The default value is `0`.

## See Also

### Getting information about ancestor resources

- [parentTexture](parent.md) — The parent texture used to create this texture, if any.
- [parentRelativeSlice](parentrelativeslice.md) — The base slice of the parent texture used to create this texture.
- [buffer](buffer.md) — The source buffer used to create this texture, if any.
- [bufferOffset](bufferoffset.md) — The offset in the source buffer where the texture’s data comes from.
- [bufferBytesPerRow](bufferbytesperrow.md) — The number of bytes in each row of the texture’s source buffer.
- [rootResource](rootresource.md) — The resource that owns the storage for this texture. _(deprecated)_
