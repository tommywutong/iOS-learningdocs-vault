---
title: 'tabBar(_:didSelect:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uitabbardelegate/tabbar(_:didselect:)'
source_url: 'https://developer.apple.com/documentation/uikit/uitabbardelegate/tabbar(_:didselect:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitabbardelegate/tabbar%28_%3Adidselect%3A%29.json'
content_hash: 'sha256:c6620b3b33b58362'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITabBarDelegate](../uitabbardelegate.md)

# tabBar(_:didSelect:)

<sub>Instance Method</sub>

Sent to the delegate when the user selects a tab bar item.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional func tabBar(_ tabBar: UITabBar, didSelect item: UITabBarItem)
```

## Parameters

- `tabBar` — The tab bar that is being customized.

- `item` — The tab bar item that was selected.

## See Also

### Customizing tab bars

- [- tabBar:willBeginCustomizingItems:](<tabbar(__willbegincustomizing_).md>) — Sent to the delegate before the customizing modal view is displayed.
- [- tabBar:didBeginCustomizingItems:](<tabbar(__didbegincustomizing_).md>) — Sent to the delegate after the customizing modal view is displayed.
- [- tabBar:willEndCustomizingItems:changed:](<tabbar(__willendcustomizing_changed_).md>) — Sent to the delegate before the customizing modal view is dismissed.
- [- tabBar:didEndCustomizingItems:changed:](<tabbar(__didendcustomizing_changed_).md>) — Sent to the delegate after the customizing modal view is dismissed.
