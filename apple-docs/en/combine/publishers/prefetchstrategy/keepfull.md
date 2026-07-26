---
title: Publishers.PrefetchStrategy.keepFull
framework: Combine
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/combine/publishers/prefetchstrategy/keepfull
source_url: 'https://developer.apple.com/documentation/combine/publishers/prefetchstrategy/keepfull'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/publishers/prefetchstrategy/keepfull.json'
content_hash: 'sha256:5d3189b60c3ebbb3'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Combine](../../../combine.md) · [Publishers](../../publishers.md) · [PrefetchStrategy](../prefetchstrategy.md)

# Publishers.PrefetchStrategy.keepFull

<sub>Case</sub>

A strategy to fill the buffer at subscription time, and keep it full thereafter.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case keepFull
```

## Discussion

This strategy starts by making a demand equal to the buffer’s size from the upstream when the subscriber first connects. Afterwards, it continues to demand elements from the upstream to try to keep the buffer full.

## See Also

### Prefetching strategies

- [Publishers.PrefetchStrategy.byRequest](byrequest.md) — A strategy that avoids prefetching and instead performs requests on demand.
