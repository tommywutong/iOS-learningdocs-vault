---
title: mutability
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 11.0+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlpipelinebufferdescriptor/mutability
source_url: 'https://developer.apple.com/documentation/metal/mtlpipelinebufferdescriptor/mutability'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlpipelinebufferdescriptor/mutability.json'
content_hash: 'sha256:e142b1ab80275ede'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLPipelineBufferDescriptor](../mtlpipelinebufferdescriptor.md)

# mutability

<sub>Instance Property</sub>

A mutability option that determines whether you can update a buffer’s contents before related commands use the buffer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var mutability: MTLMutability { get set }
```

## Discussion

The default value is [MTLMutabilityDefault](../mtlmutability/default.md).

If you don’t explicitly declare mutability, Metal uses the following default behaviors:

- Regular buffers are mutable by default, and Metal treats [MTLMutabilityDefault](../mtlmutability/default.md) as if it were [MTLMutabilityMutable](../mtlmutability/mutable.md).
- Argument buffers are immutable by default, and Metal treats [MTLMutabilityDefault](../mtlmutability/default.md) as if it were [MTLMutabilityImmutable](../mtlmutability/immutable.md).

## See Also

### Setting buffer mutability

- [MTLMutability](../mtlmutability.md) — The options that determine the mutability of a buffer’s contents.
