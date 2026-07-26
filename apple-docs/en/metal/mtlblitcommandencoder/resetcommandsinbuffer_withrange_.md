---
title: 'resetCommandsInBuffer:withRange:'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 13.1+, macOS 10.14+, tvOS 12.0+, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlblitcommandencoder/resetcommandsinbuffer:withrange:'
source_url: 'https://developer.apple.com/documentation/metal/mtlblitcommandencoder/resetcommandsinbuffer:withrange:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlblitcommandencoder/resetcommandsinbuffer%3Awithrange%3A.json'
content_hash: 'sha256:02439155bea4bb7c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLBlitCommandEncoder](../mtlblitcommandencoder.md)

# resetCommandsInBuffer:withRange:

<sub>Instance Method</sub>

Encodes a command that resets a range of commands in an indirect command buffer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```objc
- (void) resetCommandsInBuffer:(id<MTLIndirectCommandBuffer>) buffer withRange:(NSRange) range;
```

## Parameters

- `buffer` — An indirect command buffer the command resets.

- `range` — A range of commands within `buffer`.

## See Also

### Managing indirect command buffers

- [copyIndirectCommandBuffer:sourceRange:destination:destinationIndex:](copyindirectcommandbuffer_sourcerange_destination_destinationindex_.md) — Encodes a command that copies commands from one indirect command buffer into another.
- [optimizeIndirectCommandBuffer:withRange:](optimizeindirectcommandbuffer_withrange_.md) — Encodes a command that can improve the performance of a range of commands within an indirect command buffer.
