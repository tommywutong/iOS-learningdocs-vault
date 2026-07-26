---
title: CAPropertyAnimation
framework: Core Animation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/quartzcore/capropertyanimation
source_url: 'https://developer.apple.com/documentation/quartzcore/capropertyanimation'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/capropertyanimation.json'
content_hash: 'sha256:3b44ecb31719bfc8'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Animation](../quartzcore.md)

# CAPropertyAnimation

<sub>Class</sub>

An abstract subclass for creating animations that manipulate the value of layer properties.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class CAPropertyAnimation
```

## Overview

The property to animate is specified using a key path that is relative to the layer using the animation.

You do not create instances of [CAPropertyAnimation](capropertyanimation.md): to animate the properties of a Core Animation layer, create instance of the concrete subclasses [CABasicAnimation](cabasicanimation.md) or [CAKeyframeAnimation](cakeyframeanimation.md).

## Relationships

- **Inherits From**: [CAAnimation](caanimation.md)

- **Inherited By**: [CABasicAnimation](cabasicanimation.md), [CAKeyframeAnimation](cakeyframeanimation.md)

- **Conforms To**: [CAAction](caaction.md), [CAMediaTiming](camediatiming.md), [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCoding](../foundation/nscoding.md), [NSCopying](../foundation/nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [NSSecureCoding](../foundation/nssecurecoding.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Animated Key Path

- [keyPath](capropertyanimation/keypath.md) — Specifies the key path the receiver animates.

### Property Value Calculation Behavior

- [cumulative](capropertyanimation/iscumulative.md) — Determines if the value of the property is the value at the end of the previous repeat cycle, plus the value of the current repeat cycle.
- [additive](capropertyanimation/isadditive.md) — Determines if the value specified by the animation is added to the current render tree value to produce the new render tree value.
- [valueFunction](capropertyanimation/valuefunction.md) — An optional value function that is applied to interpolated values.

### Creating an Animation

- [+ animationWithKeyPath:](<capropertyanimation/init(keypath_).md>) — Creates and returns an `CAPropertyAnimation` instance for the specified key path.

## See Also

### Animation

- [CAAnimation](caanimation.md) — The abstract superclass for animations in Core Animation.
- [CAAnimationDelegate](caanimationdelegate.md) — Methods your app can implement to respond when animations start and stop.
- [CABasicAnimation](cabasicanimation.md) — An object that provides basic, single-keyframe animation capabilities for a layer property.
- [CAKeyframeAnimation](cakeyframeanimation.md) — An object that provides keyframe animation capabilities for a layer object.
- [CASpringAnimation](caspringanimation.md) — An animation that applies a spring-like force to a layer’s properties.
- [CATransition](catransition.md) — An object that provides an animated transition between a layer’s states.
- [CAValueFunction](cavaluefunction.md) — An object that provides a flexible method of defining animated transformations.
