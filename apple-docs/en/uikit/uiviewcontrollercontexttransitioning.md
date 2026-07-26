---
title: UIViewControllerContextTransitioning
framework: UIKit
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiviewcontrollercontexttransitioning
source_url: 'https://developer.apple.com/documentation/uikit/uiviewcontrollercontexttransitioning'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiviewcontrollercontexttransitioning.json'
content_hash: 'sha256:57d9f6b3cea4d9ae'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIViewControllerContextTransitioning

<sub>Protocol</sub>

A set of methods that provide contextual information for transition animations between view controllers.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor protocol UIViewControllerContextTransitioning : NSObjectProtocol
```

## Overview

Don’t adopt this protocol in your own classes, nor should you directly create objects that adopt this protocol. During a transition, the animator objects involved in that transition receive a fully configured context object from UIKit. Custom animator objects — objects that adopt the [UIViewControllerAnimatedTransitioning](uiviewcontrolleranimatedtransitioning.md) or [UIViewControllerInteractiveTransitioning](uiviewcontrollerinteractivetransitioning.md) protocol — should simply retrieve the information they need from the provided object.

A context object encapsulates information about the views and view controllers involved in the transition. It also contains details about the how to execute the transition. For interactive transitions, the interactive animator object uses the methods of this protocol to report the animation’s progress. When the animation starts, the interactive animator object must save a pointer to the context object. Based on user interactions, the animator object then calls the [- updateInteractiveTransition:](<uiviewcontrollercontexttransitioning/updateinteractivetransition(__).md>), [- finishInteractiveTransition](<uiviewcontrollercontexttransitioning/finishinteractivetransition().md>), or [- cancelInteractiveTransition](<uiviewcontrollercontexttransitioning/cancelinteractivetransition().md>) methods to report the progress toward completing the animation. Those methods send that information to UIKit so that it can drive the timing of the animations.

> [!important] Important
> When defining custom animator objects, always check the value returned by the [animated](uiviewcontrollercontexttransitioning/isanimated.md) method to determine whether you should create animations at all. And when you do create transition animations, always call the [- completeTransition:](<uiviewcontrollercontexttransitioning/completetransition(__).md>) method from an appropriate completion block to let UIKit know when all of your animations have finished.

## Relationships

- **Inherits From**: [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Accessing the transition objects

- [containerView](uiviewcontrollercontexttransitioning/containerview.md) — The view that acts as the superview for the views involved in the transition.
- [- viewControllerForKey:](<uiviewcontrollercontexttransitioning/viewcontroller(forkey_).md>) — Returns a view controller involved in the transition.
- [- viewForKey:](<uiviewcontrollercontexttransitioning/view(forkey_).md>) — Returns the specified view involved in the transition.

### Getting the transition frame rectangles

- [- initialFrameForViewController:](<uiviewcontrollercontexttransitioning/initialframe(for_).md>) — Returns the starting frame rectangle for the specified view controller’s view.
- [- finalFrameForViewController:](<uiviewcontrollercontexttransitioning/finalframe(for_).md>) — Returns the ending frame rectangle for the specified view controller’s view.

### Getting the transition behaviors

- [animated](uiviewcontrollercontexttransitioning/isanimated.md) — A Boolean value indicating whether the transition should be animated.
- [interactive](uiviewcontrollercontexttransitioning/isinteractive.md) — A Boolean value indicating whether the transition is currently interactive.
- [presentationStyle](uiviewcontrollercontexttransitioning/presentationstyle.md) — Returns the presentation style for the view controller transition.

### Reporting the transition progress

- [- completeTransition:](<uiviewcontrollercontexttransitioning/completetransition(__).md>) — Notifies the system that the transition animation is done.
- [- updateInteractiveTransition:](<uiviewcontrollercontexttransitioning/updateinteractivetransition(__).md>) — Updates the completion percentage of the transition.
- [- pauseInteractiveTransition](<uiviewcontrollercontexttransitioning/pauseinteractivetransition().md>) — Tells the system to pause the animations.
- [- finishInteractiveTransition](<uiviewcontrollercontexttransitioning/finishinteractivetransition().md>) — Notifies the system that user interactions signaled the completion of the transition.
- [- cancelInteractiveTransition](<uiviewcontrollercontexttransitioning/cancelinteractivetransition().md>) — Notifies the system that user interactions canceled the transition.
- [transitionWasCancelled](uiviewcontrollercontexttransitioning/transitionwascancelled.md) — Returns a Boolean value indicating whether the transition was canceled.

### Getting the rotation factor

- [targetTransform](uiviewcontrollercontexttransitioning/targettransform.md) — Returns a transform indicating the amount of rotation being applied during the transition.

### Constants

- [UITransitionContextViewControllerKey](uitransitioncontextviewcontrollerkey.md) — The keys you use to identify the view controllers involved in a transition.
- [UITransitionContextViewKey](uitransitioncontextviewkey.md) — The keys you use to identify the views involved in a transition.

## See Also

### Non-interactive transitions

- [UIViewControllerAnimatedTransitioning](uiviewcontrolleranimatedtransitioning.md) — A set of methods for implementing the animations for a custom view controller transition.
