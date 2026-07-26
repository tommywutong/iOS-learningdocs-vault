---
title: CAKeyframeAnimation
framework: Core Animation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/quartzcore/cakeyframeanimation
source_url: 'https://developer.apple.com/documentation/quartzcore/cakeyframeanimation'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/cakeyframeanimation.json'
content_hash: 'sha256:ee8c8880b9508a29'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Animation](../quartzcore.md)

# CAKeyframeAnimation

<sub>Class</sub>

An object that provides keyframe animation capabilities for a layer object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class CAKeyframeAnimation
```

## Overview

You create a [CAKeyframeAnimation](cakeyframeanimation.md) object using the inherited [+ animationWithKeyPath:](<capropertyanimation/init(keypath_).md>) method, specifying the key path of the property that you want to animate on the layer. You can then specify the keyframe values to use to control the timing and animation behavior.

For most types of animations, you specify the keyframe values using the [values](cakeyframeanimation/values.md) and [keyTimes](cakeyframeanimation/keytimes.md) properties. During the animation, Core Animation generates intermediate values by interpolating between the values you provide. When animating a value that is a coordinate point, such as the layer’s position, you can specify a [path](cakeyframeanimation/path.md) for that point to follow instead of individual values. The pacing of the animation is controlled by the timing information you provide.

The following code shows how to create a keyframe animation that animates a layer’s background color from red to green to blue over a two second duration.

```swift
let colorKeyframeAnimation = CAKeyframeAnimation(keyPath: "backgroundColor")

colorKeyframeAnimation.values = [UIColor.red.cgColor,
                                 UIColor.green.cgColor,
                                 UIColor.blue.cgColor]
colorKeyframeAnimation.keyTimes = [0, 0.5, 1]
colorKeyframeAnimation.duration = 2
```

## Relationships

- **Inherits From**: [CAPropertyAnimation](capropertyanimation.md)

- **Conforms To**: [CAAction](caaction.md), [CAMediaTiming](camediatiming.md), [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCoding](../foundation/nscoding.md), [NSCopying](../foundation/nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [NSSecureCoding](../foundation/nssecurecoding.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Providing keyframe values

- [values](cakeyframeanimation/values.md) — An array of objects that specify the keyframe values to use for the animation.
- [path](cakeyframeanimation/path.md) — The path for a point-based property to follow.

### Keyframe timing

- [keyTimes](cakeyframeanimation/keytimes.md) — An optional array of `NSNumber` objects that define the time at which to apply a given keyframe segment.
- [timingFunctions](cakeyframeanimation/timingfunctions.md) — An optional array of `CAMediaTimingFunction` objects that define the pacing for each keyframe segment.
- [calculationMode](cakeyframeanimation/calculationmode.md) — Specifies how intermediate keyframe values are calculated by the receiver.

### Rotation Mode Attribute

- [rotationMode](cakeyframeanimation/rotationmode.md) — Determines whether objects animating along the path rotate to match the path tangent.

### Cubic Mode Attributes

- [tensionValues](cakeyframeanimation/tensionvalues.md) — An array of numbers that define the tightness of the curve.
- [continuityValues](cakeyframeanimation/continuityvalues.md) — An array of numbers that define the sharpness of the timing curve’s corners.
- [biasValues](cakeyframeanimation/biasvalues.md) — An array of numbers that define the position of the curve relative to a control point.

### Constants

- [Rotation Mode Values](rotation-mode-values.md) — These constants are used by the [rotationMode](cakeyframeanimation/rotationmode.md) property.
- [Value calculation modes](value-calculation-modes.md) — These constants are used by the [calculationMode](cakeyframeanimation/calculationmode.md) property.

## See Also

### Animation

- [CAAnimation](caanimation.md) — The abstract superclass for animations in Core Animation.
- [CAAnimationDelegate](caanimationdelegate.md) — Methods your app can implement to respond when animations start and stop.
- [CAPropertyAnimation](capropertyanimation.md) — An abstract subclass for creating animations that manipulate the value of layer properties.
- [CABasicAnimation](cabasicanimation.md) — An object that provides basic, single-keyframe animation capabilities for a layer property.
- [CASpringAnimation](caspringanimation.md) — An animation that applies a spring-like force to a layer’s properties.
- [CATransition](catransition.md) — An object that provides an animated transition between a layer’s states.
- [CAValueFunction](cavaluefunction.md) — An object that provides a flexible method of defining animated transformations.
