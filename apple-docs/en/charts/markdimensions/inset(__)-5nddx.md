---
title: 'inset(_:)'
framework: Swift Charts
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/charts/markdimensions/inset(_:)-5nddx'
source_url: 'https://developer.apple.com/documentation/charts/markdimensions/inset(_:)-5nddx'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/charts/markdimensions/inset%28_%3A%29-5nddx.json'
content_hash: 'sha256:afcda2b5482b1017'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift Charts](../../charts.md) · [MarkDimensions](../markdimensions.md)

# inset(_:)

<sub>Type Method</sub>

A dimension that’s the step size minus the specified inset value on each side.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func inset(_ value: CGFloat) -> MarkDimensions<DataElement>
```

## Parameters

- `value` — The given inset value in screen coordinates.
