---
title: 'optimizeIndirectCommandBuffer(_:range:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 12.0+, macOS 10.14+, tvOS 12.0+, visionOS]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlblitcommandencoder/optimizeindirectcommandbuffer(_:range:)'
source_url: 'https://developer.apple.com/documentation/metal/mtlblitcommandencoder/optimizeindirectcommandbuffer(_:range:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlblitcommandencoder/optimizeindirectcommandbuffer%28_%3Arange%3A%29.json'
content_hash: 'sha256:607bac0dfcb293ef'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLBlitCommandEncoder](../mtlblitcommandencoder.md)

# optimizeIndirectCommandBuffer(_:range:)

<sub>Instance Method</sub>

Encodes a command that can improve the performance of a range of commands within an indirect command buffer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func optimizeIndirectCommandBuffer(_ buffer: any MTLIndirectCommandBuffer, range: Range<Int>)
```

## Parameters

- `buffer` — An indirect command buffer the command optimizes.

- `range` — A range of commands within `indirectCommandBuffer`.

## Discussion

This command can reduce the time it takes the GPU to run the commands within an indirect command buffer by removing its redundancies. For example, an indirect command buffer may have empty commands or commands that duplicate identical state. Redundancies like these can come from multiple compute functions that encode commands in parallel, which can sometimes reset commands or configure identical states multiple times.

> [!important] Important
> You can only run optimized commands by using the entire range. Otherwise, starting or ending within an optimized range may result in unexpected behavior.

You can’t run any commands that start or end at an index within that range, or that cross into another optimized range. However, you can reuse the range you optimize by resetting it and then encoding new commands to it.

## See Also

### Managing indirect command buffers

- [copyIndirectCommandBuffer(_:sourceRange:destination:destinationIndex:)](<copyindirectcommandbuffer(__sourcerange_destination_destinationindex_).md>) — Encodes a command that copies commands from one indirect command buffer into another.
- [resetCommandsInBuffer(_:range:)](<resetcommandsinbuffer(__range_).md>) — Encodes a command that resets a range of commands in an indirect command buffer.
