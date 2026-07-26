---
title: 'forUnwindSegueAction(_:from:withSender:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 6.0+（9.0 起废弃）, iPadOS 6.0+（9.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）, tvOS（9.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/uikit/uiviewcontroller/forunwindsegueaction(_:from:withsender:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiviewcontroller/forunwindsegueaction(_:from:withsender:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiviewcontroller/forunwindsegueaction%28_%3Afrom%3Awithsender%3A%29.json'
content_hash: 'sha256:00d77343dfe50639'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIViewController](../uiviewcontroller.md)

# forUnwindSegueAction(_:from:withSender:)

<sub>Instance Method</sub>

Called when an unwind segue action wants to search a container’s children for a view controller to handle the unwind action.

> [!warning] Deprecated
> Override the [- allowedChildViewControllersForUnwindingFromSource:](<allowedchildrenforunwinding(from_).md>) method instead.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
func forUnwindSegueAction(_ action: Selector, from fromViewController: UIViewController, withSender sender: Any?) -> UIViewController?
```

## Parameters

- `action` — The action that triggered the unwind action.

- `fromViewController` — The view controller that is the source of the unwinding action.

- `sender` — The object that initiated the action.

## Return Value

The view controller that wants to handle the unwind action.

## Discussion

A custom container view controller should override this method and use it to search its children for a view controller to handle the unwind action. It does this by invoking the [- canPerformUnwindSegueAction:fromViewController:withSender:](<canperformunwindsegueaction(__from_withsender_).md>) method on each child. If a view controller wants to handle the action, your method should return it. If none of the container’s children want to handle the unwind action, invoke the super’s implementation and return the result of that method.

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
- [- presentMoviePlayerViewControllerAnimated:](<presentmovieplayerviewcontrolleranimated(__).md>) — Presents the movie player view controller using the standard movie player transition. _(deprecated)_
- [- rotatingFooterView](<rotatingfooterview().md>) — Returns the footer view to transition during an interface orientation change. _(deprecated)_
- [- rotatingHeaderView](<rotatingheaderview().md>) — Returns the header view to transition during an interface orientation change. _(deprecated)_
- [- segueForUnwindingToViewController:fromViewController:identifier:](<segueforunwinding(to_from_identifier_).md>) — Called when an unwind segue action needs to transition between two view controllers. _(deprecated)_
- [- shouldAutomaticallyForwardRotationMethods](<shouldautomaticallyforwardrotationmethods().md>) — Returns a Boolean value indicating whether rotation methods are forwarded to child view controllers. _(deprecated)_
- [- willAnimateRotationToInterfaceOrientation:duration:](<willanimaterotation(to_duration_).md>) — Sent to the view controller before performing a one-step user interface rotation. _(deprecated)_
- [- willRotateToInterfaceOrientation:duration:](<willrotate(to_duration_).md>) — Sent to the view controller just before the user interface begins rotating. _(deprecated)_
