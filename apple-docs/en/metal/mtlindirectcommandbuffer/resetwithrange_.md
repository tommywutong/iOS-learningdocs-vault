---
title: 'resetWithRange:'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 13.1+, macOS 10.14+, tvOS 12.0+, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlindirectcommandbuffer/resetwithrange:'
source_url: 'https://developer.apple.com/documentation/metal/mtlindirectcommandbuffer/resetwithrange:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlindirectcommandbuffer/resetwithrange%3A.json'
content_hash: 'sha256:1ede1f5890695295'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLIndirectCommandBuffer](../mtlindirectcommandbuffer.md)

# resetWithRange:

<sub>Instance Method</sub>

Resets a range of commands to their default state.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```objc
- (void) resetWithRange:(NSRange) range;
```

## Parameters

- `range` — The range of commands to reset. The range needs to fit inside the indirect command buffer’s extents.
