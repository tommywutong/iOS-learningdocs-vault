---
title: wantsFullScreenLayout
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 3.0+（7.0 起废弃）, iPadOS 3.0+（7.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: /documentation/uikit/uiviewcontroller/wantsfullscreenlayout
source_url: 'https://developer.apple.com/documentation/uikit/uiviewcontroller/wantsfullscreenlayout'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiviewcontroller/wantsfullscreenlayout.json'
content_hash: 'sha256:0d12400bfc745d57'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIViewController](../uiviewcontroller.md)

# wantsFullScreenLayout

<sub>Instance Property</sub>

A Boolean value indicating whether the view should underlap the status bar.

> [!warning] Deprecated
> Use [edgesForExtendedLayout](edgesforextendedlayout.md) and [extendedLayoutIncludesOpaqueBars](extendedlayoutincludesopaquebars.md) instead.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
@property (nonatomic, assign) BOOL wantsFullScreenLayout;
```

## Discussion

When a view controller presents its view, it normally shrinks that view so that its frame does not overlap the device’s status bar. Setting this property to [true](../../swift/true.md) causes the view controller to size its view so that it fills the entire screen, including the area under the status bar. (Of course, for this to happen, the window hosting the view controller must itself be sized to fill the entire screen, including the area underneath the status bar.) You would typically set this property to [true](../../swift/true.md) in cases where you have a translucent status bar and want your view’s content to be visible behind that view.

If this property is [true](../../swift/true.md), the view is not resized in a way that would cause it to underlap a tab bar but is resized to underlap translucent toolbars. Regardless of the value of this property, navigation controllers always allow views to underlap translucent navigation bars.

The default value of this property is [false](../../swift/false.md), which causes the view to be laid out so it does not underlap the status bar.

## See Also

### Deprecated properties

- [shouldAutorotate](shouldautorotate.md) — A Boolean value that indicates whether the view controller’s contents should autorotate. _(deprecated)_
- [previewActionItems](previewactionitems.md) — The quick actions displayed when a user swipes upward on a 3D Touch preview. _(deprecated)_
- [automaticallyAdjustsScrollViewInsets](automaticallyadjustsscrollviewinsets.md) — A Boolean value that indicates whether the view controller should automatically adjust its scroll view insets. _(deprecated)_
- [bottomLayoutGuide](bottomlayoutguide.md) — Indicates the lowest vertical extent for your onscreen content, for use with Auto Layout constraints. _(deprecated)_
- [contentSizeForViewInPopover](contentsizeforviewinpopover.md) — The size of the view controller’s view while displayed in a popover. _(deprecated)_
- [interfaceOrientation](interfaceorientation.md) — Convenience property that provides the current orientation of the interface, meaningful only if the view controller is taking up the full screen. _(deprecated)_
- [modalInPopover](ismodalinpopover.md) — A Boolean value indicating whether the view controller should be presented modally by a popover. _(deprecated)_
- [modalViewController](modalviewcontroller.md) — The controller for the active presented view’that is, the view that is temporarily displayed on top of the view managed by the receiver. _(deprecated)_
- [searchDisplayController](searchdisplaycontroller.md) — The search display controller associated with the view controller. _(deprecated)_
- [topLayoutGuide](toplayoutguide.md) — Indicates the highest vertical extent for your onscreen content, for use with Auto Layout constraints. _(deprecated)_
