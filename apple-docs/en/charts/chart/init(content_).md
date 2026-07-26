---
title: 'init(content:)'
framework: Swift Charts
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/charts/chart/init(content:)'
source_url: 'https://developer.apple.com/documentation/charts/chart/init(content:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/charts/chart/init%28content%3A%29.json'
content_hash: 'sha256:38e910a52d217afd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift Charts](../../charts.md) · [Chart](../chart.md)

# init(content:)

<sub>Initializer</sub>

Creates a chart composed of any number of data series and individual marks.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated init(@ContentBuilder content: () -> Content)
```

## Parameters

- `content` — A chart content builder that returns the marks that the chart should draw.

## Discussion

This initializer draws the marks that you specify in the `content` input. You can provide individual marks, or marks produced by one or more [ForEach](../../swiftui/foreach.md) constructs, or any combination of these. As a convenience when you have exactly one `ForEach` in your chart’s content, you can use either the [init(_:content:)](<init(__content_).md>) or [init(_:id:content:)](<init(__id_content_).md>) initializer instead, either of which wraps the content in an implicit `ForEach`.

## See Also

### Creating a chart

- [init(_:content:)](<init(__content_).md>) — Creates a chart composed of a series of identifiable marks.
- [init(_:id:content:)](<init(__id_content_).md>) — Creates a chart composed of a series of marks.
