---
title: 'presentModalViewController:animated:'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+（6.0 起废弃）, iPadOS 2.0+（6.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: '/documentation/uikit/uiviewcontroller/presentmodalviewcontroller:animated:'
source_url: 'https://developer.apple.com/documentation/uikit/uiviewcontroller/presentmodalviewcontroller:animated:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiviewcontroller/presentmodalviewcontroller%3Aanimated%3A.json'
content_hash: 'sha256:456ca39b27df420c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIViewController](../uiviewcontroller.md)

# presentModalViewController:animated:

<sub>Instance Method</sub>

Presents a modal view managed by the given view controller to the user.

> [!warning] Deprecated
> Use [- presentViewController:animated:completion:](<present(__animated_completion_).md>) instead.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
- (void) presentModalViewController:(UIViewController *) modalViewController animated:(BOOL) animated;
```

## Parameters

- `modalViewController` — The view controller that manages the modal view.

- `animated` — If [true](../../swift/true.md), animates the view as it’s presented; otherwise, does not.

## Discussion

On iPhone and iPod touch devices, the view of `modalViewController` is always presented full screen. On iPad, the presentation depends on the value in the [modalPresentationStyle](modalpresentationstyle.md) property.

Sets the [modalViewController](modalviewcontroller.md) property to the specified view controller. Resizes its view and attaches it to the view hierarchy. The view is animated according to the transition style specified in the [modalTransitionStyle](modaltransitionstyle.md) property of the controller in the `modalViewController` parameter.

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
- [- presentMoviePlayerViewControllerAnimated:](<presentmovieplayerviewcontrolleranimated(__).md>) — Presents the movie player view controller using the standard movie player transition. _(deprecated)_
- [- rotatingFooterView](<rotatingfooterview().md>) — Returns the footer view to transition during an interface orientation change. _(deprecated)_
- [- rotatingHeaderView](<rotatingheaderview().md>) — Returns the header view to transition during an interface orientation change. _(deprecated)_
