---
title: Publishers.TryReduce
framework: Combine
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/combine/publishers/tryreduce
source_url: 'https://developer.apple.com/documentation/combine/publishers/tryreduce'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/publishers/tryreduce.json'
content_hash: 'sha256:1ad6d6a1a38428f8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Combine](../../combine.md) · [Publishers](../publishers.md)

# Publishers.TryReduce

<sub>Structure</sub>

A publisher that applies an error-throwing closure to all received elements and produces an accumulated value when the upstream publisher finishes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct TryReduce<Upstream, Output> where Upstream : Publisher
```

## Relationships

- **Conforms To**: [Publisher](../publisher.md)

## Topics

### Creating a try-reduce publisher

- [init(upstream:initial:nextPartialResult:)](<tryreduce/init(upstream_initial_nextpartialresult_).md>) — Creates a publisher that applies an error-throwing closure to all received elements and produces an accumulated value when the upstream publisher finishes.

### Declaring supporting types

- [Output](output.md) — A publisher that publishes elements specified by a range in the sequence of published elements.
- [Failure](tryreduce/failure.md) — The kind of errors this publisher might publish.

### Inspecting publisher properties

- [upstream](tryreduce/upstream.md) — The publisher from which this publisher receives elements.
- [initial](tryreduce/initial.md) — The initial value provided on the first-use of the closure.
- [nextPartialResult](tryreduce/nextpartialresult.md) — An error-throwing closure that takes the previously-accumulated value and the next element from the upstream to produce a new value.

## See Also

### Reducing elements

- [Collect](collect.md) — A publisher that buffers items.
- [CollectByCount](collectbycount.md) — A publisher that buffers a maximum number of items.
- [CollectByTime](collectbytime.md) — A publisher that buffers and periodically publishes its items.
- [TimeGroupingStrategy](timegroupingstrategy.md) — A strategy for collecting received elements.
- [IgnoreOutput](ignoreoutput.md) — A publisher that ignores all upstream elements, but passes along the upstream publisher’s completion state (finished or failed).
- [Reduce](reduce.md) — A publisher that applies a closure to all received elements and produces an accumulated value when the upstream publisher finishes.
