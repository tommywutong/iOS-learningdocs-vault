---
title: Publishers.Concatenate
framework: Combine
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/combine/publishers/concatenate
source_url: 'https://developer.apple.com/documentation/combine/publishers/concatenate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/publishers/concatenate.json'
content_hash: 'sha256:7c84f2a859cf2277'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Combine](../../combine.md) · [Publishers](../publishers.md)

# Publishers.Concatenate

<sub>Structure</sub>

A publisher that emits all of one publisher’s elements before those from another publisher.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct Concatenate<Prefix, Suffix> where Prefix : Publisher, Suffix : Publisher, Prefix.Failure == Suffix.Failure, Prefix.Output == Suffix.Output
```

## Relationships

- **Conforms To**: [Equatable](../../swift/equatable.md), [Publisher](../publisher.md)

## Topics

### Creating a concatenate publisher

- [init(prefix:suffix:)](<concatenate/init(prefix_suffix_).md>) — Creates a publisher that emits all of one publisher’s elements before those from another publisher.

### Declaring supporting types

- [Output](concatenate/output.md) — The kind of values published by this publisher.
- [Failure](concatenate/failure.md) — The kind of errors this publisher might publish.

### Inspecting publisher properties

- [prefix](concatenate/prefix.md) — The publisher to republish, in its entirety, before republishing elements from `suffix`.
- [suffix](concatenate/suffix.md) — The publisher to republish only after `prefix` finishes.

### Comparing publishers

- [==(_:_:)](<concatenate/==(____).md>) — Returns a Boolean value that indicates whether two publishers are equivalent.

### Default Implementations

- [Equatable Implementations](concatenate/equatable-implementations.md)

## See Also

### Applying sequence operations to elements

- [DropUntilOutput](dropuntiloutput.md) — A publisher that ignores elements from the upstream publisher until it receives an element from second publisher.
- [Drop](drop.md) — A publisher that omits a specified number of elements before republishing later elements.
- [DropWhile](dropwhile.md) — A publisher that omits elements from an upstream publisher until a given closure returns false.
- [TryDropWhile](trydropwhile.md) — A publisher that omits elements from an upstream publisher until a given error-throwing closure returns false.
- [PrefixWhile](prefixwhile.md) — A publisher that republishes elements while a predicate closure indicates publishing should continue.
- [TryPrefixWhile](tryprefixwhile.md) — A publisher that republishes elements while an error-throwing predicate closure indicates publishing should continue.
- [PrefixUntilOutput](prefixuntiloutput.md) — A publisher that republishes elements until another publisher emits an element.
