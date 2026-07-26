---
title: 'fillBuffer:range:value:'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlblitcommandencoder/fillbuffer:range:value:'
source_url: 'https://developer.apple.com/documentation/metal/mtlblitcommandencoder/fillbuffer:range:value:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlblitcommandencoder/fillbuffer%3Arange%3Avalue%3A.json'
content_hash: 'sha256:a9dd1a8edbbb5b15'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLBlitCommandEncoder](../mtlblitcommandencoder.md)

# fillBuffer:range:value:

<sub>Instance Method</sub>

Encodes a command that fills a buffer with a constant value for each byte.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```objc
- (void) fillBuffer:(id<MTLBuffer>) buffer range:(NSRange) range value:(uint8_t) value;
```

## Parameters

- `buffer` — A buffer instance the command assigns each byte in `range` to `value`.

- `range` — A range of bytes within the `buffer` the command assigns `value` to. The range’s [count](../../swift/collection/count.md) property needs to be greater than `0`. The range’s [count](../../swift/collection/count.md), [lowerBound](../../swift/range/lowerbound.md), and [upperBound](../../swift/range/upperbound.md) properties need to be a multiple of `4` in macOS, but can be any value in iOS and tvOS.

- `value` — The value to write to each byte.

## Default Implementations

### MTLBlitCommandEncoder Implementations

- [fill(buffer:range:value:)](<fill(buffer_range_value_).md>) — Encodes a command that fills a buffer with a constant value for each byte.
