---
title: automaticallyForwardAppearanceAndRotationMethodsToChildViewControllers
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 5.0+（6.0 起废弃）, iPadOS 5.0+（6.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: /documentation/uikit/uiviewcontroller/automaticallyforwardappearanceandrotationmethodstochildviewcontrollers
source_url: 'https://developer.apple.com/documentation/uikit/uiviewcontroller/automaticallyforwardappearanceandrotationmethodstochildviewcontrollers'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiviewcontroller/automaticallyforwardappearanceandrotationmethodstochildviewcontrollers.json'
content_hash: 'sha256:e399593a079afcbd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIViewController](../uiviewcontroller.md)

# automaticallyForwardAppearanceAndRotationMethodsToChildViewControllers

<sub>Instance Method</sub>

Returns a Boolean value that indicates whether appearance and rotation methods are forwarded.

> [!warning] Deprecated
> Manually forward calls to the [- viewWillTransitionToSize:withTransitionCoordinator:](<../uicontentcontainer/viewwilltransition(to_with_).md>) method as needed.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
- (BOOL) automaticallyForwardAppearanceAndRotationMethodsToChildViewControllers;
```

## Return Value

A Boolean value that indicates whether appearance and rotation methods are forwarded.

## Discussion

This method is called to determine whether to automatically forward containment callbacks to the child view controllers.

The default implementation returns [true](../../swift/true.md). Subclasses of the [UIViewController](../uiviewcontroller.md) class that implement containment logic may override this method to control how these methods are forwarded. If you override this method and return [false](../../swift/false.md), you are responsible for forwarding the following methods to child view controllers at the appropriate times:

- [- viewWillAppear:](<viewwillappear(__).md>)
- [- viewDidAppear:](<viewdidappear(__).md>)
- [- viewWillDisappear:](<viewwilldisappear(__).md>)
- [- viewDidDisappear:](<viewdiddisappear(__).md>)
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
- [didAnimateFirstHalfOfRotationToInterfaceOrientation:](didanimatefirsthalfofrotationtointerfaceorientation_.md) — Sent to the view controller after the completion of the first half of the user interface rotation. _(deprecated)_
- [- didRotateFromInterfaceOrientation:](<didrotate(from_).md>) — Sent to the view controller after the user interface rotates. _(deprecated)_
- [dismissModalViewControllerAnimated:](dismissmodalviewcontrolleranimated_.md) — Dismisses the view controller that was presented by the receiver. _(deprecated)_
- [- dismissMoviePlayerViewControllerAnimated](<dismissmovieplayerviewcontrolleranimated().md>) — Dismisses a movie player view controller using the standard movie player transition. _(deprecated)_
- [- viewControllerForUnwindSegueAction:fromViewController:withSender:](<forunwindsegueaction(__from_withsender_).md>) — Called when an unwind segue action wants to search a container’s children for a view controller to handle the unwind action. _(deprecated)_
- [presentModalViewController:animated:](presentmodalviewcontroller_animated_.md) — Presents a modal view managed by the given view controller to the user. _(deprecated)_
- [- presentMoviePlayerViewControllerAnimated:](<presentmovieplayerviewcontrolleranimated(__).md>) — Presents the movie player view controller using the standard movie player transition. _(deprecated)_
- [- rotatingFooterView](<rotatingfooterview().md>) — Returns the footer view to transition during an interface orientation change. _(deprecated)_
- [- rotatingHeaderView](<rotatingheaderview().md>) — Returns the header view to transition during an interface orientation change. _(deprecated)_
