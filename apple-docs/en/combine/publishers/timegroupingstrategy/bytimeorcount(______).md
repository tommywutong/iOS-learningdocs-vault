---
title: 'Publishers.TimeGroupingStrategy.byTimeOrCount(_:_:_:)'
framework: Combine
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/combine/publishers/timegroupingstrategy/bytimeorcount(_:_:_:)'
source_url: 'https://developer.apple.com/documentation/combine/publishers/timegroupingstrategy/bytimeorcount(_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/publishers/timegroupingstrategy/bytimeorcount%28_%3A_%3A_%3A%29.json'
content_hash: 'sha256:e97af4e1eab1091e'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Combine](../../../combine.md) · [Publishers](../../publishers.md) · [TimeGroupingStrategy](../timegroupingstrategy.md)

# Publishers.TimeGroupingStrategy.byTimeOrCount(_:_:_:)

<sub>Case</sub>

A grouping that collects and publishes items periodically or when a buffer reaches a maximum size.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case byTimeOrCount(Context, Context.SchedulerTimeType.Stride, Int)
```

## See Also

### Time groupings

- [Publishers.TimeGroupingStrategy.byTime(_:_:)](<bytime(____).md>) — A grouping that collects and periodically publishes items.
