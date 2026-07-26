---
title: shouldAutomaticallyForwardRotationMethods()
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 6.0+（8.0 起废弃）, iPadOS 6.0+（8.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/uikit/uiviewcontroller/shouldautomaticallyforwardrotationmethods()
source_url: 'https://developer.apple.com/documentation/uikit/uiviewcontroller/shouldautomaticallyforwardrotationmethods()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiviewcontroller/shouldautomaticallyforwardrotationmethods%28%29.json'
content_hash: 'sha256:244f8c3ddeca6827'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIViewController](../uiviewcontroller.md)

# shouldAutomaticallyForwardRotationMethods()

<sub>Instance Method</sub>

Returns a Boolean value indicating whether rotation methods are forwarded to child view controllers.

> [!warning] Deprecated
> Manually forward calls to the [- viewWillTransitionToSize:withTransitionCoordinator:](<../uicontentcontainer/viewwilltransition(to_with_).md>) method as needed.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
func shouldAutomaticallyForwardRotationMethods() -> Bool
```

## Return Value

[true](../../swift/true.md) if rotation methods are forwarded or [false](../../swift/false.md) if they are not.

## Discussion

This method is called to determine whether to automatically forward rotation-related containment callbacks to child view controllers.

The default implementation returns [true](../../swift/true.md). Subclasses of the [UIViewController](../uiviewcontroller.md) class that implement containment logic may override this method to control how these methods are forwarded. If you override this method and return [false](../../swift/false.md), you are responsible for forwarding the following methods to child view controllers at the appropriate times:

- [- willRotateToInterfaceOrientation:duration:](<willrotate(to_duration_).md>)
- [- willAnimateRotationToInterfaceOrientation:duration:](<willanimaterotation(to_duration_).md>)
- [- didRotateFromInterfaceOrientation:](<didrotate(from_).md>)

## See Also

### Deprecated methods

- [- setOverrideTraitCollection:forChildViewController:](<setoverridetraitcollection(__forchild_).md>) — Changes the traits assigned to the specified child view controller. _(deprecated)_
- [- overrideTraitCollectionForChildViewController:](<overridetraitcollection(forchild_).md>) — Retrieves the trait collection for a child view controller. _(deprecated)_
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
- [- willAnimateRotationToInterfaceOrientation:duration:](<willanimaterotation(to_duration_).md>) — Sent to the view controller before performing a one-step user interface rotation. _(deprecated)_
- [- willRotateToInterfaceOrientation:duration:](<willrotate(to_duration_).md>) — Sent to the view controller just before the user interface begins rotating. _(deprecated)_
