---
title: UISpringTimingParameters
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, tvOS 10.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uispringtimingparameters
source_url: 'https://developer.apple.com/documentation/uikit/uispringtimingparameters'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uispringtimingparameters.json'
content_hash: 'sha256:e013f3909fb3f493'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UISpringTimingParameters

<sub>Class</sub>

The timing information for animations that mimics the behavior of a spring.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor class UISpringTimingParameters
```

## Overview

The timing provided by a [UISpringTimingParameters](uispringtimingparameters.md) object mimics the behavior of a spring acting on the value of the property being animated. This property’s value accelerates toward its final value according to the relative force of the spring, which you configure. It then oscillates around that final value until it comes to a rest. The speed at which a property animates to its new value is based on the initial velocity of the value and the damping ratio applied to the spring. You can specify those values directly or using analogous spring-related values.

Use instances of this class to specify custom timing curves when creating animations with objects that adopt the [UIViewAnimating](uiviewanimating.md) protocol, such as [UIViewPropertyAnimator](uiviewpropertyanimator.md). Spring animations are commonly used to modify a view’s position onscreen, but you can apply the timing to any of the view’s properties to get a similar type of animation timing.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCoding](../foundation/nscoding.md), [NSCopying](../foundation/nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [UITimingCurveProvider](uitimingcurveprovider.md)

## Topics

### Initializing a spring timing parameters object

- [- init](<uispringtimingparameters/init().md>) — Creates a default timing parameters object.
- [- initWithDampingRatio:](<uispringtimingparameters/init(dampingratio_).md>) — Creates a timing parameters object with the specified damping ratio.
- [- initWithDampingRatio:initialVelocity:](<uispringtimingparameters/init(dampingratio_initialvelocity_).md>) — Creates a timing parameters object with the specified damping ratio and initial velocity.
- [- initWithMass:stiffness:damping:initialVelocity:](<uispringtimingparameters/init(mass_stiffness_damping_initialvelocity_).md>) — Creates a timing parameters object with the specified spring stiffness, mass, damping coefficient, and initial velocity.
- [- initWithCoder:](<uispringtimingparameters/init(coder_).md>) — Creates a timing parameters object from data in an unarchiver.

### Getting the initial velocity

- [initialVelocity](uispringtimingparameters/initialvelocity.md) — The target property’s rate of change at the start of a spring animation, enabling a smooth transition into the animation.

### Initializers

- [- initWithDuration:bounce:](<uispringtimingparameters/init(duration_bounce_).md>)
- [- initWithDuration:bounce:initialVelocity:](<uispringtimingparameters/init(duration_bounce_initialvelocity_).md>)

## See Also

### Timing curves

- [UITimingCurveProvider](uitimingcurveprovider.md) — An interface for providing the timing information needed to perform animations.
- [UICubicTimingParameters](uicubictimingparameters.md) — The timing information for animations in the form of a cubic Bézier curve.
