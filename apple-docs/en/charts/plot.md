---
title: Plot
framework: Swift Charts
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/charts/plot
source_url: 'https://developer.apple.com/documentation/charts/plot'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/charts/plot.json'
content_hash: 'sha256:483adb2c92d8e98c'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Swift Charts](../charts.md)

# Plot

<sub>Structure</sub>

A mechanism for grouping chart contents into a single entity.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@MainActor @preconcurrency struct Plot<Content> where Content : ChartContent
```

## Relationships

- **Conforms To**: [ChartContent](chartcontent.md), [Copyable](../swift/copyable.md), [Escapable](../swift/escapable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Initializers

- [init(content:)](<plot/init(content_).md>)

## See Also

### Charts

- [Creating a chart using Swift Charts](creating-a-chart-using-swift-charts.md) — Make a chart by combining chart building blocks in SwiftUI.
- [Visualizing your app’s data](visualizing-your-app-s-data.md) — Build complex and interactive charts using Swift Charts.
- [Chart](chart.md) — A SwiftUI view that displays a chart.
- [ChartContent](chartcontent.md) — A type that represents the content that you draw on a chart.
- [ChartContentBuilder](chartcontentbuilder.md) — A result builder that you use to compose the contents of a chart.
