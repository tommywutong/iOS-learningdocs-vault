---
title: 'optimizeContentsForCPUAccess(texture:slice:level:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 13.1+, macOS 10.14+, tvOS 12.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlblitcommandencoder/optimizecontentsforcpuaccess(texture:slice:level:)'
source_url: 'https://developer.apple.com/documentation/metal/mtlblitcommandencoder/optimizecontentsforcpuaccess(texture:slice:level:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlblitcommandencoder/optimizecontentsforcpuaccess%28texture%3Aslice%3Alevel%3A%29.json'
content_hash: 'sha256:171413a9212101e5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLBlitCommandEncoder](../mtlblitcommandencoder.md)

# optimizeContentsForCPUAccess(texture:slice:level:)

<sub>Instance Method</sub>

Encodes a command that improves the performance of CPU memory operations with a specific portion of a texture.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func optimizeContentsForCPUAccess(texture: any MTLTexture, slice: Int, level: Int)
```

## Parameters

- `texture` — A texture the command optimizes.

- `slice` — A slice within `texture`.

- `level` — A mipmap level within `texture`.

## Discussion

This command can reduce the time it takes the CPU to access a texture. Apps typically run the command for:

- Textures the CPU accesses for an extended period of time
- Textures with a [storageMode](../mtlresource/storagemode.md) property that’s [MTLStorageModeShared](../mtlstoragemode/shared.md) or [MTLStorageModeManaged](../mtlstoragemode/managed.md)

When a blit pass runs this command, the GPU only applies lossless changes to the texture’s underlying data.

> [!note] Note
> Optimizing a texture for the CPU may affect the performance of GPU memory operations, but the data the GPU retrieves from the texture remains consistent.

## See Also

### Optimizing textures for CPU access

- [- optimizeContentsForCPUAccess:](<optimizecontentsforcpuaccess(texture_).md>) — Encodes a command that improves the performance of CPU memory operations with a texture.
