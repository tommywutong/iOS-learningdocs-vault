---
title: Custom layout
framework: SwiftUI
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/custom-layout
source_url: 'https://developer.apple.com/documentation/swiftui/custom-layout'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/custom-layout.json'
content_hash: 'sha256:ea49ab74d42dc29a'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# Custom layout

<sub>API Collection</sub>

Place views in custom arrangements and create animated transitions between layout types.

## Overview

You can create complex view layouts using the built-in layout containers and layout view modifiers that SwiftUI provides. However, if you need behavior that you can’t achieve with the built-in layout tools, create a custom layout container type using the [Layout](layout.md) protocol. A container that you define asks for the sizes of all its subviews, and then indicates where to place the subviews within its own bounds.

![](../../../attachments/098af88e7ef1601f537924b942ecfb67/custom-layout-hero@2x.png)

You can also create animated transitions among layout types that conform to the [Layout](layout.md) procotol, including both built-in and custom layouts.

For design guidance, see [Layout](../design/human-interface-guidelines/layout.md) in the Human Interface Guidelines.

## Topics

### Creating a custom layout container

- [Composing custom layouts with SwiftUI](composing-custom-layouts-with-swiftui.md) — Arrange views in your app’s interface using layout tools that SwiftUI provides.
- [Layout](layout.md) — A type that defines the geometry of a collection of views.
- [LayoutSubview](layoutsubview.md) — A proxy that represents one subview of a layout.
- [LayoutSubviews](layoutsubviews.md) — A collection of proxy values that represent the subviews of a layout view.

### Configuring a custom layout

- [LayoutProperties](layoutproperties.md) — Layout-specific properties of a layout container.
- [ProposedViewSize](proposedviewsize.md) — A proposal for the size of a view.
- [ViewSpacing](viewspacing.md) — A collection of the geometric spacing preferences of a view.

### Associating values with views in a custom layout

- [layoutValue(key:value:)](<view/layoutvalue(key_value_).md>) — Associates a value with a custom layout property.
- [LayoutValueKey](layoutvaluekey.md) — A key for accessing a layout value of a layout container’s subviews.

### Transitioning between layout types

- [AnyLayout](anylayout.md) — A type-erased instance of the layout protocol.
- [HStackLayout](hstacklayout.md) — A horizontal container that you can use in conditional layouts.
- [VStackLayout](vstacklayout.md) — A vertical container that you can use in conditional layouts.
- [ZStackLayout](zstacklayout.md) — An overlaying container that you can use in conditional layouts.
- [GridLayout](gridlayout.md) — A grid that you can use in conditional layouts.

## See Also

### View layout

- [Layout fundamentals](layout-fundamentals.md) — Arrange views inside built-in layout containers like stacks and grids.
- [Layout adjustments](layout-adjustments.md) — Make fine adjustments to alignment, spacing, padding, and other layout parameters.
- [Lists](lists.md) — Display a structured, scrollable column of information.
- [Tables](tables.md) — Display selectable, sortable data arranged in rows and columns.
- [View groupings](view-groupings.md) — Present views in different kinds of purpose-driven containers, like forms or control groups.
- [Scroll views](scroll-views.md) — Enable people to scroll to content that doesn’t fit in the current display.
