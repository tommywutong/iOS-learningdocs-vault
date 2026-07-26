---
title: CAValueFunction
framework: Core Animation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/quartzcore/cavaluefunction
source_url: 'https://developer.apple.com/documentation/quartzcore/cavaluefunction'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/cavaluefunction.json'
content_hash: 'sha256:e7709c86465d8f6a'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Animation](../quartzcore.md)

# CAValueFunction

<sub>Class</sub>

An object that provides a flexible method of defining animated transformations.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class CAValueFunction
```

## Overview

You can use a value function to specify the individual components of an animated transform.

For example, to create a basic animation that rotates a layer from 0° to 180° around its z-axis, you would create a [CABasicAnimation](cabasicanimation.md) object with a [fromValue](cabasicanimation/fromvalue.md) of `0`, a [toValue](cabasicanimation/tovalue.md) of [pi](../swift/float/pi.md), and a [valueFunction](capropertyanimation/valuefunction.md) of a [CAValueFunction](cavaluefunction.md) with a function name of [kCAValueFunctionRotateZ](cavaluefunctionname/rotatez.md).

The following code shows how you would create such a rotation and apply it to a [CALayer](calayer.md) named `rotatingLayer`.

```swift
let rotateAnimation = CABasicAnimation()
rotateAnimation.valueFunction = CAValueFunction(name: kCAValueFunctionRotateZ)
rotateAnimation.fromValue = 0
rotateAnimation.toValue = Float.pi
rotateAnimation.duration = 3
rotatingLayer.add(rotateAnimation,
                  forKey: "transform")
```

The value functions [kCAValueFunctionScale](cavaluefunctionname/scale.md) and [kCAValueFunctionTranslate](cavaluefunctionname/translate.md) require 3 values, for the individual `x`, `y` and `z` components. When working with these value functions, you specify the animation’s [fromValue](cabasicanimation/fromvalue.md) and [toValue](cabasicanimation/tovalue.md) as arrays.

The following code shows how you could animate a layer’s scale from `0` to `1` using a value function.

```swift
let scaleAnimation = CABasicAnimation()
scaleAnimation.valueFunction = CAValueFunction(name: kCAValueFunctionScale)
scaleAnimation.fromValue = [0, 0, 0]
scaleAnimation.toValue = [1, 1, 1]
scaleAnimation.duration = 3
scalingLayer.add(scaleAnimation,
                 forKey: "transform")
```

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCoding](../foundation/nscoding.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [NSSecureCoding](../foundation/nssecurecoding.md)

## Topics

### Getting Value Function Properties

- [name](cavaluefunction/name.md) — Returns the name of the value function.

### Creating and Initializing Value Functions

- [+ functionWithName:](<cavaluefunction/init(name_).md>) — Returns the value function object identified by the name.

### Constants

- [Rotate Value Functions](rotate-value-functions.md) — Rotate value transform functions construct a 4x4 matrix that represents the corresponding rotation matrix.
- [Scale Value Functions](scale-value-functions.md) — Scale value transform functions construct a 4x4 matrix that represents the corresponding scale matrix.
- [Translate Functions](translate-functions.md) — Translate value transform functions construct a 4x4 matrix that represents the corresponding translate matrix.

### Initializers

- [init(coder:)](<cavaluefunction/init(coder_).md>)

## See Also

### Animation

- [CAAnimation](caanimation.md) — The abstract superclass for animations in Core Animation.
- [CAAnimationDelegate](caanimationdelegate.md) — Methods your app can implement to respond when animations start and stop.
- [CAPropertyAnimation](capropertyanimation.md) — An abstract subclass for creating animations that manipulate the value of layer properties.
- [CABasicAnimation](cabasicanimation.md) — An object that provides basic, single-keyframe animation capabilities for a layer property.
- [CAKeyframeAnimation](cakeyframeanimation.md) — An object that provides keyframe animation capabilities for a layer object.
- [CASpringAnimation](caspringanimation.md) — An animation that applies a spring-like force to a layer’s properties.
- [CATransition](catransition.md) — An object that provides an animated transition between a layer’s states.
