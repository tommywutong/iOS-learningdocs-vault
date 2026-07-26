---
title: UITabBarController.Mode.automatic
framework: UIKit
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, tvOS 18.0+, visionOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitabbarcontroller/mode-swift.enum/automatic
source_url: 'https://developer.apple.com/documentation/uikit/uitabbarcontroller/mode-swift.enum/automatic'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitabbarcontroller/mode-swift.enum/automatic.json'
content_hash: 'sha256:912078ba4bbe326e'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [UIKit](../../../uikit.md) · [UITabBarController](../../uitabbarcontroller.md) · [Mode](../mode-swift.enum.md)

# UITabBarController.Mode.automatic

<sub>Case</sub>

The system sets the display mode based on the tab’s content.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
case automatic
```

## Discussion

Different platforms handle the mode differently:

- On iPad, If the [tabs](../tabs.md) array contains one or more [UITabGroup](../../uitabgroup.md) items, the system displays the content as either a tab bar or a sidebar, depending on the context. Otherwise, it only displays the content only as a tab bar.
- On Mac Catalyst, the system displays a sidebar if the [tabs](../tabs.md) array contains one or more [UITabGroup](../../uitabgroup.md) items. Otherwise, it displays a tab bar.
- On iPhone and Apple TV, the system displays the platform’s regular tab bar.
- In visionOS, the system displays the platform’s regular tabs, but a [UITabGroup](../../uitabgroup.md) can display a sidebar when it displays the group’s view controller.

For more information, see [Elevating your iPad app with a tab bar and sidebar](../../elevating-your-ipad-app-with-a-tab-bar-and-sidebar.md).

## See Also

### Setting modes

- [UITabBarControllerModeTabBar](tabbar.md) — The system displays the content only as a tab bar.
- [UITabBarControllerModeTabSidebar](tabsidebar.md) — The system displays the content as either a tab bar or a sidebar, depending on the context.
