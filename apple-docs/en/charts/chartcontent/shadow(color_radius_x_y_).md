---
title: 'shadow(color:radius:x:y:)'
framework: Swift Charts
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.4+, iPadOS 16.4+, Mac Catalyst 16.4+, macOS 13.3+, tvOS 16.4+, visionOS 1.0+, watchOS 9.4+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/charts/chartcontent/shadow(color:radius:x:y:)'
source_url: 'https://developer.apple.com/documentation/charts/chartcontent/shadow(color:radius:x:y:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/charts/chartcontent/shadow%28color%3Aradius%3Ax%3Ay%3A%29.json'
content_hash: 'sha256:a4afd21c3e77908c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift Charts](../../charts.md) · [ChartContent](../chartcontent.md)

# shadow(color:radius:x:y:)

<sub>Instance Method</sub>

A chart content that adds a shadow to this chart content.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func shadow(color: Color = Color(.sRGBLinear, white: 0, opacity: 0.33), radius: CGFloat, x: CGFloat = 0, y: CGFloat = 0) -> some ChartContent

```

## Parameters

- `color` — The shadow’s color.

- `radius` — A measure of how much to blur the shadow. Larger values result in more blur.

- `x` — An amount to offset the shadow horizontally.

- `y` — An amount to offset the shadow vertically.

## See Also

### Styling marks

- [foregroundStyle(_:)](<foregroundstyle(__).md>) — Sets the foreground style for the chart content.
- [opacity(_:)](<opacity(__).md>) — Sets the opacity for the chart content.
- [blur(radius:)](<blur(radius_).md>) — Applies a Gaussian blur to this chart content.
- [cornerRadius(_:style:)](<cornerradius(__style_).md>) — Sets the corner radius of the chart content.
- [lineStyle(_:)](<linestyle(__).md>) — Sets the style for line marks.
- [interpolationMethod(_:)](<interpolationmethod(__).md>) — Plots line and area marks with the interpolation method that you specify.
