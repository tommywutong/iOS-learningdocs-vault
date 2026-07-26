---
title: UITabBarController.Sidebar.Layout
framework: UIKit
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, visionOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitabbarcontroller/sidebar-swift.class/layout
source_url: 'https://developer.apple.com/documentation/uikit/uitabbarcontroller/sidebar-swift.class/layout'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitabbarcontroller/sidebar-swift.class/layout.json'
content_hash: 'sha256:98e1c20eaae428e0'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [UIKit](../../../uikit.md) · [UITabBarController](../../uitabbarcontroller.md) · [Sidebar](../sidebar-swift.class.md)

# UITabBarController.Sidebar.Layout

<sub>Enumeration</sub>

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
enum Layout
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../../../swift/bitwisecopyable.md), [Equatable](../../../swift/equatable.md), [Hashable](../../../swift/hashable.md), [RawRepresentable](../../../swift/rawrepresentable.md), [Sendable](../../../swift/sendable.md), [SendableMetatype](../../../swift/sendablemetatype.md)

## Topics

### Enumeration Cases

- [UITabBarControllerSidebarLayoutAutomatic](layout/automatic.md)
- [UITabBarControllerSidebarLayoutOverlap](layout/overlap.md) — When the sidebar is displayed, it will overlap the selected view controller, allowing the selected view controller to render underneath the sidebar. Anchor the view’s content to the `layoutMarginsGuide` or `safeAreaLayoutGuide` to avoid being occluded by the sidebar.
- [UITabBarControllerSidebarLayoutTile](layout/tile.md) — When the sidebar is displayed, the selected view controller is resized and shifted to display alongside the sidebar. The selected view controller is not occluded by the sidebar, cannot render underneath the sidebar.

### Initializers

- [init(rawValue:)](<layout/init(rawvalue_).md>)

## See Also

### Managing customization

- [hidden](ishidden.md) — Determines if the sidebar is currently hidden.
- [preferredLayout](preferredlayout.md) — The preferred layout for how the sidebar lays out with the tab bar controller’s content. Default is `.automatic`
- [- reconfigureItemForTab:](<reconfigureitem(for_).md>) — Requests the sidebar reconfigure the item representing the specified tab. This method has no effect if the `tab` is not currently displayed in the sidebar.
