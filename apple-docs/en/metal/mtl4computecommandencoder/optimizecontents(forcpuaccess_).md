---
title: 'optimizeContents(forCPUAccess:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtl4computecommandencoder/optimizecontents(forcpuaccess:)'
source_url: 'https://developer.apple.com/documentation/metal/mtl4computecommandencoder/optimizecontents(forcpuaccess:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtl4computecommandencoder/optimizecontents%28forcpuaccess%3A%29.json'
content_hash: 'sha256:3d445e83ee5e2e37'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTL4ComputeCommandEncoder](../mtl4computecommandencoder.md)

# optimizeContents(forCPUAccess:)

<sub>Instance Method</sub>

Encodes a command that modifies the contents of a texture to improve the performance of CPU accesses to its contents.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func optimizeContents(forCPUAccess texture: any MTLTexture)
```

## Parameters

- `texture` — A [MTLTexture](../mtltexture.md) instance the command optimizes for CPU access.

## Discussion

Optimizing a texture for CPU access may affect the performance of GPU accesses, however, the data the GPU retrieves from the texture remains consistent.

You typically use this command for:

- Textures the CPU accesses for an extended period of time.
- Textures with a [storageMode](../mtltexturedescriptor/storagemode.md) property that’s [MTLStorageModeShared](../mtlstoragemode/shared.md) or [MTLStorageModeManaged](../mtlstoragemode/managed.md).

## See Also

### Encoding optimization commands

- [optimizeCommands(buffer:range:)](<optimizecommands(buffer_range_).md>) — Encode a command to attempt to improve the performance of a range of commands within an indirect command buffer.
- [- optimizeContentsForCPUAccess:slice:level:](<optimizecontents(forcpuaccess_slice_level_).md>) — Encodes a command that modifies the contents of a texture to improve the performance of CPU accesses to its contents in a specific region.
- [- optimizeContentsForGPUAccess:](<optimizecontents(forgpuaccess_).md>) — Encodes a command that modifies the contents of a texture to improve the performance of GPU accesses to its contents.
- [- optimizeContentsForGPUAccess:slice:level:](<optimizecontents(forgpuaccess_slice_level_).md>) — Encodes a command that modifies the contents of a texture instance to improve the performance of GPU accesses to its contents in a specific region.
