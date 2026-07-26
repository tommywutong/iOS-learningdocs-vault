---
title: 'copyCommands(sourceBuffer:sourceRange:destinationBuffer:destinationIndex:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtl4computecommandencoder/copycommands(sourcebuffer:sourcerange:destinationbuffer:destinationindex:)'
source_url: 'https://developer.apple.com/documentation/metal/mtl4computecommandencoder/copycommands(sourcebuffer:sourcerange:destinationbuffer:destinationindex:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtl4computecommandencoder/copycommands%28sourcebuffer%3Asourcerange%3Adestinationbuffer%3Adestinationindex%3A%29.json'
content_hash: 'sha256:fceca056bec9549c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTL4ComputeCommandEncoder](../mtl4computecommandencoder.md)

# copyCommands(sourceBuffer:sourceRange:destinationBuffer:destinationIndex:)

<sub>Instance Method</sub>

Encodes a command that copies commands from one indirect command buffer into another.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func copyCommands(sourceBuffer: any MTLIndirectCommandBuffer, sourceRange: Range<Int>, destinationBuffer: any MTLIndirectCommandBuffer, destinationIndex: Int)
```

## Parameters

- `sourceRange` — The range of commands in `sourceBuffer` to copy. The copy operation requires that the source range starts at a valid execution point.

- `destinationIndex` — An index in `destinationBuffer` into where the command copies content to. The copy operation requires that the destination index is a valid execution point with enough space left in `destinationBuffer` to accommodate `sourceRange.count` commands.
