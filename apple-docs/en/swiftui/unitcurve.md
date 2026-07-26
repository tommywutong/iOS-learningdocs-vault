---
title: UnitCurve
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/unitcurve
source_url: 'https://developer.apple.com/documentation/swiftui/unitcurve'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/unitcurve.json'
content_hash: 'sha256:9e2d45f928c89a01'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# UnitCurve

<sub>Structure</sub>

A  function defined by a two-dimensional curve that maps an input progress in the range [0,1] to an output progress that is also in the range [0,1]. By changing the shape of the curve, the effective speed of an animation or other interpolation can be changed.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct UnitCurve
```

## Overview

The horizontal (x) axis defines the input progress: a single input progress value in the range [0,1] must be provided when evaluating a curve.

The vertical (y) axis maps to the output progress: when a curve is evaluated, the y component of the point that intersects the input progress is returned.

## Relationships

- **Conforms To**: [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Getting a linear curve

- [linear](unitcurve/linear.md) — A linear curve.

### Getting easing curves

- [easeIn](unitcurve/easein.md) — A bezier curve that starts out slowly, then speeds up as it finishes.
- [easeOut](unitcurve/easeout.md) — A bezier curve that starts out quickly, then slows down as it approaches the end.
- [easeInOut](unitcurve/easeinout.md) — A bezier curve that starts out slowly, speeds up over the middle, then slows down again as it approaches the end.
- [circularEaseIn](unitcurve/circulareasein.md) — A curve that starts out slowly, then speeds up as it finishes.
- [circularEaseOut](unitcurve/circulareaseout.md) — A circular curve that starts out quickly, then slows down as it approaches the end.
- [circularEaseInOut](unitcurve/circulareaseinout.md) — A circular curve that starts out slowly, speeds up over the middle, then slows down again as it approaches the end.

### Creating a general Bezier curve

- [bezier(startControlPoint:endControlPoint:)](<unitcurve/bezier(startcontrolpoint_endcontrolpoint_).md>) — Creates a new curve using bezier control points.

### Inverting a curve

- [inverse](unitcurve/inverse.md) — Returns a copy of the curve with its x and y components swapped.

### Getting curve characteristics

- [value(at:)](<unitcurve/value(at_).md>) — Returns the output value (y component) of the curve at the given time.
- [velocity(at:)](<unitcurve/velocity(at_).md>) — Returns the rate of change (first derivative) of the output value of the curve at the given time.

### Deprecated symbols

- [easeInEaseOut](unitcurve/easeineaseout.md) — A bezier curve that starts out slowly, speeds up over the middle, then slows down again as it approaches the end. _(deprecated)_

## See Also

### Creating custom animations

- [CustomAnimation](customanimation.md) — A type that defines how an animatable value changes over time.
- [AnimationContext](animationcontext.md) — Contextual values that a custom animation can use to manage state and access a view’s environment.
- [AnimationState](animationstate.md) — A container that stores the state for a custom animation.
- [AnimationStateKey](animationstatekey.md) — A key for accessing animation state values.
- [Spring](spring.md) — A representation of a spring’s motion.
