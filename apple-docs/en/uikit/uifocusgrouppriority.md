---
title: UIFocusGroupPriority
framework: UIKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uifocusgrouppriority
source_url: 'https://developer.apple.com/documentation/uikit/uifocusgrouppriority'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uifocusgrouppriority.json'
content_hash: 'sha256:5fe554e1d4858dd5'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIFocusGroupPriority

<sub>Structure</sub>

The importance of an item within a focus group, used by the focus system to determine the group’s primary item.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
struct UIFocusGroupPriority
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Constants

- [UIFocusGroupPriorityIgnored](uifocusgrouppriority/ignored.md) — The lowest focus group priority, assigned by default.
- [UIFocusGroupPriorityPreviouslyFocused](uifocusgrouppriority/previouslyfocused.md) — The focus group priority of a previously focused item.
- [UIFocusGroupPriorityPrioritized](uifocusgrouppriority/prioritized.md) — The focus group priority that indicates an item is more important than others.
- [UIFocusGroupPriorityCurrentlyFocused](uifocusgrouppriority/currentlyfocused.md) — The focus group priority of the currently focused item, the highest possible priority.

### Initializing a focus group priority

- [init(_:)](<uifocusgrouppriority/init(__).md>) — Creates a focus group priority with the specified value.
- [init(rawValue:)](<uifocusgrouppriority/init(rawvalue_).md>) — Creates a focus group priority with the specified raw value.

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
- [UIFocusItemScrollableContainer](uifocusitemscrollablecontainer.md) — A type of focus item container that supports automatic scrolling of focusable content.
