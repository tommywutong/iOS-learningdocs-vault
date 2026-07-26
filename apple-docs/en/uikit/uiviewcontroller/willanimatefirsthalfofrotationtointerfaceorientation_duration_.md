---
title: 'willAnimateFirstHalfOfRotationToInterfaceOrientation:duration:'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+（5.0 起废弃）, iPadOS 2.0+（5.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: '/documentation/uikit/uiviewcontroller/willanimatefirsthalfofrotationtointerfaceorientation:duration:'
source_url: 'https://developer.apple.com/documentation/uikit/uiviewcontroller/willanimatefirsthalfofrotationtointerfaceorientation:duration:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiviewcontroller/willanimatefirsthalfofrotationtointerfaceorientation%3Aduration%3A.json'
content_hash: 'sha256:acaa5da466d456f6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIViewController](../uiviewcontroller.md)

# willAnimateFirstHalfOfRotationToInterfaceOrientation:duration:

<sub>Instance Method</sub>

Sent to the view controller before performing the first half of a user interface rotation.

> [!warning] Deprecated
> Use [- viewWillTransitionToSize:withTransitionCoordinator:](<../uicontentcontainer/viewwilltransition(to_with_).md>) to make interface-based adjustments.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
- (void) willAnimateFirstHalfOfRotationToInterfaceOrientation:(UIInterfaceOrientation) toInterfaceOrientation duration:(NSTimeInterval) duration;
```

## Parameters

- `toInterfaceOrientation` — The state of the app’s user interface orientation before the rotation. The possible values are described in [UIInterfaceOrientation](../uiinterfaceorientation.md).

- `duration` — The duration of the first half of the pending rotation, measured in seconds.

## Discussion

The default implementation of this method does nothing.

This method is called from within the animation block used to rotate the view and slide the header and footer views out. You can override this method and use it to configure additional animations that should occur during the first half of the view rotation. For example, you could use it to adjust the zoom level of your content, change the scroller position, or modify other animatable properties of your view.

At the time this method is called, the [interfaceOrientation](interfaceorientation.md) property is still set to the old orientation.

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
