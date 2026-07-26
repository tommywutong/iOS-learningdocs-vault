---
title: 'dismissModalViewControllerAnimated:'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+（6.0 起废弃）, iPadOS 2.0+（6.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: '/documentation/uikit/uiviewcontroller/dismissmodalviewcontrolleranimated:'
source_url: 'https://developer.apple.com/documentation/uikit/uiviewcontroller/dismissmodalviewcontrolleranimated:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiviewcontroller/dismissmodalviewcontrolleranimated%3A.json'
content_hash: 'sha256:f8cdae75ae0e7365'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIViewController](../uiviewcontroller.md)

# dismissModalViewControllerAnimated:

<sub>Instance Method</sub>

Dismisses the view controller that was presented by the receiver.

> [!warning] Deprecated
> Use [- dismissViewControllerAnimated:completion:](<dismiss(animated_completion_).md>) instead.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
- (void) dismissModalViewControllerAnimated:(BOOL) animated;
```

## Parameters

- `animated` — If [true](../../swift/true.md), this method animates the view as it’s dismissed; otherwise, it does not. The style of animation is determined by the value in the [modalTransitionStyle](modaltransitionstyle.md) property of the view controller being dismissed.

## Discussion

The presenting view controller is responsible for dismissing the view controller it presented. If you call this method on the presented view controller itself, however, it automatically forwards the message to the presenting view controller.

If you present several view controllers in succession, and thus build a stack of presented view controllers, calling this method on a view controller lower in the stack dismisses its immediate child view controller and all view controllers above that child on the stack. When this happens, only the top-most view is dismissed in an animated fashion; any intermediate view controllers are simply removed from the stack. The top-most view is dismissed using its modal transition style, which may differ from the styles used by other view controllers lower in the stack.

If you want to retain a reference to the receiver’s presented view controller, get the value in the [modalViewController](modalviewcontroller.md) property before calling this method.

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
- [- dismissMoviePlayerViewControllerAnimated](<dismissmovieplayerviewcontrolleranimated().md>) — Dismisses a movie player view controller using the standard movie player transition. _(deprecated)_
- [- viewControllerForUnwindSegueAction:fromViewController:withSender:](<forunwindsegueaction(__from_withsender_).md>) — Called when an unwind segue action wants to search a container’s children for a view controller to handle the unwind action. _(deprecated)_
- [presentModalViewController:animated:](presentmodalviewcontroller_animated_.md) — Presents a modal view managed by the given view controller to the user. _(deprecated)_
- [- presentMoviePlayerViewControllerAnimated:](<presentmovieplayerviewcontrolleranimated(__).md>) — Presents the movie player view controller using the standard movie player transition. _(deprecated)_
- [- rotatingFooterView](<rotatingfooterview().md>) — Returns the footer view to transition during an interface orientation change. _(deprecated)_
- [- rotatingHeaderView](<rotatingheaderview().md>) — Returns the header view to transition during an interface orientation change. _(deprecated)_
