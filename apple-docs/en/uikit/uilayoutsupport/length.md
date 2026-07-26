---
title: length
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uilayoutsupport/length
source_url: 'https://developer.apple.com/documentation/uikit/uilayoutsupport/length'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uilayoutsupport/length.json'
content_hash: 'sha256:dce87c354044cfc1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UILayoutSupport](../uilayoutsupport.md)

# length

<sub>Instance Property</sub>

Provides the length, in points, of the portion of a view controller’s view that is overlaid by translucent or transparent UIKit bars.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var length: CGFloat { get }
```

## Discussion

In iOS 7 and later, a view controller’s view occupies the full height of the screen when there are no opaque UIKit bars (such as opaque navigation or tab bars). To keep your content within the area of a view that is not overlaid by translucent or transparent UIKit bars, employ the [topLayoutGuide](../uiviewcontroller/toplayoutguide.md) and [bottomLayoutGuide](../uiviewcontroller/bottomlayoutguide.md) properties in the [UIViewController](../uiviewcontroller.md) class and take advantage of Auto Layout. Query these properties within your implementation of the [UIViewController](../uiviewcontroller.md) method [- viewDidLayoutSubviews](<../uiviewcontroller/viewdidlayoutsubviews().md>).

The guides work as follows:

- The top layout guide indicates the distance, in points, between the top of a view controller’s view and the bottom of the bottommost bar that overlays the view
- The bottom layout guide indicates the distance, in points, between the bottom of a view controller’s view and the top the bar (such as a tab bar) that overlays the view.

If you are not using Auto Layout, you can make use of the [length](length.md) property and perform layout calculations yourself. Refer to the code snippets in the descriptions for the [topLayoutGuide](../uiviewcontroller/toplayoutguide.md) and [bottomLayoutGuide](../uiviewcontroller/bottomlayoutguide.md) properties, which explain how to obtain the numbers you need.
