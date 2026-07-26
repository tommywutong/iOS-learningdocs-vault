---
title: UIPercentDrivenInteractiveTransition
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uipercentdriveninteractivetransition
source_url: 'https://developer.apple.com/documentation/uikit/uipercentdriveninteractivetransition'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uipercentdriveninteractivetransition.json'
content_hash: 'sha256:76e2b251d18d09fa'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIPercentDrivenInteractiveTransition

<sub>Class</sub>

An object that drives an interactive animation between one view controller and another.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor class UIPercentDrivenInteractiveTransition
```

## Overview

A percent-driven interactive transition object relies on a transition animator delegate—a custom object that adopts the [UIViewControllerAnimatedTransitioning](uiviewcontrolleranimatedtransitioning.md) protocol—to set up and perform the animations.

To use this concrete class, return an instance of it from your view controller delegate when asked for an interactive transition controller. As user events arrive that would affect the progress of a transition, call the [- updateInteractiveTransition:](<uipercentdriveninteractivetransition/update(__).md>), [- cancelInteractiveTransition](<uipercentdriveninteractivetransition/cancel().md>), and [- finishInteractiveTransition](<uipercentdriveninteractivetransition/finish().md>) methods to reflect the current progress. For example, you might call these methods from a gesture recognizer to reflect how much of the gesture is completed.

You can subclass [UIPercentDrivenInteractiveTransition](uipercentdriveninteractivetransition.md), but if you do so you must start each of your method overrides with a call to the `super` implementation of the method.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [UIViewControllerInteractiveTransitioning](uiviewcontrollerinteractivetransitioning.md)

## Topics

### Accessing transition attributes

- [timingCurve](uipercentdriveninteractivetransition/timingcurve.md) — The timing curve to use when driving the animations.
- [completionCurve](uipercentdriveninteractivetransition/completioncurve.md) — Indicates the animation completion curve for an interactive transition.
- [duration](uipercentdriveninteractivetransition/duration.md) — The overall duration (in seconds) of the transition animation.
- [percentComplete](uipercentdriveninteractivetransition/percentcomplete.md) — The amount of the transition (specified as a percentage of the overall duration) that’s complete.
- [completionSpeed](uipercentdriveninteractivetransition/completionspeed.md) — The speed of the transition animation.
- [wantsInteractiveStart](uipercentdriveninteractivetransition/wantsinteractivestart.md) — A Boolean value indicating whether the animations are interactive initially.

### Managing a transition

- [- updateInteractiveTransition:](<uipercentdriveninteractivetransition/update(__).md>) — Updates the completion percentage of the transition.
- [- pauseInteractiveTransition](<uipercentdriveninteractivetransition/pause().md>) — Pauses an interruptible transition animation.
- [- cancelInteractiveTransition](<uipercentdriveninteractivetransition/cancel().md>) — Notifies the system that user interactions canceled the transition.
- [- finishInteractiveTransition](<uipercentdriveninteractivetransition/finish().md>) — Notifies the system that user interactions signaled the completion of the transition.

## See Also

### Interactive transitions

- [UIViewControllerInteractiveTransitioning](uiviewcontrollerinteractivetransitioning.md) — A set of methods that enable an object (such as a navigation controller) to drive a view controller transition.
- [UIViewImplicitlyAnimating](uiviewimplicitlyanimating.md) — An interface for modifying an animation while it’s running.
