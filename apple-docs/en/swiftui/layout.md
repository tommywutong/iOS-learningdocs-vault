---
title: Layout
framework: SwiftUI
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/layout
source_url: 'https://developer.apple.com/documentation/swiftui/layout'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/layout.json'
content_hash: 'sha256:91188043b679eaa8'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# Layout

<sub>Protocol</sub>

A type that defines the geometry of a collection of views.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@preconcurrency protocol Layout : Sendable, Animatable
```

## Overview

You traditionally arrange views in your app’s user interface using built-in layout containers like [HStack](hstack.md) and [Grid](grid.md). If you need more complex layout behavior, you can define a custom layout container by creating a type that conforms to the `Layout` protocol and implementing its required methods:

- [sizeThatFits(proposal:subviews:cache:)](<layout/sizethatfits(proposal_subviews_cache_).md>) reports the size of the composite layout view.
- [placeSubviews(in:proposal:subviews:cache:)](<layout/placesubviews(in_proposal_subviews_cache_).md>) assigns positions to the container’s subviews.

You can define a basic layout type with only these two methods:

```swift
struct BasicVStack: Layout {
    func sizeThatFits(
        proposal: ProposedViewSize,
        subviews: Subviews,
        cache: inout ()
    ) -> CGSize {
        // Calculate and return the size of the layout container.
    }

    func placeSubviews(
        in bounds: CGRect,
        proposal: ProposedViewSize,
        subviews: Subviews,
        cache: inout ()
    ) {
        // Tell each subview where to appear.
    }
}
```

Use your layout the same way you use a built-in layout container, by providing a [ContentBuilder](contentbuilder.md) with the list of subviews to arrange:

```swift
BasicVStack {
    Text("A Subview")
    Text("Another Subview")
}
```

### Support additional behaviors

You can optionally implement other protocol methods and properties to provide more layout container features:

- Define explicit horizontal and vertical layout guides for the container by implementing [explicitAlignment(of:in:proposal:subviews:cache:)](<layout/explicitalignment(of_in_proposal_subviews_cache_).md>) for each dimension.
- Establish the preferred spacing around the container by implementing [spacing(subviews:cache:)](<layout/spacing(subviews_cache_).md>).
- Indicate the axis of orientation for a container that has characteristics of a stack by implementing the [layoutProperties](layout/layoutproperties.md) static property.
- Create and manage a cache to store computed values across different layout protocol calls by implementing [makeCache(subviews:)](<layout/makecache(subviews_).md>).

The protocol provides default implementations for these symbols if you don’t implement them. See each method or property for details.

### Add input parameters

You can define parameters as inputs to the layout, like you might for a [View](view.md):

```swift
struct BasicVStack: Layout {
    var alignment: HorizontalAlignment

    // ...
}
```

Set the parameters at the point where you instantiate the layout:

```swift
BasicVStack(alignment: .leading) {
    // ...
}
```

If the layout provides default values for its parameters, you can omit the parameters at the call site, but you might need to keep the parentheses after the name of the layout, depending on how you specify the defaults. For example, suppose you set a default alignment for the basic stack in the parameter declaration:

```swift
struct BasicVStack: Layout {
    var alignment: HorizontalAlignment = .center

