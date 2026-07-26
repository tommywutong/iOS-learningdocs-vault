---
title: 'fill(buffer:range:value:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtl4computecommandencoder/fill(buffer:range:value:)'
source_url: 'https://developer.apple.com/documentation/metal/mtl4computecommandencoder/fill(buffer:range:value:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtl4computecommandencoder/fill%28buffer%3Arange%3Avalue%3A%29.json'
content_hash: 'sha256:48ccb96b5c17431e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTL4ComputeCommandEncoder](../mtl4computecommandencoder.md)

# fill(buffer:range:value:)

<sub>Instance Method</sub>

Encodes a command that fills a buffer with a constant value for each byte.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func fill(buffer: any MTLBuffer, range: Range<Int>, value: UInt8)
```

## Parameters

- `buffer` — A MTLBuffer instance the command assigns each byte in range to value.

- `range` — A range of bytes within the buffer the command assigns value to. The range’s count property needs to be greater than 0.

- `value` — The value to write to each byte.
