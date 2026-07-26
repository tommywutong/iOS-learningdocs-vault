---
title: transform
framework: Combine
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/combine/publishers/trycompactmap/transform
source_url: 'https://developer.apple.com/documentation/combine/publishers/trycompactmap/transform'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/publishers/trycompactmap/transform.json'
content_hash: 'sha256:1604a16efff22395'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Combine](../../../combine.md) · [Publishers](../../publishers.md) · [TryCompactMap](../trycompactmap.md)

# transform

<sub>Instance Property</sub>

An error-throwing closure that receives values from the upstream publisher and returns optional values.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let transform: (Upstream.Output) throws -> Output?
```

## Discussion

If this closure throws an error, the publisher fails.

## See Also

### Inspecting publisher properties

- [upstream](upstream.md) — The publisher from which this publisher receives elements.
