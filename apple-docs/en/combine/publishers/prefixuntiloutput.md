---
title: Publishers.PrefixUntilOutput
framework: Combine
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/combine/publishers/prefixuntiloutput
source_url: 'https://developer.apple.com/documentation/combine/publishers/prefixuntiloutput'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/publishers/prefixuntiloutput.json'
content_hash: 'sha256:bc733855d69bf3ca'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Combine](../../combine.md) · [Publishers](../publishers.md)

# Publishers.PrefixUntilOutput

<sub>Structure</sub>

A publisher that republishes elements until another publisher emits an element.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct PrefixUntilOutput<Upstream, Other> where Upstream : Publisher, Other : Publisher
```

## Relationships

- **Conforms To**: [Publisher](../publisher.md)

## Topics

### Creating a prefix until output publisher

- [init(upstream:other:)](<prefixuntiloutput/init(upstream_other_).md>) — Creates a publisher that republishes elements until another publisher emits an element.

### Declaring supporting types

- [Output](prefixuntiloutput/output.md) — The kind of values published by this publisher.
- [Failure](prefixuntiloutput/failure.md) — The kind of errors this publisher might publish.

### Inspecting publisher properties

- [upstream](prefixuntiloutput/upstream.md) — The publisher from which this publisher receives elements.
- [other](prefixuntiloutput/other.md) — Another publisher, whose first output causes this publisher to finish.

## See Also

### Applying sequence operations to elements

- [DropUntilOutput](dropuntiloutput.md) — A publisher that ignores elements from the upstream publisher until it receives an element from second publisher.
- [Drop](drop.md) — A publisher that omits a specified number of elements before republishing later elements.
- [DropWhile](dropwhile.md) — A publisher that omits elements from an upstream publisher until a given closure returns false.
- [TryDropWhile](trydropwhile.md) — A publisher that omits elements from an upstream publisher until a given error-throwing closure returns false.
- [Concatenate](concatenate.md) — A publisher that emits all of one publisher’s elements before those from another publisher.
- [PrefixWhile](prefixwhile.md) — A publisher that republishes elements while a predicate closure indicates publishing should continue.
- [TryPrefixWhile](tryprefixwhile.md) — A publisher that republishes elements while an error-throwing predicate closure indicates publishing should continue.
