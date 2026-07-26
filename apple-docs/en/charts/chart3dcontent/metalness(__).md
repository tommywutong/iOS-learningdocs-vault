---
title: 'metalness(_:)'
framework: Swift Charts
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, visionOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/charts/chart3dcontent/metalness(_:)'
source_url: 'https://developer.apple.com/documentation/charts/chart3dcontent/metalness(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/charts/chart3dcontent/metalness%28_%3A%29.json'
content_hash: 'sha256:f2100cacff446ecc'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift Charts](../../charts.md) · [Chart3DContent](../chart3dcontent.md)

# metalness(_:)

<sub>Instance Method</sub>

A value that controls whether the surface has a metallic look.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
nonisolated func metalness(_ ratio: Double) -> some Chart3DContent

```

## Parameters

- `ratio` — The degree of metalness.

## Discussion

Zero represents a non-metallic (dielectric) surface. One represents a metallic surface. In real life, materials are either metallic or dielectric (0 or 1).
