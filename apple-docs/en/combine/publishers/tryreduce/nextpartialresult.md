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
doc_path: /documentation/combine/publishers/tryreduce/nextpartialresult
source_url: 'https://developer.apple.com/documentation/combine/publishers/tryreduce/nextpartialresult'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/publishers/tryreduce/nextpartialresult.json'
content_hash: 'sha256:900dbed3d2f0150c'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Combine](../../../combine.md) · [Publishers](../../publishers.md) · [TryReduce](../tryreduce.md)

# nextPartialResult

<sub>Instance Property</sub>

An error-throwing closure that takes the previously-accumulated value and the next element from the upstream to produce a new value.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let nextPartialResult: (Output, Upstream.Output) throws -> Output
```

## Discussion

If this closure throws an error, the publisher fails and passes the error to its subscriber.

## See Also

### Inspecting publisher properties

- [upstream](upstream.md) — The publisher from which this publisher receives elements.
- [initial](initial.md) — The initial value provided on the first-use of the closure.
