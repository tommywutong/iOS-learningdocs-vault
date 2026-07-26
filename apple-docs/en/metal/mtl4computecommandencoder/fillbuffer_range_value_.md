---
title: 'fillBuffer:range:value:'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtl4computecommandencoder/fillbuffer:range:value:'
source_url: 'https://developer.apple.com/documentation/metal/mtl4computecommandencoder/fillbuffer:range:value:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtl4computecommandencoder/fillbuffer%3Arange%3Avalue%3A.json'
content_hash: 'sha256:926e625d95da9470'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTL4ComputeCommandEncoder](../mtl4computecommandencoder.md)

# fillBuffer:range:value:

<sub>Instance Method</sub>

Encodes a command that fills a buffer with a constant value for each byte.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```objc
- (void) fillBuffer:(id<MTLBuffer>) buffer range:(NSRange) range value:(uint8_t) value;
```

## Parameters

- `buffer` — A [MTLBuffer](../mtlbuffer.md) instance for which this command assigns each byte in a range to a value.

- `range` — A range of bytes within `buffer` the command assigns value to. When calling this method, pass in a range with a length greater than `0`.

- `value` — The value to write to each byte.
