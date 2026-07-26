---
title: 'backgroundStyle(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/backgroundstyle(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/backgroundstyle(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/backgroundstyle%28_%3A%29.json'
content_hash: 'sha256:bbb16d9ec43d75d1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# backgroundStyle(_:)

<sub>Instance Method</sub>

Sets the specified style to render backgrounds within the view.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func backgroundStyle<S>(_ style: S) -> some View where S : ShapeStyle

```

## Discussion

The following example uses this modifier to set the [backgroundStyle](../environmentvalues/backgroundstyle.md) environment value to a [blue](../shapestyle/blue.md) color that includes a subtle [gradient](../color/gradient.md). SwiftUI fills the [Circle](../circle.md) shape that acts as a background element with this style:

```swift
Image(systemName: "swift")
    .padding()
    .background(in: Circle())
    .backgroundStyle(.blue.gradient)
```

![An image of the Swift logo inside a circle that’s blue with a slight](../../../../attachments/4b3325ab8b030bb73b60cd8cfe326695/View-backgroundStyle-1-iOS@2x.png)

To restore the default background style, set the [backgroundStyle](../environmentvalues/backgroundstyle.md) environment value to `nil` using the [environment(_:_:)](<environment(____).md>) modifer:

```swift
.environment(\.backgroundStyle, nil)
```

## See Also

### Styling content

- [border(_:width:)](<border(__width_).md>) — Adds a border to this view with the specified style and width.
- [foregroundStyle(_:)](<foregroundstyle(__).md>) — Sets a view’s foreground elements to use a given style.
- [foregroundStyle(_:_:)](<foregroundstyle(____).md>) — Sets the primary and secondary levels of the foreground style in the child view.
- [foregroundStyle(_:_:_:)](<foregroundstyle(______).md>) — Sets the primary, secondary, and tertiary levels of the foreground style.
- [backgroundStyle](../environmentvalues/backgroundstyle.md) — An optional style that overrides the default system background style when set.
- [ShapeStyle](../shapestyle.md) — A color or pattern to use when rendering a shape.
- [AnyShapeStyle](../anyshapestyle.md) — A type-erased ShapeStyle value.
- [Gradient](../gradient.md) — A color gradient represented as an array of color stops, each having a parametric location value.
- [MeshGradient](../meshgradient.md) — A two-dimensional gradient defined by a 2D grid of positioned colors.
- [AnyGradient](../anygradient.md) — A color gradient.
- [ShadowStyle](../shadowstyle.md) — A style to use when rendering shadows.
- [Glass](../glass.md) — A structure that defines the configuration of the Liquid Glass material.
