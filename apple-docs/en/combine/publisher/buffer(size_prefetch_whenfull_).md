---
title: 'buffer(size:prefetch:whenFull:)'
framework: Combine
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/combine/publisher/buffer(size:prefetch:whenfull:)'
source_url: 'https://developer.apple.com/documentation/combine/publisher/buffer(size:prefetch:whenfull:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/publisher/buffer%28size%3Aprefetch%3Awhenfull%3A%29.json'
content_hash: 'sha256:523983af0cfb0622'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Combine](../../combine.md) · [Publisher](../publisher.md)

# buffer(size:prefetch:whenFull:)

<sub>Instance Method</sub>

Buffers elements received from an upstream publisher.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func buffer(size: Int, prefetch: Publishers.PrefetchStrategy, whenFull: Publishers.BufferingStrategy<Self.Failure>) -> Publishers.Buffer<Self>
```

## Parameters

- `size` — The maximum number of elements to store.

- `prefetch` — The strategy to initially populate the buffer.

- `whenFull` — The action to take when the buffer becomes full.

## Return Value

A publisher that buffers elements received from an upstream publisher.

## Discussion

Use [buffer(size:prefetch:whenFull:)](<buffer(size_prefetch_whenfull_).md>) to collect a specific number of elements from an upstream publisher before republishing them to the downstream subscriber according to the [BufferingStrategy](../publishers/bufferingstrategy.md) and [PrefetchStrategy](../publishers/prefetchstrategy.md) strategy you specify.

If the publisher completes before reaching the `size` threshold, it buffers the elements and publishes them downstream prior to completion.

## See Also

### Buffering elements

- [PrefetchStrategy](../publishers/prefetchstrategy.md) — A strategy for filling a buffer.
- [BufferingStrategy](../publishers/bufferingstrategy.md) — A strategy that handles exhaustion of a buffer’s capacity.
