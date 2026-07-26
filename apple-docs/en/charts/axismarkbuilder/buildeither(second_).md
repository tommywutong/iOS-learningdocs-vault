---
title: 'buildEither(second:)'
framework: Swift Charts
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/charts/axismarkbuilder/buildeither(second:)'
source_url: 'https://developer.apple.com/documentation/charts/axismarkbuilder/buildeither(second:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/charts/axismarkbuilder/buildeither%28second%3A%29.json'
content_hash: 'sha256:f96ed41f58796c95'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift Charts](../../charts.md) · [AxisMarkBuilder](../axismarkbuilder.md)

# buildEither(second:)

<sub>Type Method</sub>

Provides support for “if-else” statements in multi-statement closures, producing conditional content for the “else” branch.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func buildEither<T1, T2>(second: T2) -> BuilderConditional<T1, T2> where T1 : AxisMark, T2 : AxisMark
```
