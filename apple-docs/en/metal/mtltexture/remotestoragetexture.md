---
title: remoteStorageTexture
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [macOS 10.15+（27.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/metal/mtltexture/remotestoragetexture
source_url: 'https://developer.apple.com/documentation/metal/mtltexture/remotestoragetexture'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtltexture/remotestoragetexture.json'
content_hash: 'sha256:77fa6042779132e6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLTexture](../mtltexture.md)

# remoteStorageTexture

<sub>Instance Property</sub>

The texture on another GPU that the texture was created from, if any.

> [!warning] Deprecated
> Not applicable on Apple Silicon

<sub>macOS</sub>

```swift
var remoteStorageTexture: (any MTLTexture)? { get }
```

## Discussion

If the value of this property is non-`nil`, it contains a reference to the [MTLTexture](../mtltexture.md) instance that created this texture. If the texture isn’t a remote view, the value of this property is `nil`.

You can use remote views only as the source for copy commands encoded by an [MTLBlitCommandEncoder](../mtlblitcommandencoder.md).

## See Also

### Creating views of textures on other GPUs

- [- newRemoteTextureViewForDevice:](<makeremotetextureview(__).md>) — Creates a remote texture view for another GPU in the same peer group. _(deprecated)_
