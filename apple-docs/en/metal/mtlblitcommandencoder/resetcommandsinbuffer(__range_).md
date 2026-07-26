---
title: 'resetCommandsInBuffer(_:range:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 12.0+, macOS 10.14+, tvOS 12.0+, visionOS]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlblitcommandencoder/resetcommandsinbuffer(_:range:)'
source_url: 'https://developer.apple.com/documentation/metal/mtlblitcommandencoder/resetcommandsinbuffer(_:range:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlblitcommandencoder/resetcommandsinbuffer%28_%3Arange%3A%29.json'
content_hash: 'sha256:0f02af6f1f4b62b7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLBlitCommandEncoder](../mtlblitcommandencoder.md)

# resetCommandsInBuffer(_:range:)

<sub>Instance Method</sub>

Encodes a command that resets a range of commands in an indirect command buffer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func resetCommandsInBuffer(_ buffer: any MTLIndirectCommandBuffer, range: Range<Int>)
```

## Parameters

- `buffer` — An indirect command buffer the command resets.

- `range` — A range of commands within `buffer`.

## See Also

### Managing indirect command buffers

- [copyIndirectCommandBuffer(_:sourceRange:destination:destinationIndex:)](<copyindirectcommandbuffer(__sourcerange_destination_destinationindex_).md>) — Encodes a command that copies commands from one indirect command buffer into another.
- [optimizeIndirectCommandBuffer(_:range:)](<optimizeindirectcommandbuffer(__range_).md>) — Encodes a command that can improve the performance of a range of commands within an indirect command buffer.
