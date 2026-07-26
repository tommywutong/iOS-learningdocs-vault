---
title: isModalInPopover
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 3.2+（13.0 起废弃）, iPadOS 3.2+（13.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）, tvOS（13.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/uikit/uiviewcontroller/ismodalinpopover
source_url: 'https://developer.apple.com/documentation/uikit/uiviewcontroller/ismodalinpopover'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiviewcontroller/ismodalinpopover.json'
content_hash: 'sha256:8d6c326dd34021bc'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIViewController](../uiviewcontroller.md)

# isModalInPopover

<sub>Instance Property</sub>

A Boolean value indicating whether the view controller should be presented modally by a popover.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
var isModalInPopover: Bool { get set }
```

## Discussion

The default value of this property is [false](../../swift/false.md). Setting it to [true](../../swift/true.md) causes an owning popover controller to disallow interactions outside this view controller while it is displayed. You can use this behavior to ensure that the popover is not dismissed by taps outside the popover controller.

## See Also

### Deprecated properties

- [shouldAutorotate](shouldautorotate.md) — A Boolean value that indicates whether the view controller’s contents should autorotate. _(deprecated)_
- [previewActionItems](previewactionitems.md) — The quick actions displayed when a user swipes upward on a 3D Touch preview. _(deprecated)_
- [automaticallyAdjustsScrollViewInsets](automaticallyadjustsscrollviewinsets.md) — A Boolean value that indicates whether the view controller should automatically adjust its scroll view insets. _(deprecated)_
- [bottomLayoutGuide](bottomlayoutguide.md) — Indicates the lowest vertical extent for your onscreen content, for use with Auto Layout constraints. _(deprecated)_
- [interfaceOrientation](interfaceorientation.md) — Convenience property that provides the current orientation of the interface, meaningful only if the view controller is taking up the full screen. _(deprecated)_
- [searchDisplayController](searchdisplaycontroller.md) — The search display controller associated with the view controller. _(deprecated)_
- [topLayoutGuide](toplayoutguide.md) — Indicates the highest vertical extent for your onscreen content, for use with Auto Layout constraints. _(deprecated)_
