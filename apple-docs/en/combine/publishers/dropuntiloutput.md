---
title: Publishers.DropUntilOutput
framework: Combine
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/combine/publishers/dropuntiloutput
source_url: 'https://developer.apple.com/documentation/combine/publishers/dropuntiloutput'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/publishers/dropuntiloutput.json'
content_hash: 'sha256:9374b197768ac2b1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Combine](../../combine.md) · [Publishers](../publishers.md)

# Publishers.DropUntilOutput

<sub>Structure</sub>

A publisher that ignores elements from the upstream publisher until it receives an element from second publisher.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct DropUntilOutput<Upstream, Other> where Upstream : Publisher, Other : Publisher, Upstream.Failure == Other.Failure
```

## Relationships

- **Conforms To**: [Equatable](../../swift/equatable.md), [Publisher](../publisher.md)

## Topics

### Creating a drop until output publisher

- [init(upstream:other:)](<dropuntiloutput/init(upstream_other_).md>) — Creates a publisher that ignores elements from the upstream publisher until it receives an element from another publisher.

### Declaring supporting types

- [Output](dropuntiloutput/output.md) — The kind of values published by this publisher.
- [Failure](dropuntiloutput/failure.md) — The kind of errors this publisher might publish.

### Inspecting publisher properties

- [upstream](dropuntiloutput/upstream.md) — The publisher from which this publisher receives its elements.
- [other](dropuntiloutput/other.md) — A publisher to monitor for its first emitted element.

### Comparing publishers

- [==(_:_:)](<dropuntiloutput/==(____).md>) — Returns a Boolean value that indicates whether two publishers are equivalent.

### Default Implementations

- [Equatable Implementations](dropuntiloutput/equatable-implementations.md)

## See Also

### Applying sequence operations to elements

- [Drop](drop.md) — A publisher that omits a specified number of elements before republishing later elements.
- [DropWhile](dropwhile.md) — A publisher that omits elements from an upstream publisher until a given closure returns false.
- [TryDropWhile](trydropwhile.md) — A publisher that omits elements from an upstream publisher until a given error-throwing closure returns false.
- [Concatenate](concatenate.md) — A publisher that emits all of one publisher’s elements before those from another publisher.
- [PrefixWhile](prefixwhile.md) — A publisher that republishes elements while a predicate closure indicates publishing should continue.
- [TryPrefixWhile](tryprefixwhile.md) — A publisher that republishes elements while an error-throwing predicate closure indicates publishing should continue.
- [PrefixUntilOutput](prefixuntiloutput.md) — A publisher that republishes elements until another publisher emits an element.
