---
title: 'show(_:sender:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uinavigationcontroller/show(_:sender:)'
source_url: 'https://developer.apple.com/documentation/uikit/uinavigationcontroller/show(_:sender:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uinavigationcontroller/show%28_%3Asender%3A%29.json'
content_hash: 'sha256:b97697ec0f34050e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UINavigationController](../uinavigationcontroller.md)

# show(_:sender:)

<sub>Instance Method</sub>

Presents the specified view controller in the navigation interface.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func show(_ vc: UIViewController, sender: Any?)
```

## Parameters

- `vc` — The view controller to display.

- `sender` — The object that made the request to show the view controller.

## Discussion

This method pushes `vc` onto the navigation stack in a similar way as the [- pushViewController:animated:](<pushviewcontroller(__animated_).md>) method. You can call this method directly if you want but typically this method is called from elsewhere in the view controller hierarchy when a new view controller needs to be shown.

The Show segue uses this method to display a new view controller.
