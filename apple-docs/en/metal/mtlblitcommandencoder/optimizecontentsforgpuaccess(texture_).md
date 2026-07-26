---
title: 'optimizeContentsForGPUAccess(texture:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 13.1+, macOS 10.14+, tvOS 12.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlblitcommandencoder/optimizecontentsforgpuaccess(texture:)'
source_url: 'https://developer.apple.com/documentation/metal/mtlblitcommandencoder/optimizecontentsforgpuaccess(texture:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlblitcommandencoder/optimizecontentsforgpuaccess%28texture%3A%29.json'
content_hash: 'sha256:4c5c6a7d1c03f555'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLBlitCommandEncoder](../mtlblitcommandencoder.md)

# optimizeContentsForGPUAccess(texture:)

<sub>Instance Method</sub>

Encodes a command that improves the performance of GPU memory operations with a texture.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func optimizeContentsForGPUAccess(texture: any MTLTexture)
```

## Parameters

- `texture` — A texture the command optimizes.

## Discussion

This command can reduce the time it takes the GPU to access a texture. Apps typically run the command for:

- Textures the GPU accesses for an extended period of time
- Textures with a [storageMode](../mtlresource/storagemode.md) property that’s [MTLStorageModeShared](../mtlstoragemode/shared.md) or [MTLStorageModeManaged](../mtlstoragemode/managed.md)

When a blit pass runs this command, the GPU only applies lossless changes to the texture’s underlying data.

> [!note] Note
> Optimizing a texture for the GPU may affect the performance of CPU memory operations, but the data the CPU retrieves from the texture remains consistent.

## See Also

### Optimizing textures for GPU access

- [- optimizeContentsForGPUAccess:slice:level:](<optimizecontentsforgpuaccess(texture_slice_level_).md>) — Encodes a command that improves the performance of GPU memory operations with a specific portion of a texture.
