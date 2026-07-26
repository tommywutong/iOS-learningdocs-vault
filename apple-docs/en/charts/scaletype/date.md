---
title: date
framework: Swift Charts
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/charts/scaletype/date
source_url: 'https://developer.apple.com/documentation/charts/scaletype/date'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/charts/scaletype/date.json'
content_hash: 'sha256:6e5a4ce7fe871218'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift Charts](../../charts.md) · [ScaleType](../scaletype.md)

# date

<sub>Type Property</sub>

A date scale where each range value y can be expressed as a function of the domain value x’s timestamp, with `y = a * x.timeIntervalSinceReferenceDate + b`.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var date: ScaleType { get }
```
