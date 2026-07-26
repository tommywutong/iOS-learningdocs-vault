---
title: 'overrideTraitCollection(forChild:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+（17.0 起废弃）, iPadOS 8.0+（17.0 起废弃）, Mac Catalyst 13.1+（17.0 起废弃）, tvOS（17.0 起废弃）, visionOS 1.0+（1.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/uikit/uiviewcontroller/overridetraitcollection(forchild:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiviewcontroller/overridetraitcollection(forchild:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiviewcontroller/overridetraitcollection%28forchild%3A%29.json'
content_hash: 'sha256:f778e1e42777b8cf'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIViewController](../uiviewcontroller.md)

# overrideTraitCollection(forChild:)

<sub>Instance Method</sub>

Retrieves the trait collection for a child view controller.

> [!warning] Deprecated
> Use [traitOverrides](traitoverrides-1z1cc.md) instead.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func overrideTraitCollection(forChild childViewController: UIViewController) -> UITraitCollection?
```

## Parameters

- `childViewController` — The view controller who’s trait collection is to be returned.

## Return Value

The trait collection for the designated view controller.

## Discussion

Use this method to retrieve the trait collection for a child view controller. You can then modify the trait collection for the designated child view controller and set it using the [- setOverrideTraitCollection:forChildViewController:](<setoverridetraitcollection(__forchild_).md>) method.

## See Also

### Deprecated methods

- [- setOverrideTraitCollection:forChildViewController:](<setoverridetraitcollection(__forchild_).md>) — Changes the traits assigned to the specified child view controller. _(deprecated)_
- [+ attemptRotationToDeviceOrientation](<attemptrotationtodeviceorientation().md>) — Attempts to rotate all windows to the orientation of the device. _(deprecated)_
- [- registerForPreviewingWithDelegate:sourceView:](<registerforpreviewing(with_sourceview_).md>) — Registers a view controller to participate with 3D Touch preview (peek) and commit (pop). _(deprecated)_
- [- unregisterForPreviewingWithContext:](<unregisterforpreviewing(withcontext_).md>) — Unregisters a previously registered view controller identified by its context object. _(deprecated)_
- [- canPerformUnwindSegueAction:fromViewController:withSender:](<canperformunwindsegueaction(__from_withsender_).md>) — Called on a view controller to determine whether it wants to respond to an unwind action. _(deprecated)_
- [- didRotateFromInterfaceOrientation:](<didrotate(from_).md>) — Sent to the view controller after the user interface rotates. _(deprecated)_
- [- dismissMoviePlayerViewControllerAnimated](<dismissmovieplayerviewcontrolleranimated().md>) — Dismisses a movie player view controller using the standard movie player transition. _(deprecated)_
- [- viewControllerForUnwindSegueAction:fromViewController:withSender:](<forunwindsegueaction(__from_withsender_).md>) — Called when an unwind segue action wants to search a container’s children for a view controller to handle the unwind action. _(deprecated)_
- [- presentMoviePlayerViewControllerAnimated:](<presentmovieplayerviewcontrolleranimated(__).md>) — Presents the movie player view controller using the standard movie player transition. _(deprecated)_
- [- rotatingFooterView](<rotatingfooterview().md>) — Returns the footer view to transition during an interface orientation change. _(deprecated)_
- [- rotatingHeaderView](<rotatingheaderview().md>) — Returns the header view to transition during an interface orientation change. _(deprecated)_
- [- segueForUnwindingToViewController:fromViewController:identifier:](<segueforunwinding(to_from_identifier_).md>) — Called when an unwind segue action needs to transition between two view controllers. _(deprecated)_
- [- shouldAutomaticallyForwardRotationMethods](<shouldautomaticallyforwardrotationmethods().md>) — Returns a Boolean value indicating whether rotation methods are forwarded to child view controllers. _(deprecated)_
- [- willAnimateRotationToInterfaceOrientation:duration:](<willanimaterotation(to_duration_).md>) — Sent to the view controller before performing a one-step user interface rotation. _(deprecated)_
- [- willRotateToInterfaceOrientation:duration:](<willrotate(to_duration_).md>) — Sent to the view controller just before the user interface begins rotating. _(deprecated)_
