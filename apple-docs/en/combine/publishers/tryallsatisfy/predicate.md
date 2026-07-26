---
title: predicate
framework: Combine
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/combine/publishers/tryallsatisfy/predicate
source_url: 'https://developer.apple.com/documentation/combine/publishers/tryallsatisfy/predicate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/publishers/tryallsatisfy/predicate.json'
content_hash: 'sha256:7dcdd8b684c9fb1f'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Combine](../../../combine.md) · [Publishers](../../publishers.md) · [TryAllSatisfy](../tryallsatisfy.md)

# predicate

<sub>Instance Property</sub>

A closure that evaluates each received element.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let predicate: (Upstream.Output) throws -> Bool
```

## Discussion

Return `true` to continue, or `false` to cancel the upstream and complete. The closure may throw, in which case the publisher cancels the upstream publisher and fails with the thrown error.

## See Also

### Inspecting publisher properties

- [upstream](upstream.md) — The publisher from which this publisher receives elements.
