---
title: LayoutSubview
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/layoutsubview
source_url: 'https://developer.apple.com/documentation/swiftui/layoutsubview'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/layoutsubview.json'
content_hash: 'sha256:5092b54fc4295f04'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# LayoutSubview

<sub>Structure</sub>

A proxy that represents one subview of a layout.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct LayoutSubview
```

## Overview

This type acts as a proxy for a view that your custom layout container places in the user interface. [Layout](layout.md) protocol methods receive a [LayoutSubviews](layoutsubviews.md) collection that contains exactly one proxy for each of the subviews arranged by your container.

Use a proxy to get information about the associated subview, like its dimensions, layout priority, or custom layout values. You also use the proxy to tell its corresponding subview where to appear by calling the proxy’s [place(at:anchor:proposal:)](<layoutsubview/place(at_anchor_proposal_).md>) method. Do this once for each subview from your implementation of the layout’s [placeSubviews(in:proposal:subviews:cache:)](<layout/placesubviews(in_proposal_subviews_cache_).md>) method.

You can read custom layout values associated with a subview by using the property’s key as an index on the subview. For more information about defining, setting, and reading custom values, see [LayoutValueKey](layoutvaluekey.md).

## Relationships

- **Conforms To**: [Equatable](../swift/equatable.md)

## Topics

### Placing the subview

- [place(at:anchor:proposal:)](<layoutsubview/place(at_anchor_proposal_).md>) — Assigns a position and proposed size to the subview.

### Getting subview characteristics

- [dimensions(in:)](<layoutsubview/dimensions(in_).md>) — Asks the subview for its dimensions and alignment guides.
- [sizeThatFits(_:)](<layoutsubview/sizethatfits(__).md>) — Asks the subview for its size.
- [spacing](layoutsubview/spacing.md) — The subviews’s preferred spacing values.
- [priority](layoutsubview/priority.md) — The layout priority of the subview.

### Getting custom values

- [subscript(_:)](<layoutsubview/subscript(__).md>) — Gets the value for the subview that’s associated with the specified key.

### Instance Properties

- [containerValues](layoutsubview/containervalues.md) — The container values associated with the given subview.

## See Also

### Creating a custom layout container

- [Composing custom layouts with SwiftUI](composing-custom-layouts-with-swiftui.md) — Arrange views in your app’s interface using layout tools that SwiftUI provides.
- [Layout](layout.md) — A type that defines the geometry of a collection of views.
- [LayoutSubviews](layoutsubviews.md) — A collection of proxy values that represent the subviews of a layout view.
