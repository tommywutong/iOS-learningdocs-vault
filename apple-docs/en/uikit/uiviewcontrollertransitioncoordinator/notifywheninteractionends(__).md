---
title: 'notifyWhenInteractionEnds(_:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 7.0+（10.0 起废弃）, iPadOS 7.0+（10.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）, tvOS（10.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/uikit/uiviewcontrollertransitioncoordinator/notifywheninteractionends(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiviewcontrollertransitioncoordinator/notifywheninteractionends(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiviewcontrollertransitioncoordinator/notifywheninteractionends%28_%3A%29.json'
content_hash: 'sha256:f87752a8ef85178e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIViewControllerTransitionCoordinator](../uiviewcontrollertransitioncoordinator.md)

# notifyWhenInteractionEnds(_:)

<sub>Instance Method</sub>

Registers a block to be executed when a transition changes from interactive to non-interactive.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
func notifyWhenInteractionEnds(_ handler: @escaping (any UIViewControllerTransitionCoordinatorContext) -> Void)
```

## Parameters

- `handler` — The block to execute when the transition changes from interactive to noninteractive. The block has no return value and takes the following parameter: - **context** — The contextual information for performing the animations. Use this object to get the animation-related information. For more information, see [UIViewControllerTransitionCoordinatorContext](../uiviewcontrollertransitioncoordinatorcontext.md).

## Discussion

Your block is executed both when the transition completes normally and when the user cancels the transition. In the case where the user cancels the transition, UIKit executes your `context` block, calls the [- viewWillDisappear:](<../uiviewcontroller/viewwilldisappear(__).md>) method on the presented view controller, and finally calls the [- viewWillAppear:](<../uiviewcontroller/viewwillappear(__).md>) method on the original view controller to signal that it’s once again visible.

Inside your block, you can get the value of the [cancelled](../uiviewcontrollertransitioncoordinatorcontext/iscancelled.md) method of the transition coordinator context and use that value to determine the appropriate course of action. For example, if the transition was canceled, you might use this block to remove any extra views that were added to the view hierarchy by a previous call to [- animateAlongsideTransition:completion:](<animate(alongsidetransition_completion_).md>) or [- animateAlongsideTransitionInView:animation:completion:](<animatealongsidetransition(in_animation_completion_).md>).

You can call this method multiple times to register multiple blocks. All of the registered blocks are executed when the transition state changes.

## See Also

### Responding to view controller transition progress

- [- animateAlongsideTransition:completion:](<animate(alongsidetransition_completion_).md>) — Runs the specified animations at the same time as the view controller transition animations.
- [- animateAlongsideTransitionInView:animation:completion:](<animatealongsidetransition(in_animation_completion_).md>) — Runs the specified animations in a view that’s outside of the designated container view.
- [- notifyWhenInteractionChangesUsingBlock:](<notifywheninteractionchanges(__).md>) — Registers a block to be executed when a transition changes from interactive to non-interactive.
