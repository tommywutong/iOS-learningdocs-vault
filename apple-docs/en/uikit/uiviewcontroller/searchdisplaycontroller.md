---
title: searchDisplayController
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 3.0+（8.0 起废弃）, iPadOS 3.0+（8.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/uikit/uiviewcontroller/searchdisplaycontroller
source_url: 'https://developer.apple.com/documentation/uikit/uiviewcontroller/searchdisplaycontroller'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiviewcontroller/searchdisplaycontroller.json'
content_hash: 'sha256:94fdcd5b46f4ec7c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIViewController](../uiviewcontroller.md)

# searchDisplayController

<sub>Instance Property</sub>

The search display controller associated with the view controller.

> [!warning] Deprecated
> Use the [UISearchController](../uisearchcontroller.md) class to integrate search results.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
var searchDisplayController: UISearchDisplayController? { get }
```

## Discussion

This property reflects the value of the `searchDisplayController` outlet that you set in Interface Builder. If you create your search display controller programmatically, this property is set automatically by the search display controller when it is initialized.

## See Also

### Deprecated properties

- [shouldAutorotate](shouldautorotate.md) — A Boolean value that indicates whether the view controller’s contents should autorotate. _(deprecated)_
- [previewActionItems](previewactionitems.md) — The quick actions displayed when a user swipes upward on a 3D Touch preview. _(deprecated)_
- [automaticallyAdjustsScrollViewInsets](automaticallyadjustsscrollviewinsets.md) — A Boolean value that indicates whether the view controller should automatically adjust its scroll view insets. _(deprecated)_
- [bottomLayoutGuide](bottomlayoutguide.md) — Indicates the lowest vertical extent for your onscreen content, for use with Auto Layout constraints. _(deprecated)_
- [interfaceOrientation](interfaceorientation.md) — Convenience property that provides the current orientation of the interface, meaningful only if the view controller is taking up the full screen. _(deprecated)_
- [modalInPopover](ismodalinpopover.md) — A Boolean value indicating whether the view controller should be presented modally by a popover. _(deprecated)_
- [topLayoutGuide](toplayoutguide.md) — Indicates the highest vertical extent for your onscreen content, for use with Auto Layout constraints. _(deprecated)_
