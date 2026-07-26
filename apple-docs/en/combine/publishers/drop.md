---
title: Publishers.Drop
framework: Combine
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/combine/publishers/drop
source_url: 'https://developer.apple.com/documentation/combine/publishers/drop'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/publishers/drop.json'
content_hash: 'sha256:44e27c3f05e58853'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Combine](../../combine.md) · [Publishers](../publishers.md)

# Publishers.Drop

<sub>Structure</sub>

A publisher that omits a specified number of elements before republishing later elements.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct Drop<Upstream> where Upstream : Publisher
```

## Relationships

- **Conforms To**: [Equatable](../../swift/equatable.md), [Publisher](../publisher.md)

## Topics

### Creating a drop Publisher

- [init(upstream:count:)](<drop/init(upstream_count_).md>) — Creates a publisher that omits a specified number of elements before republishing later elements.

### Declaring supporting types

- [Output](drop/output.md) — The kind of values published by this publisher.
- [Failure](drop/failure.md) — The kind of errors this publisher might publish.

### Inspecting publisher properties

- [upstream](drop/upstream.md) — The publisher from which this publisher receives elements.
- [count](drop/count.md) — The number of elements to drop.

### Comparing publishers

- [==(_:_:)](<drop/==(____).md>) — Returns a Boolean value that indicates whether two publishers are equivalent.

### Default Implementations

- [Equatable Implementations](drop/equatable-implementations.md)

## See Also

### Applying sequence operations to elements

- [DropUntilOutput](dropuntiloutput.md) — A publisher that ignores elements from the upstream publisher until it receives an element from second publisher.
- [DropWhile](dropwhile.md) — A publisher that omits elements from an upstream publisher until a given closure returns false.
- [TryDropWhile](trydropwhile.md) — A publisher that omits elements from an upstream publisher until a given error-throwing closure returns false.
- [Concatenate](concatenate.md) — A publisher that emits all of one publisher’s elements before those from another publisher.
- [PrefixWhile](prefixwhile.md) — A publisher that republishes elements while a predicate closure indicates publishing should continue.
- [TryPrefixWhile](tryprefixwhile.md) — A publisher that republishes elements while an error-throwing predicate closure indicates publishing should continue.
- [PrefixUntilOutput](prefixuntiloutput.md) — A publisher that republishes elements until another publisher emits an element.
