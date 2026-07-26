---
title: CASpringAnimation
framework: Core Animation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/quartzcore/caspringanimation
source_url: 'https://developer.apple.com/documentation/quartzcore/caspringanimation'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/caspringanimation.json'
content_hash: 'sha256:ffd0ea01ee161b0a'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Animation](../quartzcore.md)

# CASpringAnimation

<sub>Class</sub>

An animation that applies a spring-like force to a layer’s properties.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class CASpringAnimation
```

## Overview

You would typically use a spring animation to animate a layer’s position so that it appears to be pulled towards a target by a spring. The further the layer is from the target, the greater the acceleration towards it is.

[CASpringAnimation](caspringanimation.md) allows control over physically based attributes such as the spring’s damping and stiffness.

You can use a spring animation to animation properties of a layer other than its position. The following code shows how to create a spring animation that bounces a layer into view by animating its scale from `0` to `1`. Because the spring animation can overshoot its [toValue](cabasicanimation/tovalue.md), the animated layer may exceed its frame.

```swift
let springAnimation = CASpringAnimation(keyPath: "transform.scale")

springAnimation.fromValue = 0
springAnimation.toValue = 1
```

## Relationships

- **Inherits From**: [CABasicAnimation](cabasicanimation.md)

- **Conforms To**: [CAAction](caaction.md), [CAMediaTiming](camediatiming.md), [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCoding](../foundation/nscoding.md), [NSCopying](../foundation/nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [NSSecureCoding](../foundation/nssecurecoding.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Configuring Physical Attributes

- [damping](caspringanimation/damping.md) — Defines how the spring’s motion should be damped due to the forces of friction.
- [initialVelocity](caspringanimation/initialvelocity.md) — The initial velocity of the object attached to the spring.
- [mass](caspringanimation/mass.md) — The mass of the object attached to the end of the spring.
- [settlingDuration](caspringanimation/settlingduration.md) — The estimated duration required for the spring system to be considered at rest.
- [stiffness](caspringanimation/stiffness.md) — The spring stiffness coefficient.

### Initializers

- [- initWithPerceptualDuration:bounce:](<caspringanimation/init(perceptualduration_bounce_).md>)

### Instance Properties

- [allowsOverdamping](caspringanimation/allowsoverdamping.md)
- [bounce](caspringanimation/bounce.md)
- [perceptualDuration](caspringanimation/perceptualduration.md)

## See Also

### Animation

- [CAAnimation](caanimation.md) — The abstract superclass for animations in Core Animation.
- [CAAnimationDelegate](caanimationdelegate.md) — Methods your app can implement to respond when animations start and stop.
- [CAPropertyAnimation](capropertyanimation.md) — An abstract subclass for creating animations that manipulate the value of layer properties.
- [CABasicAnimation](cabasicanimation.md) — An object that provides basic, single-keyframe animation capabilities for a layer property.
- [CAKeyframeAnimation](cakeyframeanimation.md) — An object that provides keyframe animation capabilities for a layer object.
- [CATransition](catransition.md) — An object that provides an animated transition between a layer’s states.
- [CAValueFunction](cavaluefunction.md) — An object that provides a flexible method of defining animated transformations.
