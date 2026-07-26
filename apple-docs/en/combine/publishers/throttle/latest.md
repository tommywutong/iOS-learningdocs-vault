---
title: latest
framework: Combine
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/combine/publishers/throttle/latest
source_url: 'https://developer.apple.com/documentation/combine/publishers/throttle/latest'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/publishers/throttle/latest.json'
content_hash: 'sha256:1a365adc0e784c09'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Combine](../../../combine.md) · [Publishers](../../publishers.md) · [Throttle](../throttle.md)

# latest

<sub>Instance Property</sub>

A Boolean value indicating whether to publish the most recent element.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let latest: Bool
```

## Discussion

If `false`, the publisher emits the first element received during the interval.

## See Also

### Inspecting publisher properties

- [upstream](upstream.md) — The publisher from which this publisher receives elements.
- [interval](interval.md) — The interval in which to find and emit the most recent element.
- [scheduler](scheduler.md) — The scheduler on which to publish elements.
