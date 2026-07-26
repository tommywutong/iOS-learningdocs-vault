---
title: 'navigationBar(_:didPush:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uinavigationbardelegate/navigationbar(_:didpush:)'
source_url: 'https://developer.apple.com/documentation/uikit/uinavigationbardelegate/navigationbar(_:didpush:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uinavigationbardelegate/navigationbar%28_%3Adidpush%3A%29.json'
content_hash: 'sha256:1ccc359b2c549086'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UINavigationBarDelegate](../uinavigationbardelegate.md)

# navigationBar(_:didPush:)

<sub>Instance Method</sub>

Tells the delegate that an item was pushed onto the navigation bar.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional func navigationBar(_ navigationBar: UINavigationBar, didPush item: UINavigationItem)
```

## Parameters

- `navigationBar` — The navigation bar that the item is being pushed onto.

- `item` — The navigation item that is being pushed.

## Discussion

If pushing an item onto the navigation bar is animated, this method is invoked after the animation ends; otherwise, it is invoked immediately after the push.

## See Also

### Pushing items

- [- navigationBar:shouldPushItem:](<navigationbar(__shouldpush_).md>) — Returns a Boolean value indicating whether the navigation bar should push an item.
