---
title: rootViewController
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiwindow/rootviewcontroller
source_url: 'https://developer.apple.com/documentation/uikit/uiwindow/rootviewcontroller'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiwindow/rootviewcontroller.json'
content_hash: 'sha256:792e630617d17836'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIWindow](../uiwindow.md)

# rootViewController

<sub>Instance Property</sub>

The root view controller for the window.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var rootViewController: UIViewController? { get set }
```

## Discussion

The root view controller provides the content view of the window. Assigning a view controller to this property (either programmatically or using Interface Builder) installs the view controller’s view as the content view of the window. The new content view is configured to track the window size, changing as the window size changes. If the window has an existing view hierarchy, the old views are removed before the new ones are installed.

The default value of this property is `nil`.

## See Also

### Configuring the window

- [windowLevel](windowlevel.md) — The position of the window in the z-axis.
- [Level](level.md) — The positioning of windows relative to each other.
- [canResizeToFitContent](canresizetofitcontent.md) — A Boolean value that indicates whether the window’s constraint-based content determines its size.
- [screen](screen.md) — The screen to display the window on. _(deprecated)_
