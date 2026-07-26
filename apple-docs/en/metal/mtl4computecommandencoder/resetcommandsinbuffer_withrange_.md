---
title: 'resetCommandsInBuffer:withRange:'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtl4computecommandencoder/resetcommandsinbuffer:withrange:'
source_url: 'https://developer.apple.com/documentation/metal/mtl4computecommandencoder/resetcommandsinbuffer:withrange:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtl4computecommandencoder/resetcommandsinbuffer%3Awithrange%3A.json'
content_hash: 'sha256:914ffe7b182b95b1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTL4ComputeCommandEncoder](../mtl4computecommandencoder.md)

# resetCommandsInBuffer:withRange:

<sub>Instance Method</sub>

Encodes a command that resets a range of commands in an indirect command buffer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```objc
- (void) resetCommandsInBuffer:(id<MTLIndirectCommandBuffer>) buffer withRange:(NSRange) range;
```

## Parameters

- `buffer` — An [MTLIndirectCommandBuffer](../mtlindirectcommandbuffer.md) the command resets.

- `range` — A range of commands within `buffer`.
