---
title: UIViewControllerTransitionCoordinatorContext
framework: UIKit
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiviewcontrollertransitioncoordinatorcontext
source_url: 'https://developer.apple.com/documentation/uikit/uiviewcontrollertransitioncoordinatorcontext'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiviewcontrollertransitioncoordinatorcontext.json'
content_hash: 'sha256:a8a4cec441257d30'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIViewControllerTransitionCoordinatorContext

<sub>Protocol</sub>

A set of methods that provides information about an in-progress view controller transition.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor protocol UIViewControllerTransitionCoordinatorContext : NSObjectProtocol
```

## Overview

Don’t adopt this protocol in your own classes. UIKit creates an object that adopts this protocol and makes it available to your code when you animate changes using a transition coordinator object.

A transition coordinator context provides most of the same information as an object that adopts the [UIViewControllerContextTransitioning](uiviewcontrollercontexttransitioning.md) protocol. You use this contextual information to determine the animation parameters, such as the view in which the animations take place, whether the transition is interactive, or whether the transition was the result of an interface orientation change. You then apply that information to the animations you create.

Most animations take place in the view returned by the [containerView](uiviewcontrollertransitioncoordinatorcontext/containerview.md) method. And at the time your animation blocks are executed, the view hierarchy already contains the view of the _from_ view controller. You can use your animation blocks to animate additional content in that same container view or you can animate content in an entirely different view.

## Relationships

- **Inherits From**: [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

- **Inherited By**: [UIViewControllerTransitionCoordinator](uiviewcontrollertransitioncoordinator.md)

## Topics

### Getting the views and view controllers

- [- viewControllerForKey:](<uiviewcontrollertransitioncoordinatorcontext/viewcontroller(forkey_).md>) — Returns the view controllers involved in the transition.
- [- viewForKey:](<uiviewcontrollertransitioncoordinatorcontext/view(forkey_).md>) — Returns the specified view involved in the transition.
- [containerView](uiviewcontrollertransitioncoordinatorcontext/containerview.md) — Returns the view in which the transition takes place.

### Getting the behavior attributes

- [presentationStyle](uiviewcontrollertransitioncoordinatorcontext/presentationstyle.md) — The presentation style to use for the transition.
- [transitionDuration](uiviewcontrollertransitioncoordinatorcontext/transitionduration.md) — Returns the noninteractive duration of a transition.
- [completionCurve](uiviewcontrollertransitioncoordinatorcontext/completioncurve.md) — Returns the completion curve associated with the transition.
- [completionVelocity](uiviewcontrollertransitioncoordinatorcontext/completionvelocity.md) — Returns the starting velocity to use for any final animations.
- [percentComplete](uiviewcontrollertransitioncoordinatorcontext/percentcomplete.md) — Returns the percentage of completion for an interactive transition when it moves to its noninteractive phase.

### Getting the transition state

- [initiallyInteractive](uiviewcontrollertransitioncoordinatorcontext/initiallyinteractive.md) — A Boolean value indicating whether the transition started as an interactive transition.
- [interactive](uiviewcontrollertransitioncoordinatorcontext/isinteractive.md) — A Boolean value indicating whether the transition is currently interactive.
- [animated](uiviewcontrollertransitioncoordinatorcontext/isanimated.md) — A Boolean value indicating whether the transition is explicitly animated.
- [cancelled](uiviewcontrollertransitioncoordinatorcontext/iscancelled.md) — A Boolean value indicating whether an interactive transition was canceled.
- [isInterruptible](uiviewcontrollertransitioncoordinatorcontext/isinterruptible.md) — A Boolean value indicating whether the transition animations can be interrupted.

### Getting the rotation factor

- [targetTransform](uiviewcontrollertransitioncoordinatorcontext/targettransform.md) — Returns a transform indicating the amount of rotation being applied during the transition.

## See Also

### Transition coordinators

- [UIViewControllerTransitionCoordinator](uiviewcontrollertransitioncoordinator.md) — A set of methods that provides support for animations associated with a view controller transition.
