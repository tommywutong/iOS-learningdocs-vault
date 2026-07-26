---
title: Publishers.BufferingStrategy
framework: Combine
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/combine/publishers/bufferingstrategy
source_url: 'https://developer.apple.com/documentation/combine/publishers/bufferingstrategy'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/publishers/bufferingstrategy.json'
content_hash: 'sha256:da8d3008edd8fcbd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Combine](../../combine.md) · [Publishers](../publishers.md)

# Publishers.BufferingStrategy

<sub>Enumeration</sub>

A strategy that handles exhaustion of a buffer’s capacity.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
enum BufferingStrategy<Failure> where Failure : Error
```

## Topics

### Buffering strategies

- [Publishers.BufferingStrategy.dropNewest](bufferingstrategy/dropnewest.md) — When the buffer is full, discard the newly received element.
- [Publishers.BufferingStrategy.dropOldest](bufferingstrategy/dropoldest.md) — When the buffer is full, discard the oldest element in the buffer.
- [Publishers.BufferingStrategy.customError(_:)](<bufferingstrategy/customerror(__).md>) — When the buffer is full, execute the closure to provide a custom error.

## See Also

### Buffering elements

- [buffer(size:prefetch:whenFull:)](<../publisher/buffer(size_prefetch_whenfull_).md>) — Buffers elements received from an upstream publisher.
- [PrefetchStrategy](prefetchstrategy.md) — A strategy for filling a buffer.
