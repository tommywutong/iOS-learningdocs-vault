---
title: 'navigationBar(_:shouldPop:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uinavigationbardelegate/navigationbar(_:shouldpop:)'
source_url: 'https://developer.apple.com/documentation/uikit/uinavigationbardelegate/navigationbar(_:shouldpop:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uinavigationbardelegate/navigationbar%28_%3Ashouldpop%3A%29.json'
content_hash: 'sha256:88efb81a1bcc0519'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UINavigationBarDelegate](../uinavigationbardelegate.md)

# navigationBar(_:shouldPop:)

<sub>Instance Method</sub>

Returns a Boolean value indicating whether the navigation bar should pop an item.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional func navigationBar(_ navigationBar: UINavigationBar, shouldPop item: UINavigationItem) -> Bool
```

## Parameters

- `navigationBar` — The navigation bar that the item is being popped from.

- `item` — The navigation item that is being popped.

## Return Value

[true](../../swift/true.md) if the item should be popped; otherwise, [false](../../swift/false.md).

## Discussion

Sent to the delegate before popping an item from the navigation bar.

## See Also

### Popping items

- [- navigationBar:didPopItem:](<navigationbar(__didpop_).md>) — Tells the delegate that an item was popped from the navigation bar.
