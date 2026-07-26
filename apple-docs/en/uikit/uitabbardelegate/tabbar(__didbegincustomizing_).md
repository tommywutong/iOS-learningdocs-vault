---
title: 'tabBar(_:didBeginCustomizing:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uitabbardelegate/tabbar(_:didbegincustomizing:)'
source_url: 'https://developer.apple.com/documentation/uikit/uitabbardelegate/tabbar(_:didbegincustomizing:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitabbardelegate/tabbar%28_%3Adidbegincustomizing%3A%29.json'
content_hash: 'sha256:4d3cac29ee1bd39c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITabBarDelegate](../uitabbardelegate.md)

# tabBar(_:didBeginCustomizing:)

<sub>Instance Method</sub>

Sent to the delegate after the customizing modal view is displayed.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
optional func tabBar(_ tabBar: UITabBar, didBeginCustomizing items: [UITabBarItem])
```

## Parameters

- `tabBar` — The tab bar that is being customized.

- `items` — The items on the customizing modal view.

## See Also

### Customizing tab bars

- [- tabBar:willBeginCustomizingItems:](<tabbar(__willbegincustomizing_).md>) — Sent to the delegate before the customizing modal view is displayed.
- [- tabBar:willEndCustomizingItems:changed:](<tabbar(__willendcustomizing_changed_).md>) — Sent to the delegate before the customizing modal view is dismissed.
- [- tabBar:didEndCustomizingItems:changed:](<tabbar(__didendcustomizing_changed_).md>) — Sent to the delegate after the customizing modal view is dismissed.
- [- tabBar:didSelectItem:](<tabbar(__didselect_).md>) — Sent to the delegate when the user selects a tab bar item.
