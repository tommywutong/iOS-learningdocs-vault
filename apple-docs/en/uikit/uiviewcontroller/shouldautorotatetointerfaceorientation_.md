---
title: 'shouldAutorotateToInterfaceOrientation:'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+（6.0 起废弃）, iPadOS 2.0+（6.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: '/documentation/uikit/uiviewcontroller/shouldautorotatetointerfaceorientation:'
source_url: 'https://developer.apple.com/documentation/uikit/uiviewcontroller/shouldautorotatetointerfaceorientation:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiviewcontroller/shouldautorotatetointerfaceorientation%3A.json'
content_hash: 'sha256:e73fd112fd094591'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIViewController](../uiviewcontroller.md)

# shouldAutorotateToInterfaceOrientation:

<sub>Instance Method</sub>

Returns a Boolean value indicating whether the view controller supports the specified orientation.

> [!warning] Deprecated
> Override the [supportedInterfaceOrientations](supportedinterfaceorientations.md) and [preferredInterfaceOrientationForPresentation](preferredinterfaceorientationforpresentation.md) methods instead.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
- (BOOL) shouldAutorotateToInterfaceOrientation:(UIInterfaceOrientation) toInterfaceOrientation;
```

## Parameters

- `toInterfaceOrientation` — The orientation of the app’s user interface after the rotation. The possible values are described in [UIInterfaceOrientation](../uiinterfaceorientation.md).

## Return Value

[true](../../swift/true.md) if the view controller auto-rotates its view to the specified orientation; otherwise, [false](../../swift/false.md).

## Discussion

By default, this method returns [true](../../swift/true.md) for the [UIInterfaceOrientationPortrait](../uiinterfaceorientation/portrait.md) orientation only. If your view controller supports additional orientations, override this method and return [true](../../swift/true.md) for all orientations it supports.

Your implementation of this method should simply return [true](../../swift/true.md) or [false](../../swift/false.md) based on the value in the `interfaceOrientation` parameter. Do not attempt to get the value of the [interfaceOrientation](interfaceorientation.md) property or check the orientation value reported by the [UIDevice](../uidevice.md) class. Your view controller is either capable of supporting a given orientation or it is not.

## See Also

### Deprecated methods

- [- setOverrideTraitCollection:forChildViewController:](<setoverridetraitcollection(__forchild_).md>) — Changes the traits assigned to the specified child view controller. _(deprecated)_
- [- overrideTraitCollectionForChildViewController:](<overridetraitcollection(forchild_).md>) — Retrieves the trait collection for a child view controller. _(deprecated)_
- [+ attemptRotationToDeviceOrientation](<attemptrotationtodeviceorientation().md>) — Attempts to rotate all windows to the orientation of the device. _(deprecated)_
- [- registerForPreviewingWithDelegate:sourceView:](<registerforpreviewing(with_sourceview_).md>) — Registers a view controller to participate with 3D Touch preview (peek) and commit (pop). _(deprecated)_
- [- unregisterForPreviewingWithContext:](<unregisterforpreviewing(withcontext_).md>) — Unregisters a previously registered view controller identified by its context object. _(deprecated)_
- [automaticallyForwardAppearanceAndRotationMethodsToChildViewControllers](automaticallyforwardappearanceandrotationmethodstochildviewcontrollers.md) — Returns a Boolean value that indicates whether appearance and rotation methods are forwarded. _(deprecated)_
- [- canPerformUnwindSegueAction:fromViewController:withSender:](<canperformunwindsegueaction(__from_withsender_).md>) — Called on a view controller to determine whether it wants to respond to an unwind action. _(deprecated)_
- [didAnimateFirstHalfOfRotationToInterfaceOrientation:](didanimatefirsthalfofrotationtointerfaceorientation_.md) — Sent to the view controller after the completion of the first half of the user interface rotation. _(deprecated)_
- [- didRotateFromInterfaceOrientation:](<didrotate(from_).md>) — Sent to the view controller after the user interface rotates. _(deprecated)_
- [dismissModalViewControllerAnimated:](dismissmodalviewcontrolleranimated_.md) — Dismisses the view controller that was presented by the receiver. _(deprecated)_
- [- dismissMoviePlayerViewControllerAnimated](<dismissmovieplayerviewcontrolleranimated().md>) — Dismisses a movie player view controller using the standard movie player transition. _(deprecated)_
- [- viewControllerForUnwindSegueAction:fromViewController:withSender:](<forunwindsegueaction(__from_withsender_).md>) — Called when an unwind segue action wants to search a container’s children for a view controller to handle the unwind action. _(deprecated)_
- [presentModalViewController:animated:](presentmodalviewcontroller_animated_.md) — Presents a modal view managed by the given view controller to the user. _(deprecated)_
- [- presentMoviePlayerViewControllerAnimated:](<presentmovieplayerviewcontrolleranimated(__).md>) — Presents the movie player view controller using the standard movie player transition. _(deprecated)_
- [- rotatingFooterView](<rotatingfooterview().md>) — Returns the footer view to transition during an interface orientation change. _(deprecated)_
