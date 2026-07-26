---
title: 'tabBar(_:willEndCustomizing:changed:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uitabbardelegate/tabbar(_:willendcustomizing:changed:)'
source_url: 'https://developer.apple.com/documentation/uikit/uitabbardelegate/tabbar(_:willendcustomizing:changed:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitabbardelegate/tabbar%28_%3Awillendcustomizing%3Achanged%3A%29.json'
content_hash: 'sha256:729af4f94b0468ec'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITabBarDelegate](../uitabbardelegate.md)

# tabBar(_:willEndCustomizing:changed:)

<sub>Instance Method</sub>

Sent to the delegate before the customizing modal view is dismissed.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
optional func tabBar(_ tabBar: UITabBar, willEndCustomizing items: [UITabBarItem], changed: Bool)
```

## Parameters

- `tabBar` — The tab bar that is being customized.

- `items` — The items on the customizing modal view.

- `changed` — [true](../../swift/true.md) if the visible set of items on the tab bar changed; otherwise, [false](../../swift/false.md).

## See Also

### Customizing tab bars

- [- tabBar:willBeginCustomizingItems:](<tabbar(__willbegincustomizing_).md>) — Sent to the delegate before the customizing modal view is displayed.
- [- tabBar:didBeginCustomizingItems:](<tabbar(__didbegincustomizing_).md>) — Sent to the delegate after the customizing modal view is displayed.
- [- tabBar:didEndCustomizingItems:changed:](<tabbar(__didendcustomizing_changed_).md>) — Sent to the delegate after the customizing modal view is dismissed.
- [- tabBar:didSelectItem:](<tabbar(__didselect_).md>) — Sent to the delegate when the user selects a tab bar item.
