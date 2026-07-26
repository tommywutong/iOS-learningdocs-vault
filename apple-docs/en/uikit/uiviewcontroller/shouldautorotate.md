---
title: shouldAutorotate
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 6.0+（16.0 起废弃）, iPadOS 6.0+（16.0 起废弃）, Mac Catalyst 13.1+（16.0 起废弃）, visionOS 1.0+（1.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/uikit/uiviewcontroller/shouldautorotate
source_url: 'https://developer.apple.com/documentation/uikit/uiviewcontroller/shouldautorotate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiviewcontroller/shouldautorotate.json'
content_hash: 'sha256:92051be9041d2a8b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIViewController](../uiviewcontroller.md)

# shouldAutorotate

<sub>Instance Property</sub>

A Boolean value that indicates whether the view controller’s contents should autorotate.

> [!warning] Deprecated
> Instead, update [supportedInterfaceOrientations](supportedinterfaceorientations.md) and then call [- setNeedsUpdateOfSupportedInterfaceOrientations](<setneedsupdateofsupportedinterfaceorientations().md>) to indicate a change to the supported interface orientations.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var shouldAutorotate: Bool { get }
```

## Return Value

[true](../../swift/true.md) if the content should rotate, otherwise [false](../../swift/false.md). This method returns [true](../../swift/true.md) by default.

## See Also

### Deprecated properties

- [previewActionItems](previewactionitems.md) — The quick actions displayed when a user swipes upward on a 3D Touch preview. _(deprecated)_
- [automaticallyAdjustsScrollViewInsets](automaticallyadjustsscrollviewinsets.md) — A Boolean value that indicates whether the view controller should automatically adjust its scroll view insets. _(deprecated)_
- [bottomLayoutGuide](bottomlayoutguide.md) — Indicates the lowest vertical extent for your onscreen content, for use with Auto Layout constraints. _(deprecated)_
- [interfaceOrientation](interfaceorientation.md) — Convenience property that provides the current orientation of the interface, meaningful only if the view controller is taking up the full screen. _(deprecated)_
- [modalInPopover](ismodalinpopover.md) — A Boolean value indicating whether the view controller should be presented modally by a popover. _(deprecated)_
- [searchDisplayController](searchdisplaycontroller.md) — The search display controller associated with the view controller. _(deprecated)_
- [topLayoutGuide](toplayoutguide.md) — Indicates the highest vertical extent for your onscreen content, for use with Auto Layout constraints. _(deprecated)_
