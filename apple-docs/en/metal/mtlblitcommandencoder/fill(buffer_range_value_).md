---
title: 'fill(buffer:range:value:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.11+, tvOS 8.0+, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlblitcommandencoder/fill(buffer:range:value:)'
source_url: 'https://developer.apple.com/documentation/metal/mtlblitcommandencoder/fill(buffer:range:value:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlblitcommandencoder/fill%28buffer%3Arange%3Avalue%3A%29.json'
content_hash: 'sha256:971dabd429e17c89'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLBlitCommandEncoder](../mtlblitcommandencoder.md)

# fill(buffer:range:value:)

<sub>Instance Method</sub>

Encodes a command that fills a buffer with a constant value for each byte.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func fill(buffer: any MTLBuffer, range: Range<Int>, value: UInt8)
```

## Parameters

- `buffer` — A buffer instance the command assigns each byte in `range` to `value`.

- `range` — A range of bytes within the `buffer` the command assigns `value` to. The range’s [count](../../swift/collection/count.md) property needs to be greater than `0`. The range’s [count](../../swift/collection/count.md), [lowerBound](../../swift/range/lowerbound.md), and [upperBound](../../swift/range/upperbound.md) properties need to be a multiple of `4` in macOS, but can be any value in iOS and tvOS.

- `value` — The value to write to each byte.
