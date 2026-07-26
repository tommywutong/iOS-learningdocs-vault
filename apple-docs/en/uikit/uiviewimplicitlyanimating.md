---
title: UIViewImplicitlyAnimating
framework: UIKit
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiviewimplicitlyanimating
source_url: 'https://developer.apple.com/documentation/uikit/uiviewimplicitlyanimating'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiviewimplicitlyanimating.json'
content_hash: 'sha256:f4b281e0cb75fc90'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIViewImplicitlyAnimating

<sub>Protocol</sub>

An interface for modifying an animation while it’s running.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor protocol UIViewImplicitlyAnimating : UIViewAnimating
```

## Overview

Animator objects used in interruptible view controller transitions adopt the [UIViewImplicitlyAnimating](uiviewimplicitlyanimating.md) protocol to modify in-flight transition animations. This protocol also conforms to the [UIViewAnimating](uiviewanimating.md) protocol, which specifies methods for starting and stopping animations and for updating their state.

The [UIViewPropertyAnimator](uiviewpropertyanimator.md) class adopts this protocol and implements all of its methods. You can adopt this protocol in your own classes to implement custom animator objects. When adopting this protocol, it’s recommended that you implement all of the methods.

## Relationships

- **Inherits From**: [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [UIViewAnimating](uiviewanimating.md)

- **Conforming Types**: [UIViewPropertyAnimator](uiviewpropertyanimator.md)

## Topics

### Modifying animations

- [- addAnimations:](<uiviewimplicitlyanimating/addanimations(__).md>) — Adds the specified animation block to the animator.
- [- addAnimations:delayFactor:](<uiviewimplicitlyanimating/addanimations(__delayfactor_).md>) — Adds the specified animation block to the animator with a delay.
- [- addCompletion:](<uiviewimplicitlyanimating/addcompletion(__).md>) — Adds the specified completion block to the animator.
- [- continueAnimationWithTimingParameters:durationFactor:](<uiviewimplicitlyanimating/continueanimation(withtimingparameters_durationfactor_).md>) — Adjusts the final timing and duration of a paused animation.
