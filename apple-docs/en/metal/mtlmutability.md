---
title: MTLMutability
framework: Metal
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 11.0+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlmutability
source_url: 'https://developer.apple.com/documentation/metal/mtlmutability'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlmutability.json'
content_hash: 'sha256:97a7057b17319fa6'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTLMutability

<sub>Enumeration</sub>

The options that determine the mutability of a buffer’s contents.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
enum MTLMutability
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Enumeration cases

- [MTLMutabilityDefault](mtlmutability/default.md) — The default behavior, based on the buffer’s type.
- [MTLMutabilityMutable](mtlmutability/mutable.md) — An option that states that you can modify the buffer’s contents.
- [MTLMutabilityImmutable](mtlmutability/immutable.md) — An option that states that you can’t modify the buffer’s contents.

### Initializers

- [init(rawValue:)](<mtlmutability/init(rawvalue_).md>)

## See Also

### Setting buffer mutability

- [mutability](mtlpipelinebufferdescriptor/mutability.md) — A mutability option that determines whether you can update a buffer’s contents before related commands use the buffer.
