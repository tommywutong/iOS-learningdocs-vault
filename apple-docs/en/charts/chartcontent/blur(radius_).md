---
title: 'blur(radius:)'
framework: Swift Charts
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.4+, iPadOS 16.4+, Mac Catalyst 16.4+, macOS 13.3+, tvOS 16.4+, visionOS 1.0+, watchOS 9.4+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/charts/chartcontent/blur(radius:)'
source_url: 'https://developer.apple.com/documentation/charts/chartcontent/blur(radius:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/charts/chartcontent/blur%28radius%3A%29.json'
content_hash: 'sha256:af61717870749615'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift Charts](../../charts.md) · [ChartContent](../chartcontent.md)

# blur(radius:)

<sub>Instance Method</sub>

Applies a Gaussian blur to this chart content.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func blur(radius: CGFloat) -> some ChartContent

```

## Parameters

- `radius` — The radial size of the blur. A blur is more diffuse when its radius is large.

## See Also

### Styling marks

- [foregroundStyle(_:)](<foregroundstyle(__).md>) — Sets the foreground style for the chart content.
- [opacity(_:)](<opacity(__).md>) — Sets the opacity for the chart content.
- [cornerRadius(_:style:)](<cornerradius(__style_).md>) — Sets the corner radius of the chart content.
- [lineStyle(_:)](<linestyle(__).md>) — Sets the style for line marks.
- [shadow(color:radius:x:y:)](<shadow(color_radius_x_y_).md>) — A chart content that adds a shadow to this chart content.
- [interpolationMethod(_:)](<interpolationmethod(__).md>) — Plots line and area marks with the interpolation method that you specify.
