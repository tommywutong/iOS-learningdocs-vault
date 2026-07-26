---
title: previewActionItems
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 9.0+（13.0 起废弃）, iPadOS 9.0+（13.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）, tvOS 9.0+（13.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/uikit/uiviewcontroller/previewactionitems
source_url: 'https://developer.apple.com/documentation/uikit/uiviewcontroller/previewactionitems'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiviewcontroller/previewactionitems.json'
content_hash: 'sha256:e9b671dbd1447a14'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIViewController](../uiviewcontroller.md)

# previewActionItems

<sub>Instance Property</sub>

The quick actions displayed when a user swipes upward on a 3D Touch preview.

> [!warning] Deprecated
> Use [UIContextMenuInteraction](../uicontextmenuinteraction.md) instead.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
var previewActionItems: [any UIPreviewActionItem] { get }
```

## Return Value

An array of preview (peek) quick actions.

## Discussion

This property is for use with a preview (peek) view controller which you present in your implementation of the [- previewingContext:viewControllerForLocation:](<../uiviewcontrollerpreviewingdelegate/previewingcontext(__viewcontrollerforlocation_).md>) delegate method..

Implement this method to provide quick actions for such a preview. When the user swipes upward on the preview, the system presents these quick action items in a sheet below the preview.

The default implementation of this method returns an empty array.

For guidance on appropriate items to include as preview quick actions, read the material on 3D Touch in the [iOS Technologies](https://developer.apple.com/library/archive/documentation/UserExperience/Conceptual/MobileHIG/3DTouch.html#//apple_ref/doc/uid/TP40006556-CH31) chapter of [iOS Human Interface Guidelines](https://developer.apple.com/ios/human-interface-guidelines/).

For more information on preview quick actions, see [UIPreviewActionItem](../uipreviewactionitem.md) and [UIPreviewAction](../uipreviewaction.md).

## See Also

### Deprecated properties

- [shouldAutorotate](shouldautorotate.md) — A Boolean value that indicates whether the view controller’s contents should autorotate. _(deprecated)_
- [automaticallyAdjustsScrollViewInsets](automaticallyadjustsscrollviewinsets.md) — A Boolean value that indicates whether the view controller should automatically adjust its scroll view insets. _(deprecated)_
- [bottomLayoutGuide](bottomlayoutguide.md) — Indicates the lowest vertical extent for your onscreen content, for use with Auto Layout constraints. _(deprecated)_
- [interfaceOrientation](interfaceorientation.md) — Convenience property that provides the current orientation of the interface, meaningful only if the view controller is taking up the full screen. _(deprecated)_
- [modalInPopover](ismodalinpopover.md) — A Boolean value indicating whether the view controller should be presented modally by a popover. _(deprecated)_
- [searchDisplayController](searchdisplaycontroller.md) — The search display controller associated with the view controller. _(deprecated)_
- [topLayoutGuide](toplayoutguide.md) — Indicates the highest vertical extent for your onscreen content, for use with Auto Layout constraints. _(deprecated)_
