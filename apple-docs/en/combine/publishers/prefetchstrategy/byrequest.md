---
title: Publishers.PrefetchStrategy.byRequest
framework: Combine
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/combine/publishers/prefetchstrategy/byrequest
source_url: 'https://developer.apple.com/documentation/combine/publishers/prefetchstrategy/byrequest'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/publishers/prefetchstrategy/byrequest.json'
content_hash: 'sha256:d9c11fce0656cf50'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Combine](../../../combine.md) · [Publishers](../../publishers.md) · [PrefetchStrategy](../prefetchstrategy.md)

# Publishers.PrefetchStrategy.byRequest

<sub>Case</sub>

A strategy that avoids prefetching and instead performs requests on demand.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case byRequest
```

## Discussion

This strategy just forwards the downstream’s requests to the upstream publisher.

## See Also

### Prefetching strategies

- [Publishers.PrefetchStrategy.keepFull](keepfull.md) — A strategy to fill the buffer at subscription time, and keep it full thereafter.
