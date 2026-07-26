---
title: UITabBarController.Mode.tabSidebar
framework: UIKit
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, visionOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitabbarcontroller/mode-swift.enum/tabsidebar
source_url: 'https://developer.apple.com/documentation/uikit/uitabbarcontroller/mode-swift.enum/tabsidebar'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitabbarcontroller/mode-swift.enum/tabsidebar.json'
content_hash: 'sha256:87c029ff5040d33b'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [UIKit](../../../uikit.md) · [UITabBarController](../../uitabbarcontroller.md) · [Mode](../mode-swift.enum.md)

# UITabBarController.Mode.tabSidebar

<sub>Case</sub>

The system displays the content as either a tab bar or a sidebar, depending on the context.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
case tabSidebar
```

## Discussion

Different platforms handle the mode differently:

- On iPad, the system displays the content as either a tab bar or a sidebar, depending on the context.
- On Mac Catalyst, the system displays a sidebar.
- On iPhone and Apple TV, the system displays the platform’s regular tab bar.
- In visionOS, the system displays the platform’s regular tabs, but a [UITabGroup](../../uitabgroup.md) can display a sidebar when it displays the group’s view controller.

For more information, see [Elevating your iPad app with a tab bar and sidebar](../../elevating-your-ipad-app-with-a-tab-bar-and-sidebar.md).

## See Also

### Setting modes

- [UITabBarControllerModeAutomatic](automatic.md) — The system sets the display mode based on the tab’s content.
- [UITabBarControllerModeTabBar](tabbar.md) — The system displays the content only as a tab bar.
