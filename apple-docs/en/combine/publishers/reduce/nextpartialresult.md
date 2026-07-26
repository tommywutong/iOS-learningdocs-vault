---
title: nextPartialResult
framework: Combine
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/combine/publishers/reduce/nextpartialresult
source_url: 'https://developer.apple.com/documentation/combine/publishers/reduce/nextpartialresult'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/publishers/reduce/nextpartialresult.json'
content_hash: 'sha256:82d83d387fae0e2a'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Combine](../../../combine.md) · [Publishers](../../publishers.md) · [Reduce](../reduce.md)

# nextPartialResult

<sub>Instance Property</sub>

A closure that takes the previously-accumulated value and the next element from the upstream publisher to produce a new value.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let nextPartialResult: (Output, Upstream.Output) -> Output
```

## See Also

### Inspecting publisher properties

- [upstream](upstream.md) — The publisher from which this publisher receives elements.
- [initial](initial.md) — The initial value provided on the first invocation of the closure.