    // ...
}
```

To instantiate this layout using the default center alignment, you don’t have to specify the alignment value, but you do need to add empty parentheses:

```swift
BasicVStack() {
    // ...
}
```

The Swift compiler requires the parentheses in this case because of how the layout protocol implements this call site syntax. Specifically, the layout’s [callAsFunction(_:)](<layout/callasfunction(__).md>) method looks for an initializer with exactly zero input arguments when you omit the parentheses from the call site. You can enable the simpler call site for a layout that doesn’t have an implicit initializer of this type by explicitly defining one:

```swift
init() {
    self.alignment = .center
}
```

For information about Swift initializers, see [Initialization](https://docs.swift.org/swift-book/LanguageGuide/Initialization.html) in _The Swift Programming Language_.

### Interact with subviews through their proxies

To perform layout, you need information about all of its subviews, which are the views that your container arranges. While your layout can’t interact directly with its subviews, it can access a set of subview proxies through the [Subviews](layout/subviews.md) collection that each protocol method receives as an input parameter. That type is an alias for the [LayoutSubviews](layoutsubviews.md) collection type, which in turn contains [LayoutSubview](layoutsubview.md) instances that are the subview proxies.

You can get information about each subview from its proxy, like its dimensions and spacing preferences. This enables you to measure subviews before you commit to placing them. You also assign a position to each subview by calling its proxy’s [place(at:anchor:proposal:)](<layoutsubview/place(at_anchor_proposal_).md>) method. Call the method on each subview from within your implementation of the layout’s [placeSubviews(in:proposal:subviews:cache:)](<layout/placesubviews(in_proposal_subviews_cache_).md>) method.

### Access layout values

Views have layout values that you set with view modifiers. Layout containers can choose to condition their behavior accordingly. For example, a built-in [HStack](hstack.md) allocates space to its subviews based in part on the priorities that you set with the [layoutPriority(_:)](<view/layoutpriority(__).md>) view modifier. Your layout container accesses this value for a subview by reading the proxy’s [priority](layoutsubview/priority.md) property.

You can also create custom layout values by creating a layout key. Set a value on a view with the [layoutValue(key:value:)](<view/layoutvalue(key_value_).md>) view modifier. Read the corresponding value from the subview’s proxy using the key as an index on the subview. For more information about creating, setting, and accessing custom layout values, see [LayoutValueKey](layoutvaluekey.md).

## Relationships

- **Inherits From**: [Animatable](animatable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

- **Conforming Types**: [AnyLayout](anylayout.md), [GridLayout](gridlayout.md), [HStackLayout](hstacklayout.md), [SpatialContainer](spatialcontainer.md), [VStackLayout](vstacklayout.md), [ZStackLayout](zstacklayout.md)

## Topics

### Sizing the container and placing subviews

- [sizeThatFits(proposal:subviews:cache:)](<layout/sizethatfits(proposal_subviews_cache_).md>) — Returns the size of the composite view, given a proposed size and the view’s subviews.
- [placeSubviews(in:proposal:subviews:cache:)](<layout/placesubviews(in_proposal_subviews_cache_).md>) — Assigns positions to each of the layout’s subviews.
- [Subviews](layout/subviews.md) — A collection of proxies for the subviews of a layout view.

### Reporting layout container characteristics

- [explicitAlignment(of:in:proposal:subviews:cache:)](<layout/explicitalignment(of_in_proposal_subviews_cache_).md>) — Returns the position of the specified horizontal alignment guide along the x axis.
- [spacing(subviews:cache:)](<layout/spacing(subviews_cache_).md>) — Returns the preferred spacing values of the composite view.
- [layoutProperties](layout/layoutproperties.md) — Properties of a layout container.

### Managing a cache

- [makeCache(subviews:)](<layout/makecache(subviews_).md>) — Creates and initializes a cache for a layout instance.
- [updateCache(_:subviews:)](<layout/updatecache(__subviews_).md>) — Updates the layout’s cache when something changes.
- [Cache](layout/cache.md) — Cached values associated with the layout instance.

### Supporting types

- [callAsFunction(_:)](<layout/callasfunction(__).md>) — Combines the specified views into a single composite view using the layout algorithms of the custom layout container.

### Instance Methods

- [depthAlignment(_:)](<layout/depthalignment(__).md>) — Sets the depth alignment for this layout.
- [depthAlignment(_:content:)](<layout/depthalignment(__content_).md>) — Creates a layout view with the specified depth alignment.

## See Also

### Creating a custom layout container

- [Composing custom layouts with SwiftUI](composing-custom-layouts-with-swiftui.md) — Arrange views in your app’s interface using layout tools that SwiftUI provides.
- [LayoutSubview](layoutsubview.md) — A proxy that represents one subview of a layout.
- [LayoutSubviews](layoutsubviews.md) — A collection of proxy values that represent the subviews of a layout view.
