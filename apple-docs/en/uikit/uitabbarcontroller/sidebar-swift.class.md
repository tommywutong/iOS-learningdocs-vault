---
title: UITabBarController.Sidebar
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, visionOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitabbarcontroller/sidebar-swift.class
source_url: 'https://developer.apple.com/documentation/uikit/uitabbarcontroller/sidebar-swift.class'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitabbarcontroller/sidebar-swift.class.json'
content_hash: 'sha256:4a3f264d1b84a205'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITabBarController](../uitabbarcontroller.md)

# UITabBarController.Sidebar

<sub>Class</sub>

An object for managing and configuring the sidebar.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
@MainActor class Sidebar
```

## Relationships

- **Inherits From**: [NSObject](../../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../../swift/cvararg.md), [CustomDebugStringConvertible](../../swift/customdebugstringconvertible.md), [CustomStringConvertible](../../swift/customstringconvertible.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [NSObjectProtocol](../../objectivec/nsobjectprotocol.md), [Sendable](../../swift/sendable.md)

## Topics

### Setting the sidebar delegate

- [delegate](sidebar-swift.class/delegate-swift.property.md) — The object managing the delegate of the sidebar.
- [Delegate](sidebar-swift.class/delegate-swift.protocol.md)

### Scrolling

- [scroll(to:animated:)](<sidebar-swift.class/scroll(to_animated_).md>)
- [ScrollTarget](sidebar-swift.class/scrolltarget.md)

### Managing customization

- [hidden](sidebar-swift.class/ishidden.md) — Determines if the sidebar is currently hidden.
- [preferredLayout](sidebar-swift.class/preferredlayout.md) — The preferred layout for how the sidebar lays out with the tab bar controller’s content. Default is `.automatic`
- [Layout](sidebar-swift.class/layout.md)
- [- reconfigureItemForTab:](<sidebar-swift.class/reconfigureitem(for_).md>) — Requests the sidebar reconfigure the item representing the specified tab. This method has no effect if the `tab` is not currently displayed in the sidebar.

### Headers and footers

- [bottomBarView](sidebar-swift.class/bottombarview.md) — A view to display at the bottom of the sidebar, like a UIToolbar. The width of this view will be managed by the sidebar itself, and its height will be set to the value it returns from `systemLayoutSizeFittingSize:withHorizontalFittingPriority:verticalFittingPriority:` Default is nil.
- [footerContentConfiguration](sidebar-swift.class/footercontentconfiguration.md)
- [headerContentConfiguration](sidebar-swift.class/headercontentconfiguration.md)

### Instance Properties

- [isAvailable](sidebar-swift.class/isavailable.md) — Indicates when the tab sidebar is available to be displayed in the current context. When available, the sidebar is either visible, or can become visible depending on `isHidden`. Use this property to gate behaviors or UI that is dependent on the availability of the sidebar (like child tabs, or landing pages for groups). _(beta)_
- [navigationOverflowItems](sidebar-swift.class/navigationoverflowitems.md) — Additional items to add to the overflow menu in the sidebar’s navigation bar. Setting this property to a non-nil value will force the overflow button to appear, regardless of if you provide any content in the element’s callback. Items returned are displayed directly in the presented menu. When set, the “Edit Sidebar” action will also be moved into the overflow menu after the app-provided items.
- [preferredPlacement](sidebar-swift.class/preferredplacement.md) — The preferred placement for the tab bar controller when the sidebar and tab bar are mutually exclusive, and only one placement can be displayed. _(beta)_

### Enumerations

- [Placement](sidebar-swift.class/placement.md) _(beta)_

## See Also

### Supporting the sidebar

- [mode](mode-swift.property.md) — The display mode for a tab bar.
- [Mode](mode-swift.enum.md) — A tab bar’s display mode.
- [sidebar](sidebar-swift.property.md) — A tab bar’s corresponding sidebar.
- [UITabSidebarItem](../uitabsidebaritem.md)
- [Request](../uitabsidebaritem/request.md)
- [Animating](sidebar-swift.class/animating.md)
