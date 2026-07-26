---
title: ViewBuilder
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/viewbuilder
source_url: 'https://developer.apple.com/documentation/swiftui/viewbuilder'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/viewbuilder.json'
content_hash: 'sha256:870d976968ef4b51'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# ViewBuilder

<sub>Structure</sub>

A custom parameter attribute that constructs views from closures.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@resultBuilder struct ViewBuilder
```

## Overview

When you build your project in Xcode 26 and earlier, use [ViewBuilder](viewbuilder.md) as a parameter attribute for view-producing closure parameters, allowing those closures to provide multiple child views. For example, the following `contextMenu` function accepts a closure that produces one or more views via the view builder.

```swift
func contextMenu<MenuItems: View>(
    @ViewBuilder menuItems: () -> MenuItems
) -> some View
```

Clients of this function can use multiple-statement closures to provide several child views, as the following example shows:

```swift
myView.contextMenu {
    Text("Cut")
    Text("Copy")
    Text("Paste")
    if isSymbol {
        Text("Jump to Definition")
    }
}
```

When you build in Xcode 27 and later for any version of SwiftUI, the system constructs type-agnostic content from `ViewBuilder` closures, and doesn’t restrict the types you use in closures to conform to [View](view.md). Mark closures with the type alias [ContentBuilder](contentbuilder.md) instead to indicate where your code expects this behavior. For more information, see [ContentBuilder](contentbuilder.md).

## Topics

### Building content

- [buildBlock()](<viewbuilder/buildblock().md>) — Builds an empty content from a block containing no statements.
- [buildBlock(_:)](<viewbuilder/buildblock(__).md>) — Passes a single piece of content written as a child view through unmodified.

### Conditionally building content

- [buildEither(first:)](<viewbuilder/buildeither(first_).md>) — Produces content for a conditional statement in a multi-statement closure when the condition is true.
- [buildEither(second:)](<viewbuilder/buildeither(second_).md>) — Produces content for a conditional statement in a multi-statement closure when the condition is false.
- [buildIf(_:)](<viewbuilder/buildif(__).md>) — Produces optional content for conditional statements in multi-statement closures that’s only included when the condition evaluates to true.
- [buildLimitedAvailability(_:)](<viewbuilder/buildlimitedavailability(__).md>)

## See Also

### Creating a view

- [Declaring a custom view](declaring-a-custom-view.md) — Define views and assemble them into a view hierarchy.
- [Wishlist: Planning travel in a SwiftUI app](wishlist-planning-travel-in-a-swiftui-app.md) — Build a travel planning app that organizes trips into collections and tracks activity completion.
- [View](view.md) — A type that represents part of your app’s user interface and provides modifiers that you use to configure views.
- [ContentBuilder](contentbuilder.md) — A custom parameter attribute that constructs views and other content types from closures.
