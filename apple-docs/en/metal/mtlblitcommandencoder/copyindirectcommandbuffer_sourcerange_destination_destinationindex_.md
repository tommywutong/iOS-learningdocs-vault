---
title: 'copyIndirectCommandBuffer:sourceRange:destination:destinationIndex:'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 13.1+, macOS 10.14+, tvOS 12.0+, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlblitcommandencoder/copyindirectcommandbuffer:sourcerange:destination:destinationindex:'
source_url: 'https://developer.apple.com/documentation/metal/mtlblitcommandencoder/copyindirectcommandbuffer:sourcerange:destination:destinationindex:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlblitcommandencoder/copyindirectcommandbuffer%3Asourcerange%3Adestination%3Adestinationindex%3A.json'
content_hash: 'sha256:82d4b657170072e7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLBlitCommandEncoder](../mtlblitcommandencoder.md)

# copyIndirectCommandBuffer:sourceRange:destination:destinationIndex:

<sub>Instance Method</sub>

Encodes a command that copies commands from one indirect command buffer into another.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```objc
- (void) copyIndirectCommandBuffer:(id<MTLIndirectCommandBuffer>) source sourceRange:(NSRange) sourceRange destination:(id<MTLIndirectCommandBuffer>) destination destinationIndex:(NSUInteger) destinationIndex;
```

## Parameters

- `source` — An indirect command buffer the command copies from.

- `sourceRange` — The range of commands in the source buffer to copy. The source range needs to start on a valid execution point.

- `destination` — Another indirect command buffer the command copies to.

- `destinationIndex` — An index in `destination` where the command copies content from `source` to. The destination index needs to be a valid execution point with enough remaining space in `destination` to accommodate `sourceRange.count` indices.

## Discussion

You can copy commands from one indirect command buffer to another, but only a compatible one. You can create compatible indirect command buffers by passing [MTLIndirectCommandBufferDescriptor](../mtlindirectcommandbufferdescriptor.md) instances with the same configuration to the [- newIndirectCommandBufferWithDescriptor:maxCommandCount:options:](<../mtldevice/makeindirectcommandbuffer(descriptor_maxcommandcount_options_).md>) method of [MTLDevice](../mtldevice.md).

## See Also

### Managing indirect command buffers

- [resetCommandsInBuffer:withRange:](resetcommandsinbuffer_withrange_.md) — Encodes a command that resets a range of commands in an indirect command buffer.
- [optimizeIndirectCommandBuffer:withRange:](optimizeindirectcommandbuffer_withrange_.md) — Encodes a command that can improve the performance of a range of commands within an indirect command buffer.
