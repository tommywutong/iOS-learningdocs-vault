---
title: LazyCollectionProtocol
framework: Swift
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/lazycollectionprotocol
source_url: 'https://developer.apple.com/documentation/swift/lazycollectionprotocol'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/lazycollectionprotocol.json'
content_hash: 'sha256:65080bc8f074d674'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Swift](../swift.md)

# LazyCollectionProtocol

<sub>Protocol</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
protocol LazyCollectionProtocol : Collection, LazySequenceProtocol where Self.Elements : Collection
```

## Relationships

- **Inherits From**: [Collection](collection.md), [LazySequenceProtocol](lazysequenceprotocol.md), [Sequence](sequence.md)

- **Conforming Types**: [LazyDropWhileSequence](lazydropwhilesequence.md), [LazyFilterSequence](lazyfiltersequence.md), [LazyMapSequence](lazymapsequence.md), [LazyPrefixWhileSequence](lazyprefixwhilesequence.md), [LazySequence](lazysequence.md)

## Topics

### Instance Properties

- [lazy](lazycollectionprotocol/lazy-7wmso.md)
- [lazy](lazycollectionprotocol/lazy-9k7qy.md)

## See Also

### Lazy Collections

- [LazySequenceProtocol](lazysequenceprotocol.md) — A sequence on which normally-eager sequence operations are implemented lazily.
