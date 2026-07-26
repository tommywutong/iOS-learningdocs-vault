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
doc_path: /documentation/combine/publishers/filter/isincluded
source_url: 'https://developer.apple.com/documentation/combine/publishers/filter/isincluded'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/publishers/filter/isincluded.json'
content_hash: 'sha256:c32ea8dc96a3ee3e'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Combine](../../../combine.md) · [Publishers](../../publishers.md) · [Filter](../filter.md)

# isIncluded

<sub>Instance Property</sub>

A closure that indicates whether to republish an element.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let isIncluded: (Upstream.Output) -> Bool
```

## See Also

### Inspecting publisher properties

- [upstream](upstream.md) — The publisher from which this publisher receives elements.
