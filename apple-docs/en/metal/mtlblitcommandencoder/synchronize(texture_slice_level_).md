---
title: 'synchronize(texture:slice:level:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [Mac Catalyst 13.0+（27.0 起废弃）, macOS 10.11+（27.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/metal/mtlblitcommandencoder/synchronize(texture:slice:level:)'
source_url: 'https://developer.apple.com/documentation/metal/mtlblitcommandencoder/synchronize(texture:slice:level:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlblitcommandencoder/synchronize%28texture%3Aslice%3Alevel%3A%29.json'
content_hash: 'sha256:1fc4ba4f4b6c563c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLBlitCommandEncoder](../mtlblitcommandencoder.md)

# synchronize(texture:slice:level:)

<sub>Instance Method</sub>

Encodes a command that synchronizes a part of the CPU’s copy of a texture so that it matches the GPU’s copy.

> [!warning] Deprecated
> Managed storage has no effect on Apple Silicon, use Shared storage instead

<sub>Mac Catalyst, macOS</sub>

```swift
func synchronize(texture: any MTLTexture, slice: Int, level: Int)
```

## Parameters

- `texture` — An [MTLTexture](../mtltexture.md) instance with a [storageMode](../mtlresource/storagemode.md) property that’s equal to [MTLStorageModeManaged](../mtlstoragemode/managed.md).

- `slice` — A slice within `texture`.

- `level` — A mipmap level within `texture`.

## Discussion

This method ensures the CPU can correctly read the changes a GPU makes to a slice of a texture that uses the managed storage mode. For the resources you create with [MTLStorageModeManaged](../mtlstoragemode/managed.md), the CPU and GPU each have a copy of that resource. As the GPU modifies its copy, the CPU’s copy remains unchanged until you synchronize with a command, such as this one.

The CPU can access the updated content from its copy of the texture after the synchronization command completes.

> [!note] Note
> The command this method encodes behaves similarly to the command that [- synchronizeResource:](<synchronize(resource_).md>) encodes, except that it flushes only the applicable slice and mipmap level.

## See Also

### Synchronizing managed resources

- [- synchronizeResource:](<synchronize(resource_).md>) — Encodes a command that synchronizes the CPU’s copy of a managed resource, such as a buffer or texture, so that it matches the GPU’s copy. _(deprecated)_
