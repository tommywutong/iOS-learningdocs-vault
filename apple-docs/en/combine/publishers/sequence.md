---
title: Publishers.Sequence
framework: Combine
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/combine/publishers/sequence
source_url: 'https://developer.apple.com/documentation/combine/publishers/sequence'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/publishers/sequence.json'
content_hash: 'sha256:e62a390bbc24432e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Combine](../../combine.md) · [Publishers](../publishers.md)

# Publishers.Sequence

<sub>Structure</sub>

A publisher that publishes a given sequence of elements.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct Sequence<Elements, Failure> where Elements : Sequence, Failure : Error
```

## Overview

When the publisher exhausts the elements in the sequence, the next request causes the publisher to finish.

## Relationships

- **Conforms To**: [Equatable](../../swift/equatable.md), [Publisher](../publisher.md)

## Topics

### Creating a sequence publisher

- [init(sequence:)](<sequence/init(sequence_).md>) — Creates a publisher for a sequence of elements.

### Declaring supporting types

- [Output](output.md) — A publisher that publishes elements specified by a range in the sequence of published elements.

### Inspecting publisher properties

- [sequence](sequence/sequence.md) — The sequence of elements to publish.

### Comparing publishers

- [==(_:_:)](<sequence/==(____).md>) — Returns a Boolean value that indicates whether two publishers are equivalent.

### Applying Operators

- [Publisher Operators](../publishers-sequence-publisher-operators.md) — Methods that create downstream publishers or subscribers to act on the elements they receive.

### Default Implementations

- [Equatable Implementations](sequence/equatable-implementations.md)

## See Also

### Convenience publishers

- [Catch](catch.md) — A publisher that handles errors from an upstream publisher by replacing the failed publisher with another publisher.
