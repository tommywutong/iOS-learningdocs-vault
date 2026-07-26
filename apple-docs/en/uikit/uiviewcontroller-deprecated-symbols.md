---
title: Deprecated symbols
framework: UIKit
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiviewcontroller-deprecated-symbols
source_url: 'https://developer.apple.com/documentation/uikit/uiviewcontroller-deprecated-symbols'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiviewcontroller-deprecated-symbols.json'
content_hash: 'sha256:4390c7324fa2ec0a'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md) · [View controllers](view-controllers.md) · [UIViewController](uiviewcontroller.md)

# Deprecated symbols

<sub>API Collection</sub>

Symbols that view controllers no longer support.

## Topics

### Deprecated methods

- [- setOverrideTraitCollection:forChildViewController:](<uiviewcontroller/setoverridetraitcollection(__forchild_).md>) — Changes the traits assigned to the specified child view controller. _(deprecated)_
- [- overrideTraitCollectionForChildViewController:](<uiviewcontroller/overridetraitcollection(forchild_).md>) — Retrieves the trait collection for a child view controller. _(deprecated)_
- [+ attemptRotationToDeviceOrientation](<uiviewcontroller/attemptrotationtodeviceorientation().md>) — Attempts to rotate all windows to the orientation of the device. _(deprecated)_
- [- registerForPreviewingWithDelegate:sourceView:](<uiviewcontroller/registerforpreviewing(with_sourceview_).md>) — Registers a view controller to participate with 3D Touch preview (peek) and commit (pop). _(deprecated)_
- [- unregisterForPreviewingWithContext:](<uiviewcontroller/unregisterforpreviewing(withcontext_).md>) — Unregisters a previously registered view controller identified by its context object. _(deprecated)_
- [- canPerformUnwindSegueAction:fromViewController:withSender:](<uiviewcontroller/canperformunwindsegueaction(__from_withsender_).md>) — Called on a view controller to determine whether it wants to respond to an unwind action. _(deprecated)_
- [- didRotateFromInterfaceOrientation:](<uiviewcontroller/didrotate(from_).md>) — Sent to the view controller after the user interface rotates. _(deprecated)_
- [- dismissMoviePlayerViewControllerAnimated](<uiviewcontroller/dismissmovieplayerviewcontrolleranimated().md>) — Dismisses a movie player view controller using the standard movie player transition. _(deprecated)_
- [- viewControllerForUnwindSegueAction:fromViewController:withSender:](<uiviewcontroller/forunwindsegueaction(__from_withsender_).md>) — Called when an unwind segue action wants to search a container’s children for a view controller to handle the unwind action. _(deprecated)_
- [- presentMoviePlayerViewControllerAnimated:](<uiviewcontroller/presentmovieplayerviewcontrolleranimated(__).md>) — Presents the movie player view controller using the standard movie player transition. _(deprecated)_
- [- rotatingFooterView](<uiviewcontroller/rotatingfooterview().md>) — Returns the footer view to transition during an interface orientation change. _(deprecated)_
- [- rotatingHeaderView](<uiviewcontroller/rotatingheaderview().md>) — Returns the header view to transition during an interface orientation change. _(deprecated)_
- [- segueForUnwindingToViewController:fromViewController:identifier:](<uiviewcontroller/segueforunwinding(to_from_identifier_).md>) — Called when an unwind segue action needs to transition between two view controllers. _(deprecated)_
- [- shouldAutomaticallyForwardRotationMethods](<uiviewcontroller/shouldautomaticallyforwardrotationmethods().md>) — Returns a Boolean value indicating whether rotation methods are forwarded to child view controllers. _(deprecated)_
- [- willAnimateRotationToInterfaceOrientation:duration:](<uiviewcontroller/willanimaterotation(to_duration_).md>) — Sent to the view controller before performing a one-step user interface rotation. _(deprecated)_
- [- willRotateToInterfaceOrientation:duration:](<uiviewcontroller/willrotate(to_duration_).md>) — Sent to the view controller just before the user interface begins rotating. _(deprecated)_

### Deprecated properties

- [shouldAutorotate](uiviewcontroller/shouldautorotate.md) — A Boolean value that indicates whether the view controller’s contents should autorotate. _(deprecated)_
- [previewActionItems](uiviewcontroller/previewactionitems.md) — The quick actions displayed when a user swipes upward on a 3D Touch preview. _(deprecated)_
- [automaticallyAdjustsScrollViewInsets](uiviewcontroller/automaticallyadjustsscrollviewinsets.md) — A Boolean value that indicates whether the view controller should automatically adjust its scroll view insets. _(deprecated)_
- [bottomLayoutGuide](uiviewcontroller/bottomlayoutguide.md) — Indicates the lowest vertical extent for your onscreen content, for use with Auto Layout constraints. _(deprecated)_
- [interfaceOrientation](uiviewcontroller/interfaceorientation.md) — Convenience property that provides the current orientation of the interface, meaningful only if the view controller is taking up the full screen. _(deprecated)_
- [modalInPopover](uiviewcontroller/ismodalinpopover.md) — A Boolean value indicating whether the view controller should be presented modally by a popover. _(deprecated)_
- [searchDisplayController](uiviewcontroller/searchdisplaycontroller.md) — The search display controller associated with the view controller. _(deprecated)_
- [topLayoutGuide](uiviewcontroller/toplayoutguide.md) — Indicates the highest vertical extent for your onscreen content, for use with Auto Layout constraints. _(deprecated)_
