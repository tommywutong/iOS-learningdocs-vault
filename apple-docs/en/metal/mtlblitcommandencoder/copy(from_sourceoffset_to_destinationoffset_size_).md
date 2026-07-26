---
title: 'copy(from:sourceOffset:to:destinationOffset:size:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlblitcommandencoder/copy(from:sourceoffset:to:destinationoffset:size:)'
source_url: 'https://developer.apple.com/documentation/metal/mtlblitcommandencoder/copy(from:sourceoffset:to:destinationoffset:size:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlblitcommandencoder/copy%28from%3Asourceoffset%3Ato%3Adestinationoffset%3Asize%3A%29.json'
content_hash: 'sha256:c73343aae60940df'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLBlitCommandEncoder](../mtlblitcommandencoder.md)

# copy(from:sourceOffset:to:destinationOffset:size:)

<sub>Instance Method</sub>

Encodes a command that copies data from one buffer into another.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func copy(from sourceBuffer: any MTLBuffer, sourceOffset: Int, to destinationBuffer: any MTLBuffer, destinationOffset: Int, size: Int)
```

## Parameters

- `sourceBuffer` — A buffer the command copies data from.

- `sourceOffset` — A byte offset within `sourceBuffer` the command copies from. In macOS, `sourceOffset` needs to be a multiple of `4`, but can be any value in iOS and tvOS.

- `destinationBuffer` — The destination buffer for the copy operation.

- `destinationOffset` — A byte offset within `destinationBuffer` the command copies to. In macOS, `destinationOffset` needs to be a multiple of `4`, but can be any value in iOS and tvOS.

- `size` — The number of bytes the command copies from `sourceBuffer` to `destinationBuffer`. In macOS, `size` needs to be a multiple of `4`, but can be any value in iOS and tvOS.

## Discussion

You can pass the same buffer to the `sourceBuffer` and `destinationBuffer` parameters if `size` is less than the distance between `sourceOffset` and `destinationOffset`.

> [!important] Important
> Copying data to overlapping regions within the same buffer may result in unexpected behavior.
