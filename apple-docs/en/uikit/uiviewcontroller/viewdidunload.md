---
title: viewDidUnload
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 3.0+（6.0 起废弃）, iPadOS 3.0+（6.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: /documentation/uikit/uiviewcontroller/viewdidunload
source_url: 'https://developer.apple.com/documentation/uikit/uiviewcontroller/viewdidunload'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiviewcontroller/viewdidunload.json'
content_hash: 'sha256:d40ed8729ea41344'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIViewController](../uiviewcontroller.md)

# viewDidUnload

<sub>Instance Method</sub>

Called when the controller’s view is released from memory.

> [!warning] Deprecated
> Views are no longer purged under low-memory conditions and so this method is never called.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
- (void) viewDidUnload;
```

## Discussion

In iOS 5 and earlier, when a low-memory condition occurred and the current view controller’s views were not needed, the system could opt to call this method after the view controller’s view had been released. This method was your chance to perform any final cleanup. If your view controller stored separate references to the view or its subviews, you could use this method to release those references. You could also use this method to remove references to any objects that you created to support the view but that are no longer needed now that the view is gone. You would not use this method to release user data or any other information that cannot be easily recreated.

In iOS 6 and later, clearing references to views and other objects in your view controller is unnecessary.

At the time this method is called, the [view](view.md) property is `nil`.

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
