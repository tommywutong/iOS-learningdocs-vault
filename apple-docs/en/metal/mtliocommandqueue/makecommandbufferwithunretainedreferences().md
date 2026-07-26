---
title: makeCommandBufferWithUnretainedReferences()
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtliocommandqueue/makecommandbufferwithunretainedreferences()
source_url: 'https://developer.apple.com/documentation/metal/mtliocommandqueue/makecommandbufferwithunretainedreferences()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtliocommandqueue/makecommandbufferwithunretainedreferences%28%29.json'
content_hash: 'sha256:9bbfb3589122e9c4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLIOCommandQueue](../mtliocommandqueue.md)

# makeCommandBufferWithUnretainedReferences()

<sub>Instance Method</sub>

Creates an input/output command buffer for the command queue that doesn’t retain the instances you pass to its methods.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func makeCommandBufferWithUnretainedReferences() -> any MTLIOCommandBuffer
```

## See Also

### Creating a input/output command buffer

- [- commandBuffer](<makecommandbuffer().md>) — Creates an input/output command buffer for the command queue.
