---
title: 'registerForPreviewing(with:sourceView:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 9.0+（13.0 起废弃）, iPadOS 9.0+（13.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）, tvOS 9.0+（13.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/uikit/uiviewcontroller/registerforpreviewing(with:sourceview:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiviewcontroller/registerforpreviewing(with:sourceview:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiviewcontroller/registerforpreviewing%28with%3Asourceview%3A%29.json'
content_hash: 'sha256:9c6ebbf209c9fb4d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIViewController](../uiviewcontroller.md)

# registerForPreviewing(with:sourceView:)

<sub>Instance Method</sub>

Registers a view controller to participate with 3D Touch preview (peek) and commit (pop).

> [!warning] Deprecated
> Use [UIContextMenuInteraction](../uicontextmenuinteraction.md) instead.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
func registerForPreviewing(with delegate: any UIViewControllerPreviewingDelegate, sourceView: UIView) -> any UIViewControllerPreviewing
```

## Parameters

- `delegate` — The delegate object mediates the presentation of views from the preview (peek) view controller and the commit (pop) view controller. In practice, these two are typically the same view controller. The delegate performs this mediation through your implementation of the methods of the [UIViewControllerPreviewingDelegate](../uiviewcontrollerpreviewingdelegate.md) protocol.

- `sourceView` — The view, in the view hierarchy of the receiver of this method call, that invokes a preview when pressed by the user. When lightly pressed, the source view remains visually sharp while surrounding content blurs. When pressed more deeply, the system calls the [- previewingContext:viewControllerForLocation:](<../uiviewcontrollerpreviewingdelegate/previewingcontext(__viewcontrollerforlocation_).md>) method in your `delegate` object, which presents the preview (peek) view from another view controller.

## Return Value

A context object for managing the preview. This object conforms to the [UIViewControllerPreviewing](../uiviewcontrollerpreviewing.md) protocol.

## Discussion

A preview, or _peek_ in end-user terminology, provides additional content related to the view the user pressed (that is, related to the `sourceView` view).

Calling this method does three things:

- Registers the previewing view controller (the one that receives this method call) to participate with 3D Touch preview and commit
- Designates the source view, from the receiver’s view hierarchy, as the view to respond to a forceful touch
- Designates a delegate object for mediating the presentation of the preview (peek) and commit (pop) views as a user requests them in turn by pressing more deeply

You can designate more than one source view for a single registered view controller, but you cannot designate a single view as a source view more than once.

The lifetime of this method’s returned context object is managed by the system. If you need to explicitly unregister a view controller, pass its context object to the [- unregisterForPreviewingWithContext:](<unregisterforpreviewing(withcontext_).md>) method. If you do not unregister a view controller, the system automatically unregisters it when the view controller is deallocated.

## See Also

### Deprecated methods

- [- setOverrideTraitCollection:forChildViewController:](<setoverridetraitcollection(__forchild_).md>) — Changes the traits assigned to the specified child view controller. _(deprecated)_
- [- overrideTraitCollectionForChildViewController:](<overridetraitcollection(forchild_).md>) — Retrieves the trait collection for a child view controller. _(deprecated)_
- [+ attemptRotationToDeviceOrientation](<attemptrotationtodeviceorientation().md>) — Attempts to rotate all windows to the orientation of the device. _(deprecated)_
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
