---
title: Publishers.Buffer
framework: Combine
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/combine/publishers/buffer
source_url: 'https://developer.apple.com/documentation/combine/publishers/buffer'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/publishers/buffer.json'
content_hash: 'sha256:b495b05ffbf5c4f5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Combine](../../combine.md) · [Publishers](../publishers.md)

# Publishers.Buffer

<sub>Structure</sub>

A publisher that buffers elements from an upstream publisher.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct Buffer<Upstream> where Upstream : Publisher
```

## Relationships

- **Conforms To**: [Publisher](../publisher.md)

## Topics

### Creating a buffer publisher

- [init(upstream:size:prefetch:whenFull:)](<buffer/init(upstream_size_prefetch_whenfull_).md>) — Creates a publisher that buffers elements received from an upstream publisher.

### Declaring supporting types

- [Output](buffer/output.md) — The kind of values published by this publisher.
- [Failure](buffer/failure.md) — The kind of errors this publisher might publish.

### Inspecting publisher properties

- [upstream](buffer/upstream.md) — The publisher from which this publisher receives elements.
- [size](buffer/size.md) — The maximum number of elements to store.
- [prefetch](buffer/prefetch.md) — The strategy for initially populating the buffer.
- [whenFull](buffer/whenfull.md) — The action to take when the buffer becomes full.

## See Also

### Buffering elements

- [BufferingStrategy](bufferingstrategy.md) — A strategy that handles exhaustion of a buffer’s capacity.
- [PrefetchStrategy](prefetchstrategy.md) — A strategy for filling a buffer.
