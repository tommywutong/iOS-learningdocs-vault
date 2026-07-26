---
title: 'makeRemoteTextureView(_:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.15+（27.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/metal/mtltexture/makeremotetextureview(_:)'
source_url: 'https://developer.apple.com/documentation/metal/mtltexture/makeremotetextureview(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtltexture/makeremotetextureview%28_%3A%29.json'
content_hash: 'sha256:060449f0d6d0c083'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLTexture](../mtltexture.md)

# makeRemoteTextureView(_:)

<sub>Instance Method</sub>

Creates a remote texture view for another GPU in the same peer group.

> [!warning] Deprecated
> Not applicable on Apple Silicon

<sub>macOS</sub>

```swift
func makeRemoteTextureView(_ device: any MTLDevice) -> (any MTLTexture)?
```

## Discussion

The device instance that created this texture and the device instance passed into this method need to have the same nonzero peer group identifier ([peerGroupID](../mtldevice/peergroupid.md)). This texture needs to either use the private storage mode ([MTLStorageModePrivate](../mtlstoragemode/private.md)) or be backed by an [IOSurface](../../iosurface/iosurface.md).

A remote view doesn’t allocate any storage for the new texture; it references the memory allocated for the original texture. You can use remote views only as a source for copy commands encoded by an [MTLBlitCommandEncoder](../mtlblitcommandencoder.md). For more information, see [Transferring data between connected GPUs](../transferring-data-between-connected-gpus.md).

## See Also

### Creating views of textures on other GPUs

- [remoteStorageTexture](remotestoragetexture.md) — The texture on another GPU that the texture was created from, if any. _(deprecated)_
