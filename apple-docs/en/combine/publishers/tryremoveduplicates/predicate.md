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
doc_path: /documentation/combine/publishers/tryremoveduplicates/predicate
source_url: 'https://developer.apple.com/documentation/combine/publishers/tryremoveduplicates/predicate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/publishers/tryremoveduplicates/predicate.json'
content_hash: 'sha256:218cb1b9e4f93e1c'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Combine](../../../combine.md) · [Publishers](../../publishers.md) · [TryRemoveDuplicates](../tryremoveduplicates.md)

# predicate

<sub>Instance Property</sub>

An error-throwing closure to evaluate whether two elements are equivalent, for purposes of filtering.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let predicate: (Publishers.TryRemoveDuplicates<Upstream>.Output, Publishers.TryRemoveDuplicates<Upstream>.Output) throws -> Bool
```

## See Also

### Inspecting publisher properties

- [upstream](upstream.md) — The publisher from which this publisher receives elements.
