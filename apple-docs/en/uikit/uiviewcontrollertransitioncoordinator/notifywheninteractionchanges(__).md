---
title: 'notifyWhenInteractionChanges(_:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, tvOS 10.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiviewcontrollertransitioncoordinator/notifywheninteractionchanges(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiviewcontrollertransitioncoordinator/notifywheninteractionchanges(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiviewcontrollertransitioncoordinator/notifywheninteractionchanges%28_%3A%29.json'
content_hash: 'sha256:69333938e8468c8f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIViewControllerTransitionCoordinator](../uiviewcontrollertransitioncoordinator.md)

# notifyWhenInteractionChanges(_:)

<sub>Instance Method</sub>

Registers a block to be executed when a transition changes from interactive to non-interactive.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func notifyWhenInteractionChanges(_ handler: @escaping (any UIViewControllerTransitionCoordinatorContext) -> Void)
```

## Parameters

- `handler` — The block to execute when the transition changes from interactive to noninteractive. The block has no return value and takes the following parameter:

## Discussion

Your handler block is executed any time the transition changes from interactive to noninteractive, including when the transition ends or is canceled. When the user cancels a transition, UIKit executes your context block, calls the [- viewWillDisappear:](<../uiviewcontroller/viewwilldisappear(__).md>) method on the presented view controller, and finally calls the [- viewWillAppear:](<../uiviewcontroller/viewwillappear(__).md>) method on the original view controller to signal that it’s once again visible.

Use the [interactive](../uiviewcontrollertransitioncoordinatorcontext/isinteractive.md) property of the context object to determine the current interactivity of the transition. You can also use the value of the [cancelled](../uiviewcontrollertransitioncoordinatorcontext/iscancelled.md) property to determine an appropriate course of action. For example, if the transition was canceled, you might remove any extra views that were added to the view hierarchy by a previous call to [- animateAlongsideTransition:completion:](<animate(alongsidetransition_completion_).md>) or [- animateAlongsideTransitionInView:animation:completion:](<animatealongsidetransition(in_animation_completion_).md>).

You can call this method multiple times to register multiple blocks. All of the registered blocks are executed when the transition state changes.

## See Also

### Responding to view controller transition progress

- [- animateAlongsideTransition:completion:](<animate(alongsidetransition_completion_).md>) — Runs the specified animations at the same time as the view controller transition animations.
- [- animateAlongsideTransitionInView:animation:completion:](<animatealongsidetransition(in_animation_completion_).md>) — Runs the specified animations in a view that’s outside of the designated container view.
- [- notifyWhenInteractionEndsUsingBlock:](<notifywheninteractionends(__).md>) — Registers a block to be executed when a transition changes from interactive to non-interactive. _(deprecated)_
