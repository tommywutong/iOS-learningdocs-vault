---
title: UITabBarController.Mode
framework: UIKit
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, tvOS 18.0+, visionOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitabbarcontroller/mode-swift.enum
source_url: 'https://developer.apple.com/documentation/uikit/uitabbarcontroller/mode-swift.enum'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitabbarcontroller/mode-swift.enum.json'
content_hash: 'sha256:8d44d099c5e50d55'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITabBarController](../uitabbarcontroller.md)

# UITabBarController.Mode

<sub>Enumeration</sub>

A tab bar’s display mode.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
enum Mode
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Setting modes

- [UITabBarControllerModeAutomatic](mode-swift.enum/automatic.md) — The system sets the display mode based on the tab’s content.
- [UITabBarControllerModeTabBar](mode-swift.enum/tabbar.md) — The system displays the content only as a tab bar.
- [UITabBarControllerModeTabSidebar](mode-swift.enum/tabsidebar.md) — The system displays the content as either a tab bar or a sidebar, depending on the context.

### Initializers

- [init(rawValue:)](<mode-swift.enum/init(rawvalue_).md>)

## See Also

### Supporting the sidebar

- [mode](mode-swift.property.md) — The display mode for a tab bar.
- [sidebar](sidebar-swift.property.md) — A tab bar’s corresponding sidebar.
- [Sidebar](sidebar-swift.class.md) — An object for managing and configuring the sidebar.
- [UITabSidebarItem](../uitabsidebaritem.md)
- [Request](../uitabsidebaritem/request.md)
- [Animating](sidebar-swift.class/animating.md)
