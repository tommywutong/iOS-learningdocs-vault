---
title: automaticallyAdjustsScrollViewInsets
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+（11.0 起废弃）, iPadOS 7.0+（11.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）, tvOS 7.0+（11.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/uikit/uiviewcontroller/automaticallyadjustsscrollviewinsets
source_url: 'https://developer.apple.com/documentation/uikit/uiviewcontroller/automaticallyadjustsscrollviewinsets'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiviewcontroller/automaticallyadjustsscrollviewinsets.json'
content_hash: 'sha256:2d5f8de19551e8ce'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIViewController](../uiviewcontroller.md)

# automaticallyAdjustsScrollViewInsets

<sub>Instance Property</sub>

A Boolean value that indicates whether the view controller should automatically adjust its scroll view insets.

> [!warning] Deprecated
> Use [contentInsetAdjustmentBehavior](../uiscrollview/contentinsetadjustmentbehavior-swift.property.md) instead.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
var automaticallyAdjustsScrollViewInsets: Bool { get set }
```

## Discussion

The default value of this property is [true](../../swift/true.md), which lets container view controllers know that they should adjust the scroll view insets of this view controller’s view to account for screen areas consumed by a status bar, search bar, navigation bar, toolbar, or tab bar. Set this property to [false](../../swift/false.md) if your view controller implementation manages its own scroll view inset adjustments.

## See Also

### Deprecated properties

- [shouldAutorotate](shouldautorotate.md) — A Boolean value that indicates whether the view controller’s contents should autorotate. _(deprecated)_
- [previewActionItems](previewactionitems.md) — The quick actions displayed when a user swipes upward on a 3D Touch preview. _(deprecated)_
- [bottomLayoutGuide](bottomlayoutguide.md) — Indicates the lowest vertical extent for your onscreen content, for use with Auto Layout constraints. _(deprecated)_
- [interfaceOrientation](interfaceorientation.md) — Convenience property that provides the current orientation of the interface, meaningful only if the view controller is taking up the full screen. _(deprecated)_
- [modalInPopover](ismodalinpopover.md) — A Boolean value indicating whether the view controller should be presented modally by a popover. _(deprecated)_
- [searchDisplayController](searchdisplaycontroller.md) — The search display controller associated with the view controller. _(deprecated)_
- [topLayoutGuide](toplayoutguide.md) — Indicates the highest vertical extent for your onscreen content, for use with Auto Layout constraints. _(deprecated)_
