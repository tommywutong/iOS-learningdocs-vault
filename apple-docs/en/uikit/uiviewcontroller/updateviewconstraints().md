---
title: updateViewConstraints()
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, swift, swift, swift, occ, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiviewcontroller/updateviewconstraints()
source_url: 'https://developer.apple.com/documentation/uikit/uiviewcontroller/updateviewconstraints()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiviewcontroller/updateviewconstraints%28%29.json'
content_hash: 'sha256:2cc7a378e8a410a8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIViewController](../uiviewcontroller.md)

# updateViewConstraints()

<sub>Instance Method</sub>

Notifies the view controller when its view needs to update its constraints.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func updateViewConstraints()
```

## Discussion

Override this method to optimize changes to your constraints.

> [!note] Note
> It is almost always cleaner and easier to update a constraint immediately after the affecting change has occurred. For example, if you want to change a constraint in response to a button tap, make that change directly in the button’s action method.
>
> You should only override this method when changing constraints in place is too slow, or when a view is producing a number of redundant changes.

To schedule a change, call [- setNeedsUpdateConstraints](<../uiview/setneedsupdateconstraints().md>) on the view. The system then calls your implementation of [- updateViewConstraints](<updateviewconstraints().md>) before the layout occurs. This lets you verify that all necessary constraints for your content are in place at a time when your properties are not changing.

Your implementation must be as efficient as possible. Do not deactivate all your constraints, then reactivate the ones you need. Instead, your app must have some way of tracking your constraints, and validating them during each update pass. Only change items that need to be changed. During each update pass, you must ensure that you have the appropriate constraints for the app’s current state.

Do not call [- setNeedsUpdateConstraints](<../uiview/setneedsupdateconstraints().md>) inside your implementation. Calling [- setNeedsUpdateConstraints](<../uiview/setneedsupdateconstraints().md>) schedules another update pass, creating a feedback loop.

> [!important] Important
> Call `[super updateViewConstraints]` as the final step in your implementation.

In iOS 18 and later, UIKit supports automatic trait tracking inside this method for traits from this view controller’s `traitCollection` and the `traitCollection` of its [view](view.md). For more information, see [Automatic trait tracking](../automatic-trait-tracking.md).

This method supports automatic observation tracking. For more information, see [Updating views automatically with observation tracking in UIKit](../updating-views-automatically-with-observation-tracking-in-uikit.md).

## See Also

### Observing data in view controllers

- [- updateProperties](<updateproperties().md>) — Configures the view controller’s content and styling properties.
- [- viewWillLayoutSubviews](<viewwilllayoutsubviews().md>) — Notifies the view controller that its view is about to lay out its subviews.
- [- viewDidLayoutSubviews](<viewdidlayoutsubviews().md>) — Notifies the view controller when its view finishes laying out its subviews.
- [updateContentUnavailableConfiguration(using:)](<updatecontentunavailableconfiguration(using_).md>) — Updates the content-unavailable configuration for the provided state.
