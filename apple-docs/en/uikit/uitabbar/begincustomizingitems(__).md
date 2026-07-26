---
title: 'beginCustomizingItems(_:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uitabbar/begincustomizingitems(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/uitabbar/begincustomizingitems(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitabbar/begincustomizingitems%28_%3A%29.json'
content_hash: 'sha256:5071e73b8478409a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITabBar](../uitabbar.md)

# beginCustomizingItems(_:)

<sub>Instance Method</sub>

Presents a standard interface that lets the user customize the contents of the tab bar.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
func beginCustomizingItems(_ items: [UITabBarItem])
```

## Parameters

- `items` — An array of [UITabBarItem](../uitabbaritem.md) objects representing all of the items that can possibly be displayed on the tab bar. Always include at least one visible item in the tab bar. This parameter must not be `nil` or contain an empty array.

## Discussion

This method presents a custom interface that lets the user replace existing tab bar items with items in the specified array. The interface also lets the user rearrange items on the tab bar, but it does not let the user change the total number of items. The interface includes a Done button that automatically dismisses the interface. You can also dismiss the interface programmatically using the [- endCustomizingAnimated:](<endcustomizing(animated_).md>) method.

> [!important] Important
> You cannot use this method to customize a tab bar that is managed by a tab bar controller. For information about how to customize the contents of a tab bar controller, see the [UITabBarController](../uitabbarcontroller.md).

The `items` parameter should include all items currently visible in the tab bar that you allow to be replaced. Any currently visible items that are not included in this array remain fixed in place on the tab bar and cannot be repositioned or replaced by the user. If the user removes the currently selected item from the tab bar, the [selectedItem](selecteditem.md) property is set to `nil`.

The tab bar notifies its delegate about the pending customizations at various points during the presentation and dismissal of the interface. If you want to track when customizations begin and end, provide a delegate and assign it to the tab bar’s [delegate](delegate.md) property. For more information about the methods you can implement, see [UITabBarDelegate](../uitabbardelegate.md).

## See Also

### Supporting user customization of tab bars

- [- endCustomizingAnimated:](<endcustomizing(animated_).md>) — Dismisses the standard interface used to customize the tab bar.
- [customizing](iscustomizing.md) — A Boolean value indicating whether the user is currently customizing the tab bar.
