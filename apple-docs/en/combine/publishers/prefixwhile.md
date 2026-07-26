---
title: Publishers.PrefixWhile
framework: Combine
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/combine/publishers/prefixwhile
source_url: 'https://developer.apple.com/documentation/combine/publishers/prefixwhile'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/publishers/prefixwhile.json'
content_hash: 'sha256:e8ccd5ecc1ce5aee'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Combine](../../combine.md) · [Publishers](../publishers.md)

# Publishers.PrefixWhile

<sub>Structure</sub>

A publisher that republishes elements while a predicate closure indicates publishing should continue.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct PrefixWhile<Upstream> where Upstream : Publisher
```

## Relationships

- **Conforms To**: [Publisher](../publisher.md)

## Topics

### Creating a prefix while publisher

- [init(upstream:predicate:)](<prefixwhile/init(upstream_predicate_).md>) — Creates a publisher that republishes elements while a predicate closure indicates publishing should continue.

### Declaring supporting types

- [Output](prefixwhile/output.md) — The kind of values published by this publisher.
- [Failure](prefixwhile/failure.md) — The kind of errors this publisher might publish.

### Inspecting publisher properties

- [upstream](prefixwhile/upstream.md) — The publisher from which this publisher receives elements.
- [predicate](prefixwhile/predicate.md) — The closure that determines whether publishing should continue.

## See Also

### Applying sequence operations to elements

- [DropUntilOutput](dropuntiloutput.md) — A publisher that ignores elements from the upstream publisher until it receives an element from second publisher.
- [Drop](drop.md) — A publisher that omits a specified number of elements before republishing later elements.
- [DropWhile](dropwhile.md) — A publisher that omits elements from an upstream publisher until a given closure returns false.
- [TryDropWhile](trydropwhile.md) — A publisher that omits elements from an upstream publisher until a given error-throwing closure returns false.
- [Concatenate](concatenate.md) — A publisher that emits all of one publisher’s elements before those from another publisher.
- [TryPrefixWhile](tryprefixwhile.md) — A publisher that republishes elements while an error-throwing predicate closure indicates publishing should continue.
- [PrefixUntilOutput](prefixuntiloutput.md) — A publisher that republishes elements until another publisher emits an element.
