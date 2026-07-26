---
title: body
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/shapestyle/body
source_url: 'https://developer.apple.com/documentation/swiftui/shapestyle/body'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/shapestyle/body.json'
content_hash: 'sha256:3d0826e6833ae592'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [ShapeStyle](../shapestyle.md)

# body

<sub>Instance Property</sub>

A rectangular view that’s filled with the shape style.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var body: _ShapeView<Rectangle, Self> { get }
```

## Discussion

For a [ShapeStyle](../shapestyle.md) that also conforms to the [View](../view.md) protocol, like [Color](../color.md) or [LinearGradient](../lineargradient.md), this default implementation of the [body](../view/body-8kl5o.md) property provides a visual representation for the shape style. As a result, you can use the shape style in a view hierarchy like any other view:

```swift
ZStack {
    Color.cyan
    Text("Hello!")
}
.frame(width: 200, height: 50)
```

![A screenshot of a cyan rectangle with the text hello appearing](../../../../attachments/d98cc7c4fc793e30a60868b76210d872/ShapeStyle-body-1@2x.png)
