---
title: 'optimizeContents(forCPUAccess:slice:level:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtl4computecommandencoder/optimizecontents(forcpuaccess:slice:level:)'
source_url: 'https://developer.apple.com/documentation/metal/mtl4computecommandencoder/optimizecontents(forcpuaccess:slice:level:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtl4computecommandencoder/optimizecontents%28forcpuaccess%3Aslice%3Alevel%3A%29.json'
content_hash: 'sha256:0b7480903488c628'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTL4ComputeCommandEncoder](../mtl4computecommandencoder.md)

# optimizeContents(forCPUAccess:slice:level:)

<sub>Instance Method</sub>

Encodes a command that modifies the contents of a texture to improve the performance of CPU accesses to its contents in a specific region.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func optimizeContents(forCPUAccess texture: any MTLTexture, slice: Int, level: Int)
```

## Parameters

- `texture` — A [MTLTexture](../mtltexture.md) the command optimizes for CPU access.

- `slice` — A slice within `texture`.

- `level` — A mipmap level within `texture`.

## Discussion

Optimizing a texture for CPU access may affect the performance of GPU accesses, however, the data the GPU retrieves from the texture remains consistent.

You typically use this command for:

- Textures the CPU accesses for an extended period of time.
- Textures with a [storageMode](../mtltexturedescriptor/storagemode.md) property that’s [MTLStorageModeShared](../mtlstoragemode/shared.md) or [MTLStorageModeManaged](../mtlstoragemode/managed.md).

## See Also

### Encoding optimization commands

- [optimizeCommands(buffer:range:)](<optimizecommands(buffer_range_).md>) — Encode a command to attempt to improve the performance of a range of commands within an indirect command buffer.
- [- optimizeContentsForCPUAccess:](<optimizecontents(forcpuaccess_).md>) — Encodes a command that modifies the contents of a texture to improve the performance of CPU accesses to its contents.
- [- optimizeContentsForGPUAccess:](<optimizecontents(forgpuaccess_).md>) — Encodes a command that modifies the contents of a texture to improve the performance of GPU accesses to its contents.
- [- optimizeContentsForGPUAccess:slice:level:](<optimizecontents(forgpuaccess_slice_level_).md>) — Encodes a command that modifies the contents of a texture instance to improve the performance of GPU accesses to its contents in a specific region.
