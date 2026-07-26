---
title: 'copyIndirectCommandBuffer:sourceRange:destination:destinationIndex:'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtl4computecommandencoder/copyindirectcommandbuffer:sourcerange:destination:destinationindex:'
source_url: 'https://developer.apple.com/documentation/metal/mtl4computecommandencoder/copyindirectcommandbuffer:sourcerange:destination:destinationindex:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtl4computecommandencoder/copyindirectcommandbuffer%3Asourcerange%3Adestination%3Adestinationindex%3A.json'
content_hash: 'sha256:1973dd4ce17801a7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTL4ComputeCommandEncoder](../mtl4computecommandencoder.md)

# copyIndirectCommandBuffer:sourceRange:destination:destinationIndex:

<sub>Instance Method</sub>

Encodes a command that copies commands from an indirect command buffer into another.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```objc
- (void) copyIndirectCommandBuffer:(id<MTLIndirectCommandBuffer>) source sourceRange:(NSRange) sourceRange destination:(id<MTLIndirectCommandBuffer>) destination destinationIndex:(NSUInteger) destinationIndex;
```

## Parameters

- `source` — An [MTLIndirectCommandBuffer](../mtlindirectcommandbuffer.md) instance from where the command copies.

- `sourceRange` — The range of commands in `source` to copy. The copy operation requires that the source range starts at a valid execution point.

- `destination` — Another [MTLIndirectCommandBuffer](../mtlindirectcommandbuffer.md) instance into which the command copies.

- `destinationIndex` — An index in `destination` into where the command copies content to. The copy operation requires that the destination index is a valid execution point with enough space left in `destination` to accommodate `sourceRange.count` commands.
