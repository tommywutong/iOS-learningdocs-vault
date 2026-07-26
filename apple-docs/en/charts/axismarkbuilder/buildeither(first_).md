---
title: 'buildEither(first:)'
framework: Swift Charts
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/charts/axismarkbuilder/buildeither(first:)'
source_url: 'https://developer.apple.com/documentation/charts/axismarkbuilder/buildeither(first:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/charts/axismarkbuilder/buildeither%28first%3A%29.json'
content_hash: 'sha256:d7c9215a840752ae'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift Charts](../../charts.md) · [AxisMarkBuilder](../axismarkbuilder.md)

# buildEither(first:)

<sub>Type Method</sub>

Provides support for “if-else” statements in multi-statement closures, producing conditional content for the “then” branch.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func buildEither<T1, T2>(first: T1) -> BuilderConditional<T1, T2> where T1 : AxisMark, T2 : AxisMark
```
