---
title: UIFocusItemScrollableContainer
framework: UIKit
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 13.1+, tvOS 12.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uifocusitemscrollablecontainer
source_url: 'https://developer.apple.com/documentation/uikit/uifocusitemscrollablecontainer'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uifocusitemscrollablecontainer.json'
content_hash: 'sha256:68233b5f95cc37f0'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIFocusItemScrollableContainer

<sub>Protocol</sub>

A type of focus item container that supports automatic scrolling of focusable content.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor protocol UIFocusItemScrollableContainer : UIFocusItemContainer
```

## Overview

The focus engine scrolls the container to keep items onscreen as they become focused. This is done by repeatedly setting [contentOffset](uifocusitemscrollablecontainer/contentoffset.md).

## Relationships

- **Inherits From**: [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [UIFocusItemContainer](uifocusitemcontainer.md)

- **Conforming Types**: [UICollectionView](uicollectionview.md), [UIScrollView](uiscrollview.md), [UITableView](uitableview.md), [UITextView](uitextview.md)

## Topics

### Retrieving the content size

- [contentOffset](uifocusitemscrollablecontainer/contentoffset.md) — The current content offset for the scrollable container.
- [contentSize](uifocusitemscrollablecontainer/contentsize.md) — The total size of the content contained by this container.
- [visibleSize](uifocusitemscrollablecontainer/visiblesize.md) — The visible size of the scrollable container.

## See Also

### Focus interactions

- [Navigating an app’s user interface using a keyboard](navigating-an-app-s-user-interface-using-a-keyboard.md) — Navigate between user interface elements using a keyboard and focusable UI elements in iPad apps and apps built with Mac Catalyst.
- [About focus interactions for Apple TV](about-focus-interactions-for-apple-tv.md) — Design and implement intuitive control schemes for menus and interactive user interface layouts.
- [Adding user-focusable elements to a tvOS app](adding-user-focusable-elements-to-a-tvos-app.md) — Create intuitive and easily manipulated user-interactive controls for your tvOS app.
- [UIFocusEnvironment](uifocusenvironment.md) — A set of methods that define the focus behavior for a branch of the view hierarchy.
- [UIFocusSystem](uifocussystem.md) — Queries and reevaluates the currently focused item.
- [UIFocusUpdateContext](uifocusupdatecontext.md) — An object that provides information relevant to a specific focus update from one view to another.
- [UIFocusItem](uifocusitem.md) — An object that can become focused.
- [UIFocusMovementHint](uifocusmovementhint.md) — Provides movement hint information for the focused item.
- [UIFocusItemContainer](uifocusitemcontainer.md) — The container responsible for providing geometric context to focus items within a given focus environment.
- [UIFocusGroupPriority](uifocusgrouppriority.md) — The importance of an item within a focus group, used by the focus system to determine the group’s primary item.
