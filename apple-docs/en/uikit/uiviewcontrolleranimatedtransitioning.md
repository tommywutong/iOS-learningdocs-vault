---
title: UIViewControllerAnimatedTransitioning
framework: UIKit
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiviewcontrolleranimatedtransitioning
source_url: 'https://developer.apple.com/documentation/uikit/uiviewcontrolleranimatedtransitioning'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiviewcontrolleranimatedtransitioning.json'
content_hash: 'sha256:679dbf9767ab3cee'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIViewControllerAnimatedTransitioning

<sub>Protocol</sub>

A set of methods for implementing the animations for a custom view controller transition.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor protocol UIViewControllerAnimatedTransitioning : NSObjectProtocol
```

## Overview

The methods in this protocol let you define an animator object, which creates the animations for transitioning a view controller on or off screen in a fixed amount of time. The animations you create using this protocol must not be interactive. To create interactive transitions, you must combine your animator object with another object that controls the timing of your animations.

In your animator object, implement the [- transitionDuration:](<uiviewcontrolleranimatedtransitioning/transitionduration(using_).md>) method to specify the duration of your transition and implement the [- animateTransition:](<uiviewcontrolleranimatedtransitioning/animatetransition(using_).md>) method to create the animations themselves. Information about the objects involved in the transition is passed to your [- animateTransition:](<uiviewcontrolleranimatedtransitioning/animatetransition(using_).md>) method in the form of a context object. Use the information provided by that object to move the target view controller’s view on or off screen over the specified duration.

Create your animator object from a transitioning delegate — an object that conforms to the [UIViewControllerTransitioningDelegate](uiviewcontrollertransitioningdelegate.md) protocol. When presenting a view controller, set the presentation style to [UIModalPresentationCustom](uimodalpresentationstyle/custom.md) and assign your transitioning delegate to the view controller’s [transitioningDelegate](uiviewcontroller/transitioningdelegate.md) property. The view controller retrieves your animator object from the transitioning delegate and uses it to perform the animations. You can provide separate animator objects for presenting and dismissing the view controller.

To add user interaction to a view controller transition, you must use an animator object together with an _interactive animator object_** **— a custom object that adopts the [UIViewControllerInteractiveTransitioning](uiviewcontrollerinteractivetransitioning.md) protocol. For more on defining interactive transitions, see [UIViewControllerInteractiveTransitioning](uiviewcontrollerinteractivetransitioning.md).

## Relationships

- **Inherits From**: [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

- **Conforming Types**: [UIDocumentBrowserTransitionController](uidocumentbrowsertransitioncontroller.md), [UISearchController](uisearchcontroller.md)

## Topics

### Performing a transition

- [- animateTransition:](<uiviewcontrolleranimatedtransitioning/animatetransition(using_).md>) — Tells your animator object to perform the transition animations.
- [- animationEnded:](<uiviewcontrolleranimatedtransitioning/animationended(__).md>) — Tells your animator object that the transition animations have finished.

### Reporting transition duration

- [- transitionDuration:](<uiviewcontrolleranimatedtransitioning/transitionduration(using_).md>) — Asks your animator object for the duration (in seconds) of the transition animation.

### Returning an interruptible animator

- [- interruptibleAnimatorForTransition:](<uiviewcontrolleranimatedtransitioning/interruptibleanimator(using_).md>) — Returns the interruptible animator to use during the transition.

## See Also

### Non-interactive transitions

- [UIViewControllerContextTransitioning](uiviewcontrollercontexttransitioning.md) — A set of methods that provide contextual information for transition animations between view controllers.
