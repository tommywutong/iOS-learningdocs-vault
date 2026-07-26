---
title: 'setOverrideTraitCollection(_:forChild:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+（17.0 起废弃）, iPadOS 8.0+（17.0 起废弃）, Mac Catalyst 13.1+（17.0 起废弃）, tvOS（17.0 起废弃）, visionOS 1.0+（1.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/uikit/uiviewcontroller/setoverridetraitcollection(_:forchild:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiviewcontroller/setoverridetraitcollection(_:forchild:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiviewcontroller/setoverridetraitcollection%28_%3Aforchild%3A%29.json'
content_hash: 'sha256:f410db28daf42c81'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIViewController](../uiviewcontroller.md)

# setOverrideTraitCollection(_:forChild:)

<sub>Instance Method</sub>

Changes the traits assigned to the specified child view controller.

> [!warning] Deprecated
> Use [traitOverrides](traitoverrides-1z1cc.md) instead.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func setOverrideTraitCollection(_ collection: UITraitCollection?, forChild childViewController: UIViewController)
```

## Parameters

- `collection` — The new traits to apply to the child view controller.

- `childViewController` — The child view controller whose trait collection is to be changed.

## Discussion

Usually, traits are passed unmodified from the parent view controller to its child view controllers. When implementing a custom container view controller, you can use this method to change the traits of any embedded child view controllers to something more appropriate for your layout. Making such a change alters other view controller behaviors associated with that child. For example, modal presentations behave differently in a horizontally compact versus horizontally regular environment. You might also make such a change to force the same set of traits on the child view controller regardless of the actual trait environment.

## See Also

### Deprecated methods

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
- [- shouldAutomaticallyForwardRotationMethods](<shouldautomaticallyforwardrotationmethods().md>) — Returns a Boolean value indicating whether rotation methods are forwarded to child view controllers. _(deprecated)_
- [- willAnimateRotationToInterfaceOrientation:duration:](<willanimaterotation(to_duration_).md>) — Sent to the view controller before performing a one-step user interface rotation. _(deprecated)_
- [- willRotateToInterfaceOrientation:duration:](<willrotate(to_duration_).md>) — Sent to the view controller just before the user interface begins rotating. _(deprecated)_
