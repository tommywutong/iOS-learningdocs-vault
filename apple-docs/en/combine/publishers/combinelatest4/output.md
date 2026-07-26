---
title: Publishers.CombineLatest4.Output
framework: Combine
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/combine/publishers/combinelatest4/output
source_url: 'https://developer.apple.com/documentation/combine/publishers/combinelatest4/output'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/publishers/combinelatest4/output.json'
content_hash: 'sha256:5bc88abcb9ca38a3'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Combine](../../../combine.md) · [Publishers](../../publishers.md) · [CombineLatest4](../combinelatest4.md)

# Publishers.CombineLatest4.Output

<sub>Type Alias</sub>

The kind of values published by this publisher.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
typealias Output = (A.Output, B.Output, C.Output, D.Output)
```

## Discussion

This publisher produces four-element tuples of the upstream publishers’ output types.

## See Also

### Declaring supporting types

- [Failure](failure.md) — The kind of errors this publisher might publish.
