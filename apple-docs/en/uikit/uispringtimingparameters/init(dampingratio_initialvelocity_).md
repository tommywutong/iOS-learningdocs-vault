---
title: 'init(dampingRatio:initialVelocity:)'
framework: UIKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, tvOS 10.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uispringtimingparameters/init(dampingratio:initialvelocity:)'
source_url: 'https://developer.apple.com/documentation/uikit/uispringtimingparameters/init(dampingratio:initialvelocity:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uispringtimingparameters/init%28dampingratio%3Ainitialvelocity%3A%29.json'
content_hash: 'sha256:ec9d1e11b374cc67'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UISpringTimingParameters](../uispringtimingparameters.md)

# init(dampingRatio:initialVelocity:)

<sub>Initializer</sub>

Creates a timing parameters object with the specified damping ratio and initial velocity.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
init(dampingRatio ratio: CGFloat, initialVelocity velocity: CGVector)
```

## Parameters

- `ratio` — The damping ratio to apply to the spring’s motion. To smoothly decelerate the animation without oscillation, specify a value of `1`. Specify values closer to `0` to create less damping and more oscillation.

- `velocity` — The target property’s initial rate of change at the start of the spring animation. If the target property doesn’t change, specify a vector with `dx` and `dy` components of `0`. For details about how to calculate this velocity, see [initialVelocity](initialvelocity.md).

## Return Value

An initialized spring timing parameters object or `nil` if the object could not be created.

## See Also

### Initializing a spring timing parameters object

- [- init](<init().md>) — Creates a default timing parameters object.
- [- initWithDampingRatio:](<init(dampingratio_).md>) — Creates a timing parameters object with the specified damping ratio.
- [- initWithMass:stiffness:damping:initialVelocity:](<init(mass_stiffness_damping_initialvelocity_).md>) — Creates a timing parameters object with the specified spring stiffness, mass, damping coefficient, and initial velocity.
- [- initWithCoder:](<init(coder_).md>) — Creates a timing parameters object from data in an unarchiver.
