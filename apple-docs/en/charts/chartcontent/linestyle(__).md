---
title: 'lineStyle(_:)'
framework: Swift Charts
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/charts/chartcontent/linestyle(_:)'
source_url: 'https://developer.apple.com/documentation/charts/chartcontent/linestyle(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/charts/chartcontent/linestyle%28_%3A%29.json'
content_hash: 'sha256:70c2e817ec1d9a30'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift Charts](../../charts.md) · [ChartContent](../chartcontent.md)

# lineStyle(_:)

<sub>Instance Method</sub>

Sets the style for line marks.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func lineStyle(_ style: StrokeStyle) -> some ChartContent

```

## Parameters

- `style` — The stroke style.

## Discussion

> [!warning] Warning
> Use this `.lineStyle(_:)` overload only if you have a predefined stroke style. The provided stroke style will override default line width and line cap for line marks.

## See Also

### Styling marks

- [foregroundStyle(_:)](<foregroundstyle(__).md>) — Sets the foreground style for the chart content.
- [opacity(_:)](<opacity(__).md>) — Sets the opacity for the chart content.
- [blur(radius:)](<blur(radius_).md>) — Applies a Gaussian blur to this chart content.
- [cornerRadius(_:style:)](<cornerradius(__style_).md>) — Sets the corner radius of the chart content.
- [shadow(color:radius:x:y:)](<shadow(color_radius_x_y_).md>) — A chart content that adds a shadow to this chart content.
- [interpolationMethod(_:)](<interpolationmethod(__).md>) — Plots line and area marks with the interpolation method that you specify.
