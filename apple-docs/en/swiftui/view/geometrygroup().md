---
title: geometryGroup()
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/view/geometrygroup()
source_url: 'https://developer.apple.com/documentation/swiftui/view/geometrygroup()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/geometrygroup%28%29.json'
content_hash: 'sha256:f023046e85bf27bf'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# geometryGroup()

<sub>Instance Method</sub>

Isolates the geometry (e.g. position and size) of the view from its parent view.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@export(implementation) nonisolated func geometryGroup() -> some View

```

## Discussion

By default SwiftUI views push position and size changes down through the view hierarchy, so that only views that draw something (known as leaf views) apply the current animation to their frame rectangle. However in some cases this coalescing behavior can give undesirable results; inserting a geometry group can correct that. A group acts as a barrier between the parent view and its subviews, forcing the position and size values to be resolved and animated by the parent, before being passed down to each subview.

The example below shows one use of this function: ensuring that the member views of each row in the stack apply (and animate as) a single geometric transform from their ancestor view, rather than letting the effects of the ancestor views be applied separately to each leaf view. If the members of `ItemView` may be added and removed at different times the group ensures that they stay locked together as animations are applied.

```swift
VStack {
    ForEach(items) { item in
        ItemView(item: item)
            .geometryGroup()
    }
}
```

Returns: a new view whose geometry is isolated from that of its parent view.

## See Also

### Synchronizing geometries

- [matchedGeometryEffect(id:in:properties:anchor:isSource:)](<matchedgeometryeffect(id_in_properties_anchor_issource_).md>) — Defines a group of views with synchronized geometry using an identifier and namespace that you provide.
- [MatchedGeometryProperties](../matchedgeometryproperties.md) — A set of view properties that may be synchronized between views using the `View.matchedGeometryEffect()` function.
- [GeometryEffect](../geometryeffect.md) — An effect that changes the visual appearance of a view, largely without changing its ancestors or descendants.
- [Namespace](../namespace.md) — A dynamic property type that allows access to a namespace defined by the persistent identity of the object containing the property (e.g. a view).
