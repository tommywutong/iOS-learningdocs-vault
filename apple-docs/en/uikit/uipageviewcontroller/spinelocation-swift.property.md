---
title: spineLocation
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uipageviewcontroller/spinelocation-swift.property
source_url: 'https://developer.apple.com/documentation/uikit/uipageviewcontroller/spinelocation-swift.property'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uipageviewcontroller/spinelocation-swift.property.json'
content_hash: 'sha256:583dcc5f9b451f1b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPageViewController](../uipageviewcontroller.md)

# spineLocation

<sub>Instance Property</sub>

The location of the spine.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var spineLocation: UIPageViewController.SpineLocation { get }
```

## Discussion

The value of this property is set with the [UIPageViewControllerOptionSpineLocationKey](optionskey/spinelocation.md) key when the page view controller is initialized, and can be changed by returning the new value from the [- pageViewController:spineLocationForInterfaceOrientation:](<../uipageviewcontrollerdelegate/pageviewcontroller(__spinelocationfor_).md>) method of the delegate.

## See Also

### Display Options

- [navigationOrientation](navigationorientation-swift.property.md) — The direction along which navigation occurs.
- [NavigationOrientation](navigationorientation-swift.enum.md) — Orientations for page-turn transitions.
- [SpineLocation](spinelocation-swift.enum.md) — Locations for the spine.
- [transitionStyle](transitionstyle-swift.property.md) — The style used to transition between view controllers.
- [TransitionStyle](transitionstyle-swift.enum.md) — Styles for the page-turn transition.
- [doubleSided](isdoublesided.md) — A Boolean value that indicates whether content appears on the back of pages.
