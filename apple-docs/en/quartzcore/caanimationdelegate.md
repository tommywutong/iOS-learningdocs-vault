---
title: CAAnimationDelegate
framework: Core Animation
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.12+, tvOS 10.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/quartzcore/caanimationdelegate
source_url: 'https://developer.apple.com/documentation/quartzcore/caanimationdelegate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/caanimationdelegate.json'
content_hash: 'sha256:daf8916624ecae2b'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Animation](../quartzcore.md)

# CAAnimationDelegate

<sub>Protocol</sub>

Methods your app can implement to respond when animations start and stop.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
protocol CAAnimationDelegate : NSObjectProtocol
```

## Overview

You can use an animation delegate to execute additional logic when an animation starts or ends. For example, you may want to remove a layer from its parent once a fade out animation has completed.

The following example shows code taken from a class that implements [CAAnimationDelegate](caanimationdelegate.md) and has had a layer, named `sublayer`, added to its layer. The `fadeOut` function animates the opacity of `sublayer` and, once the animation has completed, [- animationDidStop:finished:](<caanimationdelegate/animationdidstop(__finished_).md>) removes it from its superlayer.

```swift
func fadeOut() {
    let fadeOutAnimation = CABasicAnimation()
    fadeOutAnimation.keyPath = "opacity"
    fadeOutAnimation.fromValue = 1
    fadeOutAnimation.toValue = 0
    fadeOutAnimation.duration = 0.25
    
    fadeOutAnimation.delegate = self
    
    sublayer.add(fadeOutAnimation,
                      forKey: "fade")
}
    
func animationDidStop(_ anim: CAAnimation, finished flag: Bool) {
    sublayer.removeFromSuperlayer()
}
```

## Relationships

- **Inherits From**: [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Customizing Start and Stop Times

- [- animationDidStart:](<caanimationdelegate/animationdidstart(__).md>) — Tells the delegate the animation has started.
- [- animationDidStop:finished:](<caanimationdelegate/animationdidstop(__finished_).md>) — Tells the delegate the animation has ended.

## See Also

### Animation

- [CAAnimation](caanimation.md) — The abstract superclass for animations in Core Animation.
- [CAPropertyAnimation](capropertyanimation.md) — An abstract subclass for creating animations that manipulate the value of layer properties.
- [CABasicAnimation](cabasicanimation.md) — An object that provides basic, single-keyframe animation capabilities for a layer property.
- [CAKeyframeAnimation](cakeyframeanimation.md) — An object that provides keyframe animation capabilities for a layer object.
- [CASpringAnimation](caspringanimation.md) — An animation that applies a spring-like force to a layer’s properties.
- [CATransition](catransition.md) — An object that provides an animated transition between a layer’s states.
- [CAValueFunction](cavaluefunction.md) — An object that provides a flexible method of defining animated transformations.
