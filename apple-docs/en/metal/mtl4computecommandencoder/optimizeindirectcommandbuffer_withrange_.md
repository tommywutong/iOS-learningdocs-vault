---
title: 'optimizeIndirectCommandBuffer:withRange:'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtl4computecommandencoder/optimizeindirectcommandbuffer:withrange:'
source_url: 'https://developer.apple.com/documentation/metal/mtl4computecommandencoder/optimizeindirectcommandbuffer:withrange:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtl4computecommandencoder/optimizeindirectcommandbuffer%3Awithrange%3A.json'
content_hash: 'sha256:712927cf266d7363'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTL4ComputeCommandEncoder](../mtl4computecommandencoder.md)

# optimizeIndirectCommandBuffer:withRange:

<sub>Instance Method</sub>

Encode a command to attempt to improve the performance of a range of commands within an indirect command buffer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```objc
- (void) optimizeIndirectCommandBuffer:(id<MTLIndirectCommandBuffer>) indirectCommandBuffer withRange:(NSRange) range;
```

## Parameters

- `indirectCommandBuffer` — An [MTLIndirectCommandBuffer](../mtlindirectcommandbuffer.md) instance that this command optimizes.

- `range` — A range of commands within `indirectCommandBuffer`.

## See Also

### Encoding optimization commands

- [- optimizeContentsForCPUAccess:](<optimizecontents(forcpuaccess_).md>) — Encodes a command that modifies the contents of a texture to improve the performance of CPU accesses to its contents.
- [- optimizeContentsForCPUAccess:slice:level:](<optimizecontents(forcpuaccess_slice_level_).md>) — Encodes a command that modifies the contents of a texture to improve the performance of CPU accesses to its contents in a specific region.
- [- optimizeContentsForGPUAccess:](<optimizecontents(forgpuaccess_).md>) — Encodes a command that modifies the contents of a texture to improve the performance of GPU accesses to its contents.
- [- optimizeContentsForGPUAccess:slice:level:](<optimizecontents(forgpuaccess_slice_level_).md>) — Encodes a command that modifies the contents of a texture instance to improve the performance of GPU accesses to its contents in a specific region.
