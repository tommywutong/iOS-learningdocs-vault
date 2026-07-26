---
title: 'automatic(includesZero:reversed:)'
framework: Swift Charts
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/charts/scaledomain/automatic(includeszero:reversed:)'
source_url: 'https://developer.apple.com/documentation/charts/scaledomain/automatic(includeszero:reversed:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/charts/scaledomain/automatic%28includeszero%3Areversed%3A%29.json'
content_hash: 'sha256:96e5a4de6fe78887'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift Charts](../../charts.md) · [ScaleDomain](../scaledomain.md)

# automatic(includesZero:reversed:)

<sub>Type Method</sub>

Creates a scale domain configuration that infers the scale domain from data.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func automatic(includesZero: Bool? = nil, reversed: Bool? = nil) -> AutomaticScaleDomain
```

## Parameters

- `includesZero` — Whether the scale domain should include zero (only applicable for numerical values).

- `reversed` — Whether the scale domain should be reversed (e.g., 100 … 0).
