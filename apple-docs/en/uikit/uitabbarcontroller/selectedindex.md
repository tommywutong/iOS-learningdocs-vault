---
title: selectedIndex
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitabbarcontroller/selectedindex
source_url: 'https://developer.apple.com/documentation/uikit/uitabbarcontroller/selectedindex'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitabbarcontroller/selectedindex.json'
content_hash: 'sha256:91d7794a166b833c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITabBarController](../uitabbarcontroller.md)

# selectedIndex

<sub>Instance Property</sub>

The index of the view controller associated with the currently selected tab item.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var selectedIndex: Int { get set }
```

## Discussion

This property nominally represents an index into the array of the [viewControllers](viewcontrollers.md) property. However, if the selected view controller is currently the More navigation controller, this property contains the value `NSNotFound`. Setting this property changes the selected view controller to the one at the designated index in the [viewControllers](viewcontrollers.md) array. To select the More navigation controller itself, you must change the value of the [selectedViewController](selectedviewcontroller.md) property instead.

In versions of iOS prior to version 3.0, this property reflects the index of the selected tab bar item only. Attempting to set this value to an index of a view controller that is not visible in the tab bar, but is instead managed by the More navigation controller, has no effect.

> [!note] Note
> The More interface is not available in tvOS.

## See Also

### Managing the selected tab

- [selectedTab](selectedtab.md) — The currently selected tab, which can be a root tab or any of their descendants.
- [selectedViewController](selectedviewcontroller.md) — The view controller associated with the currently selected tab item.
