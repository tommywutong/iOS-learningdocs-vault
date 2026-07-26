---
title: upstream
framework: Combine
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/combine/publishers/tryreduce/upstream
source_url: 'https://developer.apple.com/documentation/combine/publishers/tryreduce/upstream'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/publishers/tryreduce/upstream.json'
content_hash: 'sha256:05fb2e40191709b9'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Combine](../../../combine.md) · [Publishers](../../publishers.md) · [TryReduce](../tryreduce.md)

# upstream

<sub>Instance Property</sub>

The publisher from which this publisher receives elements.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let upstream: Upstream
```

## See Also

### Inspecting publisher properties

- [initial](initial.md) — The initial value provided on the first-use of the closure.
- [nextPartialResult](nextpartialresult.md) — An error-throwing closure that takes the previously-accumulated value and the next element from the upstream to produce a new value.
