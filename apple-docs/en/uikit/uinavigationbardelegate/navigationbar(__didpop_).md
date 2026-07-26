---
title: 'navigationBar(_:didPop:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uinavigationbardelegate/navigationbar(_:didpop:)'
source_url: 'https://developer.apple.com/documentation/uikit/uinavigationbardelegate/navigationbar(_:didpop:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uinavigationbardelegate/navigationbar%28_%3Adidpop%3A%29.json'
content_hash: 'sha256:803c9d71265696c7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UINavigationBarDelegate](../uinavigationbardelegate.md)

# navigationBar(_:didPop:)

<sub>Instance Method</sub>

Tells the delegate that an item was popped from the navigation bar.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional func navigationBar(_ navigationBar: UINavigationBar, didPop item: UINavigationItem)
```

## Parameters

- `navigationBar` — The navigation bar that the item is being popped from.

- `item` — The navigation item that is being popped.

## Discussion

If animating the pop operation, this method is invoked after the animation ends; otherwise, it is invoked immediately after the pop.

## See Also

### Popping items

- [- navigationBar:shouldPopItem:](<navigationbar(__shouldpop_).md>) — Returns a Boolean value indicating whether the navigation bar should pop an item.
