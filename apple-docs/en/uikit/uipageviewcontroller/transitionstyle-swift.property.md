---
title: transitionStyle
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uipageviewcontroller/transitionstyle-swift.property
source_url: 'https://developer.apple.com/documentation/uikit/uipageviewcontroller/transitionstyle-swift.property'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uipageviewcontroller/transitionstyle-swift.property.json'
content_hash: 'sha256:67cef8aa48a564f7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPageViewController](../uipageviewcontroller.md)

# transitionStyle

<sub>Instance Property</sub>

The style used to transition between view controllers.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var transitionStyle: UIPageViewController.TransitionStyle { get }
```

## Discussion

The value of this property is set when the page view controller is initialized, and cannot be changed.

## See Also

### Display Options

- [navigationOrientation](navigationorientation-swift.property.md) — The direction along which navigation occurs.
- [NavigationOrientation](navigationorientation-swift.enum.md) — Orientations for page-turn transitions.
- [spineLocation](spinelocation-swift.property.md) — The location of the spine.
- [SpineLocation](spinelocation-swift.enum.md) — Locations for the spine.
- [TransitionStyle](transitionstyle-swift.enum.md) — Styles for the page-turn transition.
- [doubleSided](isdoublesided.md) — A Boolean value that indicates whether content appears on the back of pages.
