---
title: UIViewControllerInteractiveTransitioning
framework: UIKit
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiviewcontrollerinteractivetransitioning
source_url: 'https://developer.apple.com/documentation/uikit/uiviewcontrollerinteractivetransitioning'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiviewcontrollerinteractivetransitioning.json'
content_hash: 'sha256:f1add18238637421'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIViewControllerInteractiveTransitioning

<sub>Protocol</sub>

A set of methods that enable an object (such as a navigation controller) to drive a view controller transition.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor protocol UIViewControllerInteractiveTransitioning : NSObjectProtocol
```

## Overview

An _interactive transition delegate_ (which is the term for an object that supports this protocol) can respond to touch events, or to time-varying programmatic input, by speeding up, slowing down, or even reversing the progress of a view controller transition. For example, an interactive transition on a navigation controller could respond to a swipe gesture by moving a view controller onto or off of the navigation stack.

To support an interactive view controller transition, you must also provide a transition animator delegate, which is a custom object that adopts the [UIViewControllerAnimatedTransitioning](uiviewcontrolleranimatedtransitioning.md) protocol. The transition delegate and the transition animator can, if you wish, be defined within a single custom class, but the class must adopt both protocols.

If you instead want to provide a fixed-duration animated view controller transition — one that doesn’t support user interaction — use a transition animator delegate on its own. Refer to [UIViewControllerAnimatedTransitioning](uiviewcontrolleranimatedtransitioning.md).

For the methods you can call to retrieve view transition context information from within your [- startInteractiveTransition:](<uiviewcontrollerinteractivetransitioning/startinteractivetransition(__).md>) method, refer to [UIViewControllerContextTransitioning](uiviewcontrollercontexttransitioning.md).

## Relationships

- **Inherits From**: [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

- **Conforming Types**: [UIPercentDrivenInteractiveTransition](uipercentdriveninteractivetransition.md)

## Topics

### Starting an interactive transition

- [- startInteractiveTransition:](<uiviewcontrollerinteractivetransitioning/startinteractivetransition(__).md>) — Called when the system needs to set up the interactive portions of a view controller transition and start the animations.
- [wantsInteractiveStart](uiviewcontrollerinteractivetransitioning/wantsinteractivestart.md) — A Boolean value indicating whether the transition is interactive when it starts.

### Providing a transition’s completion characteristics

- [completionCurve](uiviewcontrollerinteractivetransitioning/completioncurve.md) — Called when the system needs the animation completion curve for an interactive view controller transition.
- [completionSpeed](uiviewcontrollerinteractivetransitioning/completionspeed.md) — Called when the system needs the speed at which to complete an interactive transition, after the interactive portion is finished.

## See Also

### Interactive transitions

- [UIPercentDrivenInteractiveTransition](uipercentdriveninteractivetransition.md) — An object that drives an interactive animation between one view controller and another.
- [UIViewImplicitlyAnimating](uiviewimplicitlyanimating.md) — An interface for modifying an animation while it’s running.
