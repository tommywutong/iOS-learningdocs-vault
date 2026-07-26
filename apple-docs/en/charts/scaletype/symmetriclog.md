---
title: symmetricLog
framework: Swift Charts
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 16.4+, iPadOS 16.4+, Mac Catalyst 16.4+, macOS 13.3+, tvOS 16.4+, visionOS 1.0+, watchOS 9.4+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/charts/scaletype/symmetriclog
source_url: 'https://developer.apple.com/documentation/charts/scaletype/symmetriclog'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/charts/scaletype/symmetriclog.json'
content_hash: 'sha256:36a4a94e0eba44aa'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift Charts](../../charts.md) · [ScaleType](../scaletype.md)

# symmetricLog

<sub>Type Property</sub>

A number scale where each range value y can be expressed as a symmetric log function of the domain value x, with `y = a * sign(x) * log(1 + |x * slopeAtZero|) + b`. The constant `slopeAtZero` defaults to 1. You can configure it with `symmetricLog(slopeAtZero:)`.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var symmetricLog: ScaleType { get }
```
