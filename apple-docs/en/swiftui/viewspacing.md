---
title: ViewSpacing
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/viewspacing
source_url: 'https://developer.apple.com/documentation/swiftui/viewspacing'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/viewspacing.json'
content_hash: 'sha256:c0cbd4b7c15c7e54'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# ViewSpacing

<sub>Structure</sub>

A collection of the geometric spacing preferences of a view.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct ViewSpacing
```

## Overview

This type represents how much space a view prefers to have between it and the next view in a layout. The type stores independent values for each of the top, bottom, leading, and trailing edges, and can also record different values for different kinds of adjacent views. For example, it might contain one value for the spacing to the next text view along the top and bottom edges, other values for the spacing to text views on other edges, and yet other values for other kinds of views. Spacing preferences can also vary by platform.

Your [Layout](layout.md) type doesn’t have to take preferred spacing into account, but if it does, you can use the [spacing](layoutsubview/spacing.md) preferences of the subviews in your layout container to:

- Add space between subviews when you implement the [placeSubviews(in:proposal:subviews:cache:)](<layout/placesubviews(in_proposal_subviews_cache_).md>) method.
- Create a spacing preferences instance for the container view by implementing the [spacing(subviews:cache:)](<layout/spacing(subviews_cache_).md>) method.

## Relationships

- **Conforms To**: [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Creating spacing instances

- [init()](<viewspacing/init().md>) — Initializes an instance with default spacing values.
- [zero](viewspacing/zero.md) — A view spacing instance that contains zero on all edges.

### Measuring spacing distance

- [distance(to:along:)](<viewspacing/distance(to_along_).md>) — Gets the preferred spacing distance along the specified axis to the view that returns a specified spacing preference.

### Merging spacing instances

- [formUnion(_:edges:)](<viewspacing/formunion(__edges_).md>) — Merges the spacing preferences of another spacing instance with this instance for a specified set of edges.
- [union(_:edges:)](<viewspacing/union(__edges_).md>) — Gets a new value that merges the spacing preferences of another spacing instance with this instance for a specified set of edges.

## See Also

### Configuring a custom layout

- [LayoutProperties](layoutproperties.md) — Layout-specific properties of a layout container.
- [ProposedViewSize](proposedviewsize.md) — A proposal for the size of a view.
