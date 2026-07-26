---
title: 'cornerRadius(_:style:)'
framework: Swift Charts
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/charts/chartcontent/cornerradius(_:style:)'
source_url: 'https://developer.apple.com/documentation/charts/chartcontent/cornerradius(_:style:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/charts/chartcontent/cornerradius%28_%3Astyle%3A%29.json'
content_hash: 'sha256:7cf221409abc3f3d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift Charts](../../charts.md) · [ChartContent](../chartcontent.md)

# cornerRadius(_:style:)

<sub>Instance Method</sub>

Sets the corner radius of the chart content.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func cornerRadius(_ radius: CGFloat, style: RoundedCornerStyle = .continuous) -> some ChartContent

```

## Parameters

- `radius` — The corner radius.

- `style` — The style of the rounded corners.

## See Also

### Styling marks

- [foregroundStyle(_:)](<foregroundstyle(__).md>) — Sets the foreground style for the chart content.
- [opacity(_:)](<opacity(__).md>) — Sets the opacity for the chart content.
- [blur(radius:)](<blur(radius_).md>) — Applies a Gaussian blur to this chart content.
- [lineStyle(_:)](<linestyle(__).md>) — Sets the style for line marks.
- [shadow(color:radius:x:y:)](<shadow(color_radius_x_y_).md>) — A chart content that adds a shadow to this chart content.
- [interpolationMethod(_:)](<interpolationmethod(__).md>) — Plots line and area marks with the interpolation method that you specify.
