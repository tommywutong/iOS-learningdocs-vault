---
title: Publishers.TimeGroupingStrategy
framework: Combine
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/combine/publishers/timegroupingstrategy
source_url: 'https://developer.apple.com/documentation/combine/publishers/timegroupingstrategy'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/publishers/timegroupingstrategy.json'
content_hash: 'sha256:6fd7d049c1869153'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Combine](../../combine.md) · [Publishers](../publishers.md)

# Publishers.TimeGroupingStrategy

<sub>Enumeration</sub>

A strategy for collecting received elements.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
enum TimeGroupingStrategy<Context> where Context : Scheduler
```

## Topics

### Time groupings

- [Publishers.TimeGroupingStrategy.byTime(_:_:)](<timegroupingstrategy/bytime(____).md>) — A grouping that collects and periodically publishes items.
- [Publishers.TimeGroupingStrategy.byTimeOrCount(_:_:_:)](<timegroupingstrategy/bytimeorcount(______).md>) — A grouping that collects and publishes items periodically or when a buffer reaches a maximum size.

## See Also

### Reducing elements

- [collect()](<../publisher/collect().md>) — Collects all received elements, and emits a single array of the collection when the upstream publisher finishes.
- [collect(_:)](<../publisher/collect(__).md>) — Collects up to the specified number of elements, and then emits a single array of the collection.
- [collect(_:options:)](<../publisher/collect(__options_).md>) — Collects elements by a given time-grouping strategy, and emits a single array of the collection.
- [ignoreOutput()](<../publisher/ignoreoutput().md>) — Ignores all upstream elements, but passes along the upstream publisher’s completion state (finished or failed).
- [reduce(_:_:)](<../publisher/reduce(____).md>) — Applies a closure that collects each element of a stream and publishes a final result upon completion.
- [tryReduce(_:_:)](<../publisher/tryreduce(____).md>) — Applies an error-throwing closure that collects each element of a stream and publishes a final result upon completion.
