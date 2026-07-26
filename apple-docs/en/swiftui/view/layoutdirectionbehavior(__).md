---
title: 'layoutDirectionBehavior(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/layoutdirectionbehavior(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/layoutdirectionbehavior(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/layoutdirectionbehavior%28_%3A%29.json'
content_hash: 'sha256:3b073da3396a5977'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# layoutDirectionBehavior(_:)

<sub>Instance Method</sub>

Sets the behavior of this view for different layout directions.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func layoutDirectionBehavior(_ behavior: LayoutDirectionBehavior) -> some View

```

## Parameters

- `behavior` — A LayoutDirectionBehavior value that indicates whether this view should mirror in a particular layout direction. By default, views will adjust their layouts automatically in a right-to-left context and do not need to be mirrored.

## Return Value

A view that conditionally mirrors its contents horizontally in a given layout direction.

## Discussion

Use `layoutDirectionBehavior(_:)` when you need the system to horizontally mirror the contents of the view when presented in a layout direction.

To override the layout direction for a specific view, use the [environment(_:_:)](<environment(____).md>) view modifier to explicitly override the [layoutDirection](../environmentvalues/layoutdirection.md) environment value for the view.

## See Also

### Setting a layout direction

- [LayoutDirectionBehavior](../layoutdirectionbehavior.md) — A description of what should happen when the layout direction changes.
- [layoutDirection](../environmentvalues/layoutdirection.md) — The layout direction associated with the current environment.
- [LayoutDirection](../layoutdirection.md) — A direction in which SwiftUI can lay out content.
- [LayoutRotationUnaryLayout](../layoutrotationunarylayout.md)
