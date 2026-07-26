---
title: 'navigationBar(_:shouldPush:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uinavigationbardelegate/navigationbar(_:shouldpush:)'
source_url: 'https://developer.apple.com/documentation/uikit/uinavigationbardelegate/navigationbar(_:shouldpush:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uinavigationbardelegate/navigationbar%28_%3Ashouldpush%3A%29.json'
content_hash: 'sha256:f895ffe517118887'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UINavigationBarDelegate](../uinavigationbardelegate.md)

# navigationBar(_:shouldPush:)

<sub>Instance Method</sub>

Returns a Boolean value indicating whether the navigation bar should push an item.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional func navigationBar(_ navigationBar: UINavigationBar, shouldPush item: UINavigationItem) -> Bool
```

## Parameters

- `navigationBar` — The navigation bar that the item is being pushed onto.

- `item` — The navigation item that is being pushed.

## Return Value

[true](../../swift/true.md) if the item should be pushed; otherwise, [false](../../swift/false.md).

## Discussion

Sent to the delegate before pushing an item onto the navigation bar.

## See Also

### Pushing items

- [- navigationBar:didPushItem:](<navigationbar(__didpush_).md>) — Tells the delegate that an item was pushed onto the navigation bar.
