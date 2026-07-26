---
title: ScrollAnchorRole
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/scrollanchorrole
source_url: 'https://developer.apple.com/documentation/swiftui/scrollanchorrole'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/scrollanchorrole.json'
content_hash: 'sha256:7688505bbdafa65c'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# ScrollAnchorRole

<sub>Structure</sub>

A type defining the role of a scroll anchor.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct ScrollAnchorRole
```

## Overview

You can associate a [UnitPoint](unitpoint.md) to a [ScrollView](scrollview.md) using the [defaultScrollAnchor(_:)](<view/defaultscrollanchor(__).md>) modifier. By default, the system uses this point for different kinds of behaviors including:

- Where the scroll view should initially be scrolled
- How the scroll view should handle content size or container size changes
- How the scroll view should align content smaller than its container size

You can further customize this behavior by assigning different unit points for these different roles.

## Relationships

- **Conforms To**: [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Type Properties

- [alignment](scrollanchorrole/alignment.md) — The role that influences how a scroll view should align its content when the size of its content is smaller than the container size of the scroll view.
- [initialOffset](scrollanchorrole/initialoffset.md) — The role that influences where a scroll view should be initially scrolled.
- [sizeChanges](scrollanchorrole/sizechanges.md) — The role that influences how a scroll view should adjust its content offset when the scroll view’s content or container size changes.

## See Also

### Managing scroll position

- [scrollPosition(_:anchor:)](<view/scrollposition(__anchor_).md>) — Associates a binding to a scroll position with a scroll view within this view.
- [scrollPosition(id:anchor:)](<view/scrollposition(id_anchor_).md>) — Associates a binding to be updated when a scroll view within this view scrolls.
- [defaultScrollAnchor(_:)](<view/defaultscrollanchor(__).md>) — Associates an anchor to control which part of the scroll view’s content should be rendered by default.
- [defaultScrollAnchor(_:for:)](<view/defaultscrollanchor(__for_).md>) — Associates an anchor to control the position of a scroll view in a particular circumstance.
- [ScrollPosition](scrollposition.md) — A type that defines the semantic position of where a scroll view is scrolled within its content.
