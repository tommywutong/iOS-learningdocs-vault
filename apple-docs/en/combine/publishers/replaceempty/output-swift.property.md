---
title: output
framework: Combine
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/combine/publishers/replaceempty/output-swift.property
source_url: 'https://developer.apple.com/documentation/combine/publishers/replaceempty/output-swift.property'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/publishers/replaceempty/output-swift.property.json'
content_hash: 'sha256:9612f1a8473aa95b'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Combine](../../../combine.md) · [Publishers](../../publishers.md) · [ReplaceEmpty](../replaceempty.md)

# output

<sub>Instance Property</sub>

The element to deliver when the upstream publisher finishes without delivering any elements.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let output: Publishers.ReplaceEmpty<Upstream>.Output
```

## See Also

### Inspecting publisher properties

- [upstream](upstream.md) — The publisher from which this publisher receives elements.
