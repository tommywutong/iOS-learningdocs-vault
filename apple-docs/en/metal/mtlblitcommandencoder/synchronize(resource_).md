---
title: 'synchronize(resource:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [Mac Catalyst 13.0+（27.0 起废弃）, macOS 10.11+（27.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/metal/mtlblitcommandencoder/synchronize(resource:)'
source_url: 'https://developer.apple.com/documentation/metal/mtlblitcommandencoder/synchronize(resource:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlblitcommandencoder/synchronize%28resource%3A%29.json'
content_hash: 'sha256:1ba79e778b5489b4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLBlitCommandEncoder](../mtlblitcommandencoder.md)

# synchronize(resource:)

<sub>Instance Method</sub>

Encodes a command that synchronizes the CPU’s copy of a managed resource, such as a buffer or texture, so that it matches the GPU’s copy.

> [!warning] Deprecated
> Managed storage has no effect on Apple Silicon, use Shared storage instead

<sub>Mac Catalyst, macOS</sub>

```swift
func synchronize(resource: any MTLResource)
```

## Parameters

- `resource` — An [MTLResource](../mtlresource.md) instance — such as an [MTLBuffer](../mtlbuffer.md) or [MTLTexture](../mtltexture.md) — with a [storageMode](../mtlresource/storagemode.md) property that’s equal to [MTLStorageModeManaged](../mtlstoragemode/managed.md).

## Discussion

This method ensures the CPU can correctly read all the changes a GPU makes to a resource that uses the managed storage mode. For the resources you create with [MTLStorageModeManaged](../mtlstoragemode/managed.md), the CPU and GPU each have a copy of that resource. As the GPU modifies its copy, the CPU’s copy remains unchanged until you synchronize with a command, such as this one.

The CPU can access the updated content from its copy of the resources after the synchronization command completes.

> [!note] Note
> You can encode a command that selectively synchronizes parts of an [MTLTexture](../mtltexture.md) by calling the [- synchronizeTexture:slice:level:](<synchronize(texture_slice_level_).md>) method.

## See Also

### Synchronizing managed resources

- [- synchronizeTexture:slice:level:](<synchronize(texture_slice_level_).md>) — Encodes a command that synchronizes a part of the CPU’s copy of a texture so that it matches the GPU’s copy. _(deprecated)_
