---
title: Publishers.PrefetchStrategy
framework: Combine
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/combine/publishers/prefetchstrategy
source_url: 'https://developer.apple.com/documentation/combine/publishers/prefetchstrategy'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/publishers/prefetchstrategy.json'
content_hash: 'sha256:7a626654847f85fe'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Combine](../../combine.md) · [Publishers](../publishers.md)

# Publishers.PrefetchStrategy

<sub>Enumeration</sub>

A strategy for filling a buffer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
enum PrefetchStrategy
```

## Relationships

- **Conforms To**: [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md)

## Topics

### Prefetching strategies

- [Publishers.PrefetchStrategy.byRequest](prefetchstrategy/byrequest.md) — A strategy that avoids prefetching and instead performs requests on demand.
- [Publishers.PrefetchStrategy.keepFull](prefetchstrategy/keepfull.md) — A strategy to fill the buffer at subscription time, and keep it full thereafter.

## See Also

### Buffering elements

- [buffer(size:prefetch:whenFull:)](<../publisher/buffer(size_prefetch_whenfull_).md>) — Buffers elements received from an upstream publisher.
- [BufferingStrategy](bufferingstrategy.md) — A strategy that handles exhaustion of a buffer’s capacity.
