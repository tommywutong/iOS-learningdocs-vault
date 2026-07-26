---
title: Publishers.Zip3.Output
framework: Combine
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/combine/publishers/zip3/output
source_url: 'https://developer.apple.com/documentation/combine/publishers/zip3/output'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/publishers/zip3/output.json'
content_hash: 'sha256:85e5055d4fe0b6a4'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Combine](../../../combine.md) · [Publishers](../../publishers.md) · [Zip3](../zip3.md)

# Publishers.Zip3.Output

<sub>Type Alias</sub>

The kind of values published by this publisher.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
typealias Output = (A.Output, B.Output, C.Output)
```

## Discussion

This publisher produces three-element tuples, whose members’ types correspond to the types produced by the upstream publishers.

## See Also

### Declaring supporting types

- [Failure](failure.md) — The kind of errors this publisher might publish.
