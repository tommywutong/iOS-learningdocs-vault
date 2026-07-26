---
title: EmptyView
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/emptyview
source_url: 'https://developer.apple.com/documentation/swiftui/emptyview'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/emptyview.json'
content_hash: 'sha256:517df772d36ad87c'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# EmptyView

<sub>Structure</sub>

A view that doesn’t contain any content.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@frozen nonisolated struct EmptyView
```

## Overview

You will rarely, if ever, need to create an `EmptyView` directly. Instead, `EmptyView` represents the absence of a view.

SwiftUI uses `EmptyView` in situations where a SwiftUI view type defines one or more child views with generic parameters, and allows the child views to be absent. When absent, the child view’s type in the generic type parameter is `EmptyView`.

The following example creates an indeterminate [ProgressView](progressview.md) without a label. The [ProgressView](progressview.md) type declares two generic parameters, `Label` and `CurrentValueLabel`, for the types used by its subviews. When both subviews are absent, like they are here, the resulting type is `ProgressView<EmptyView, EmptyView>`, as indicated by the example’s output:

```swift
let progressView = ProgressView()
print("\(type(of:progressView))")
// Prints: ProgressView<EmptyView, EmptyView>
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [ChartContent](../charts/chartcontent.md), [Commands](commands.md), [Copyable](../swift/copyable.md), [CustomizableToolbarContent](customizabletoolbarcontent.md), [Escapable](../swift/escapable.md), [SceneAccessoryContent](sceneaccessorycontent.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [ToolbarContent](toolbarcontent.md), [View](view.md)

## Topics

### Creating an empty view

- [init()](<emptyview/init().md>) — Creates an empty view.

## See Also

### Supporting view types

- [AnyView](anyview.md) — A type-erased view.
- [EquatableView](equatableview.md) — A view type that compares itself against its previous value and prevents its child updating if its new value is the same as its old value.
- [SubscriptionView](subscriptionview.md) — A view that subscribes to a publisher with an action.
- [TupleView](tupleview.md) — A View created from a swift tuple of View values.
