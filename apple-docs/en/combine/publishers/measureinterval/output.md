---
title: Publishers.MeasureInterval.Output
framework: Combine
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/combine/publishers/measureinterval/output
source_url: 'https://developer.apple.com/documentation/combine/publishers/measureinterval/output'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/publishers/measureinterval/output.json'
content_hash: 'sha256:de9e2209d61b8907'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Combine](../../../combine.md) · [Publishers](../../publishers.md) · [MeasureInterval](../measureinterval.md)

# Publishers.MeasureInterval.Output

<sub>Type Alias</sub>

The kind of values published by this publisher.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
typealias Output = Context.SchedulerTimeType.Stride
```

## Discussion

This publisher produces elements of the provided scheduler’s time type’s stride.

## See Also

### Declaring supporting types

- [Failure](failure.md) — The kind of errors this publisher might publish.
