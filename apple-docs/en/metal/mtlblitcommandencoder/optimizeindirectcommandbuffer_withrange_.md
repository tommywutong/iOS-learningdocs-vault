---
title: 'optimizeIndirectCommandBuffer:withRange:'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 13.1+, macOS 10.14+, tvOS 12.0+, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlblitcommandencoder/optimizeindirectcommandbuffer:withrange:'
source_url: 'https://developer.apple.com/documentation/metal/mtlblitcommandencoder/optimizeindirectcommandbuffer:withrange:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlblitcommandencoder/optimizeindirectcommandbuffer%3Awithrange%3A.json'
content_hash: 'sha256:6d14a2037cebc52a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLBlitCommandEncoder](../mtlblitcommandencoder.md)

# optimizeIndirectCommandBuffer:withRange:

<sub>Instance Method</sub>

Encodes a command that can improve the performance of a range of commands within an indirect command buffer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```objc
- (void) optimizeIndirectCommandBuffer:(id<MTLIndirectCommandBuffer>) indirectCommandBuffer withRange:(NSRange) range;
```

## Parameters

- `indirectCommandBuffer` — An indirect command buffer the command optimizes.

- `range` — A range of commands within `indirectCommandBuffer`.

## Discussion

This command can reduce the time it takes the GPU to run the commands within an indirect command buffer by removing its redundancies. For example, an indirect command buffer may have empty commands or commands that duplicate identical state. Redundancies like these can come from multiple compute functions that encode commands in parallel, which can sometimes reset commands or configure identical states multiple times.

> [!important] Important
> You can only run optimized commands by using the entire range. Otherwise, starting or ending within an optimized range may result in unexpected behavior.

You can’t run any commands that start or end at an index within that range, or that cross into another optimized range. However, you can reuse the range you optimize by resetting it and then encoding new commands to it.

## See Also

### Managing indirect command buffers

- [copyIndirectCommandBuffer:sourceRange:destination:destinationIndex:](copyindirectcommandbuffer_sourcerange_destination_destinationindex_.md) — Encodes a command that copies commands from one indirect command buffer into another.
- [resetCommandsInBuffer:withRange:](resetcommandsinbuffer_withrange_.md) — Encodes a command that resets a range of commands in an indirect command buffer.
