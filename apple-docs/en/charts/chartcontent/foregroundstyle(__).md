---
title: 'foregroundStyle(_:)'
framework: Swift Charts
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/charts/chartcontent/foregroundstyle(_:)'
source_url: 'https://developer.apple.com/documentation/charts/chartcontent/foregroundstyle(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/charts/chartcontent/foregroundstyle%28_%3A%29.json'
content_hash: 'sha256:7232c975de9db54c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift Charts](../../charts.md) · [ChartContent](../chartcontent.md)

# foregroundStyle(_:)

<sub>Instance Method</sub>

Sets the foreground style for the chart content.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func foregroundStyle<S>(_ style: S) -> some ChartContent where S : ShapeStyle

```

## Parameters

- `style` — The shape style.

## See Also

### Styling marks

- [opacity(_:)](<opacity(__).md>) — Sets the opacity for the chart content.
- [blur(radius:)](<blur(radius_).md>) — Applies a Gaussian blur to this chart content.
- [cornerRadius(_:style:)](<cornerradius(__style_).md>) — Sets the corner radius of the chart content.
- [lineStyle(_:)](<linestyle(__).md>) — Sets the style for line marks.
- [shadow(color:radius:x:y:)](<shadow(color_radius_x_y_).md>) — A chart content that adds a shadow to this chart content.
- [interpolationMethod(_:)](<interpolationmethod(__).md>) — Plots line and area marks with the interpolation method that you specify.
