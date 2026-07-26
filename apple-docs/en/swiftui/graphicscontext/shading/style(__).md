---
title: 'style(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/graphicscontext/shading/style(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/graphicscontext/shading/style(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/graphicscontext/shading/style%28_%3A%29.json'
content_hash: 'sha256:fadcbbc1923249eb'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [SwiftUI](../../../swiftui.md) · [GraphicsContext](../../graphicscontext.md) · [Shading](../shading.md)

# style(_:)

<sub>Type Method</sub>

Returns a shading instance that fills with the given shape style.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func style<S>(_ style: S) -> GraphicsContext.Shading where S : ShapeStyle
```

## Parameters

- `style` — A [ShapeStyle](../../shapestyle.md) instance to draw with.

## Return Value

A shading instance filled with a shape style.

## Discussion

Styles with geometry defined in a unit coordinate space map that space to the rectangle associated with the drawn object. You can adjust that using the [in(_:)](<../../shapestyle/in(__).md>) method. The shape style might affect the blend mode and opacity of the drawn object.

## See Also

### Other shape styles

- [foreground](foreground.md) — A shading instance that fills with the foreground style from the graphics context’s environment.
