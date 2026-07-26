---
title: delegate
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitabbar/delegate
source_url: 'https://developer.apple.com/documentation/uikit/uitabbar/delegate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitabbar/delegate.json'
content_hash: 'sha256:2b44155e36c952bd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITabBar](../uitabbar.md)

# delegate

<sub>Instance Property</sub>

The tab bar’s delegate object.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
weak var delegate: (any UITabBarDelegate)? { get set }
```

## Discussion

Use the delegate to track the selection of tab bar items and to respond to the user customization of the tab bar. The default value of this property is `nil`.

For more information on how to implement the methods of this protocol, see [UITabBarDelegate](../uitabbardelegate.md).

## See Also

### Customizing the tab bar behavior

- [UITabBarDelegate](../uitabbardelegate.md) — The [UITabBarDelegate](../uitabbardelegate.md) protocol defines optional methods for a delegate of a [UITabBar](../uitabbar.md) object. The [UITabBar](../uitabbar.md) class provides the ability for the user to reorder, remove, and add items to the tab bar; this process is referred to as customizing the tab bar. The tab bar delegate receives messages when customizing occurs.
