---
title: 'containerShape(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/containershape(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/containershape(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/containershape%28_%3A%29.json'
content_hash: 'sha256:98cacedc9ffd0d83'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# containerShape(_:)

<sub>Instance Method</sub>

Sets the container shape to use for any container relative shape or concentric rectangle within this view.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func containerShape(_ shape: some RoundedRectangularShape) -> some View

```

## Discussion

The example below defines a view that shows its content with a rounded rectangle background and the same container shape. Any [ContainerRelativeShape](../containerrelativeshape.md) within the `content` matches the rounded rectangle shape from this container inset as appropriate. Any [ConcentricRectangle](../concentricrectangle.md) within the `content` will match the corners to be concentric to the container corners.

```swift
struct PlatterContainer<Content: View> : View {
    @ContentBuilder var content: Content
    var body: some View {
        content
            .padding()
            .containerShape(shape)
            .background(shape.fill(.background))
    }
    var shape: RoundedRectangle { RoundedRectangle(cornerRadius: 20) }
}
```

> [!info] See Also
> [containerShape(_:)](<containershape(__)-qn9q.md>)

## See Also

### Setting a container shape

- [InsettableShape](../insettableshape.md) — A shape type that is able to inset itself to produce another shape.
- [ContainerRelativeShape](../containerrelativeshape.md) — A shape whose dimensions the system calculates from an inset version of the current container shape.
