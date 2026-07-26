---
title: UITabBarDelegate
framework: UIKit
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitabbardelegate
source_url: 'https://developer.apple.com/documentation/uikit/uitabbardelegate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitabbardelegate.json'
content_hash: 'sha256:189c351b581fd113'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UITabBarDelegate

<sub>Protocol</sub>

The [UITabBarDelegate](uitabbardelegate.md) protocol defines optional methods for a delegate of a [UITabBar](uitabbar.md) object. The [UITabBar](uitabbar.md) class provides the ability for the user to reorder, remove, and add items to the tab bar; this process is referred to as customizing the tab bar. The tab bar delegate receives messages when customizing occurs.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor protocol UITabBarDelegate : NSObjectProtocol
```

## Overview

Send [- beginCustomizingItems:](<uitabbar/begincustomizingitems(__).md>) to a [UITabBar](uitabbar.md) object to begin customizing. Implement the methods in Customizing tab bars to intervene while a user is customizing a tab bar. The customizing modal view is dismissed when the user taps the Done button on the modal view.

## Relationships

- **Inherits From**: [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

- **Conforming Types**: [UITabBarController](uitabbarcontroller.md)

## Topics

### Customizing tab bars

- [- tabBar:willBeginCustomizingItems:](<uitabbardelegate/tabbar(__willbegincustomizing_).md>) — Sent to the delegate before the customizing modal view is displayed.
- [- tabBar:didBeginCustomizingItems:](<uitabbardelegate/tabbar(__didbegincustomizing_).md>) — Sent to the delegate after the customizing modal view is displayed.
- [- tabBar:willEndCustomizingItems:changed:](<uitabbardelegate/tabbar(__willendcustomizing_changed_).md>) — Sent to the delegate before the customizing modal view is dismissed.
- [- tabBar:didEndCustomizingItems:changed:](<uitabbardelegate/tabbar(__didendcustomizing_changed_).md>) — Sent to the delegate after the customizing modal view is dismissed.
- [- tabBar:didSelectItem:](<uitabbardelegate/tabbar(__didselect_).md>) — Sent to the delegate when the user selects a tab bar item.

## See Also

### Customizing the tab bar behavior

- [delegate](uitabbar/delegate.md) — The tab bar’s delegate object.
