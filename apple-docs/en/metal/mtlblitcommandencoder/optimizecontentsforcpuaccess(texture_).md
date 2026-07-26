---
title: 'optimizeContentsForCPUAccess(texture:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 13.1+, macOS 10.14+, tvOS 12.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlblitcommandencoder/optimizecontentsforcpuaccess(texture:)'
source_url: 'https://developer.apple.com/documentation/metal/mtlblitcommandencoder/optimizecontentsforcpuaccess(texture:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlblitcommandencoder/optimizecontentsforcpuaccess%28texture%3A%29.json'
content_hash: 'sha256:e6e9b1306ca6edee'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLBlitCommandEncoder](../mtlblitcommandencoder.md)

# optimizeContentsForCPUAccess(texture:)

<sub>Instance Method</sub>

Encodes a command that improves the performance of CPU memory operations with a texture.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func optimizeContentsForCPUAccess(texture: any MTLTexture)
```

## Parameters

- `texture` — A texture the command optimizes.

## Discussion

This command can reduce the time it takes the CPU to access a texture. Apps typically run the command for:

- Textures the CPU accesses for an extended period of time
- Textures with a [storageMode](../mtlresource/storagemode.md) property that’s [MTLStorageModeShared](../mtlstoragemode/shared.md) or [MTLStorageModeManaged](../mtlstoragemode/managed.md)

When a blit pass runs this command, the GPU only applies lossless changes to the texture’s underlying data.

> [!note] Note
> Optimizing a texture for the CPU may affect the performance of GPU memory operations, but the data the GPU retrieves from the texture remains consistent.

## See Also

### Optimizing textures for CPU access

- [- optimizeContentsForCPUAccess:slice:level:](<optimizecontentsforcpuaccess(texture_slice_level_).md>) — Encodes a command that improves the performance of CPU memory operations with a specific portion of a texture.
