---
title: squareRoot
framework: Swift Charts
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 16.4+, iPadOS 16.4+, Mac Catalyst 16.4+, macOS 13.3+, tvOS 16.4+, visionOS 1.0+, watchOS 9.4+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/charts/scaletype/squareroot
source_url: 'https://developer.apple.com/documentation/charts/scaletype/squareroot'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/charts/scaletype/squareroot.json'
content_hash: 'sha256:dc6a412179ddf310'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift Charts](../../charts.md) · [ScaleType](../scaletype.md)

# squareRoot

<sub>Type Property</sub>

A number scale where each range value y can be expressed as a square root function of the domain value x, with `y = a * sqrt(x) + b`. This is equivalent to a power scale with exponent 0.5.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var squareRoot: ScaleType { get }
```
