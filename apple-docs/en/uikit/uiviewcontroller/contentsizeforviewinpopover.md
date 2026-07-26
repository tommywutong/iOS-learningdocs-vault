---
title: contentSizeForViewInPopover
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 3.2+（7.0 起废弃）, iPadOS 3.2+（7.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: /documentation/uikit/uiviewcontroller/contentsizeforviewinpopover
source_url: 'https://developer.apple.com/documentation/uikit/uiviewcontroller/contentsizeforviewinpopover'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiviewcontroller/contentsizeforviewinpopover.json'
content_hash: 'sha256:fb8aff1fd2341210'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIViewController](../uiviewcontroller.md)

# contentSizeForViewInPopover

<sub>Instance Property</sub>

The size of the view controller’s view while displayed in a popover.

> [!warning] Deprecated
> Use [preferredContentSize](preferredcontentsize.md) instead.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
@property (nonatomic, readwrite) CGSize contentSizeForViewInPopover;
```

## Discussion

This property contains the desired size for the view controller when it is displayed in a popover. By default, the width is set to 320 points and the height is set to 1100 points. You can change these values as needed.

The recommended width for popovers is 320 points. If needed, you can return a width value as large as 600 points, but doing so is not recommended.

If the popover controller displaying the view controller sets its [popoverContentSize](../uipopovercontroller/contentsize.md) property, the popover controller overrides the values set in the view controller’s [contentSizeForViewInPopover](contentsizeforviewinpopover.md) property.

## See Also

### Deprecated properties

- [shouldAutorotate](shouldautorotate.md) — A Boolean value that indicates whether the view controller’s contents should autorotate. _(deprecated)_
- [previewActionItems](previewactionitems.md) — The quick actions displayed when a user swipes upward on a 3D Touch preview. _(deprecated)_
- [automaticallyAdjustsScrollViewInsets](automaticallyadjustsscrollviewinsets.md) — A Boolean value that indicates whether the view controller should automatically adjust its scroll view insets. _(deprecated)_
- [bottomLayoutGuide](bottomlayoutguide.md) — Indicates the lowest vertical extent for your onscreen content, for use with Auto Layout constraints. _(deprecated)_
- [interfaceOrientation](interfaceorientation.md) — Convenience property that provides the current orientation of the interface, meaningful only if the view controller is taking up the full screen. _(deprecated)_
- [modalInPopover](ismodalinpopover.md) — A Boolean value indicating whether the view controller should be presented modally by a popover. _(deprecated)_
- [modalViewController](modalviewcontroller.md) — The controller for the active presented view’that is, the view that is temporarily displayed on top of the view managed by the receiver. _(deprecated)_
- [searchDisplayController](searchdisplaycontroller.md) — The search display controller associated with the view controller. _(deprecated)_
- [topLayoutGuide](toplayoutguide.md) — Indicates the highest vertical extent for your onscreen content, for use with Auto Layout constraints. _(deprecated)_
- [wantsFullScreenLayout](wantsfullscreenlayout.md) — A Boolean value indicating whether the view should underlap the status bar. _(deprecated)_
