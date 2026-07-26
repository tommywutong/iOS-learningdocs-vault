---
title: HorizontalEdge
framework: SwiftUI
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/horizontaledge
source_url: 'https://developer.apple.com/documentation/swiftui/horizontaledge'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/horizontaledge.json'
content_hash: 'sha256:3492e83ffd762a0b'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# HorizontalEdge

<sub>Enumeration</sub>

An edge on the horizontal axis.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@frozen enum HorizontalEdge
```

## Overview

Use a horizontal edge for tasks like setting a swipe action with the [swipeActions(edge:allowsFullSwipe:content:)](<view/swipeactions(edge_allowsfullswipe_content_).md>) view modifier. The positions of the leading and trailing edges depend on the locale chosen by the user.

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [CaseIterable](../swift/caseiterable.md), [Copyable](../swift/copyable.md), [Decodable](../swift/decodable.md), [Encodable](../swift/encodable.md), [Equatable](../swift/equatable.md), [Escapable](../swift/escapable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Getting the edges

- [HorizontalEdge.leading](horizontaledge/leading.md) — The leading edge.
- [HorizontalEdge.trailing](horizontaledge/trailing.md) — The trailing edge.

### Accessing sets of edges

- [Set](horizontaledge/set.md) — An efficient set of horizontal edges.

## See Also

### Accessing edges, regions, and layouts

- [Edge](edge.md) — An enumeration to indicate one edge of a rectangle.
- [Edge3D](edge3d.md) — An edge or face of a 3D volume.
- [VerticalEdge](verticaledge.md) — An edge on the vertical axis.
- [EdgeInsets](edgeinsets.md) — The inset distances for the sides of a rectangle.
- [EdgeInsets3D](edgeinsets3d.md) — The inset distances for the faces of a 3D volume.
