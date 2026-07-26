---
title: interfaceOrientation
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+（8.0 起废弃）, iPadOS 2.0+（8.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/uikit/uiviewcontroller/interfaceorientation
source_url: 'https://developer.apple.com/documentation/uikit/uiviewcontroller/interfaceorientation'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiviewcontroller/interfaceorientation.json'
content_hash: 'sha256:012854c1d32762cf'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIViewController](../uiviewcontroller.md)

# interfaceOrientation

<sub>Instance Property</sub>

Convenience property that provides the current orientation of the interface, meaningful only if the view controller is taking up the full screen.

> [!warning] Deprecated
> Use [- viewWillTransitionToSize:withTransitionCoordinator:](<../uicontentcontainer/viewwilltransition(to_with_).md>) to make interface-based adjustments.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
var interfaceOrientation: UIInterfaceOrientation { get }
```

## Discussion

Do not use this property for informing layout decisions.

The possible values for the [interfaceOrientation](interfaceorientation.md) property are described in the [UIInterfaceOrientation](../uiinterfaceorientation.md) enum.

## See Also

### Deprecated properties

- [shouldAutorotate](shouldautorotate.md) — A Boolean value that indicates whether the view controller’s contents should autorotate. _(deprecated)_
- [previewActionItems](previewactionitems.md) — The quick actions displayed when a user swipes upward on a 3D Touch preview. _(deprecated)_
- [automaticallyAdjustsScrollViewInsets](automaticallyadjustsscrollviewinsets.md) — A Boolean value that indicates whether the view controller should automatically adjust its scroll view insets. _(deprecated)_
- [bottomLayoutGuide](bottomlayoutguide.md) — Indicates the lowest vertical extent for your onscreen content, for use with Auto Layout constraints. _(deprecated)_
- [modalInPopover](ismodalinpopover.md) — A Boolean value indicating whether the view controller should be presented modally by a popover. _(deprecated)_
- [searchDisplayController](searchdisplaycontroller.md) — The search display controller associated with the view controller. _(deprecated)_
- [topLayoutGuide](toplayoutguide.md) — Indicates the highest vertical extent for your onscreen content, for use with Auto Layout constraints. _(deprecated)_
