---
title: isIncluded
framework: Combine
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/combine/publishers/tryfilter/isincluded
source_url: 'https://developer.apple.com/documentation/combine/publishers/tryfilter/isincluded'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/publishers/tryfilter/isincluded.json'
content_hash: 'sha256:60776ebc69e6d5eb'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Combine](../../../combine.md) · [Publishers](../../publishers.md) · [TryFilter](../tryfilter.md)

# isIncluded

<sub>Instance Property</sub>

An error-throwing closure that indicates whether this filter should republish an element.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let isIncluded: (Upstream.Output) throws -> Bool
```

## See Also

### Inspecting publisher properties

- [upstream](upstream.md) — The publisher from which this publisher receives elements.
