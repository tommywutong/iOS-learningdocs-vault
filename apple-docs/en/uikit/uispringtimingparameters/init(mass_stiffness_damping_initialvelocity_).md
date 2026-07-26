---
title: 'init(mass:stiffness:damping:initialVelocity:)'
framework: UIKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, tvOS 10.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uispringtimingparameters/init(mass:stiffness:damping:initialvelocity:)'
source_url: 'https://developer.apple.com/documentation/uikit/uispringtimingparameters/init(mass:stiffness:damping:initialvelocity:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uispringtimingparameters/init%28mass%3Astiffness%3Adamping%3Ainitialvelocity%3A%29.json'
content_hash: 'sha256:61c1dd8163155bba'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UISpringTimingParameters](../uispringtimingparameters.md)

# init(mass:stiffness:damping:initialVelocity:)

<sub>Initializer</sub>

Creates a timing parameters object with the specified spring stiffness, mass, damping coefficient, and initial velocity.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
init(mass: CGFloat, stiffness: CGFloat, damping: CGFloat, initialVelocity velocity: CGVector)
```

## Parameters

- `mass` — The effective mass of the animated property. This value must be greater than `0`.

- `stiffness` — The spring stiffness coefficient. Higher values correspond to a stiffer spring that yields a greater amount of force for moving objects.

- `damping` — The damping force to apply to the spring’s motion. This value is used to compute the damping ratio.

- `velocity` — The target property’s initial rate of change at the start of the spring animation. If the target property doesn’t change, specify a vector with `dx` and `dy` components of `0`. For details about how to calculate this velocity, see [initialVelocity](initialvelocity.md).

## Return Value

An initialized spring timing parameters object or `nil` if the object could not be created.

## Discussion

The damping ratio for the spring is computed from the formula `damping` / (2 * sqrt (`stiffness` * `mass`)).

## See Also

### Initializing a spring timing parameters object

- [- init](<init().md>) — Creates a default timing parameters object.
- [- initWithDampingRatio:](<init(dampingratio_).md>) — Creates a timing parameters object with the specified damping ratio.
- [- initWithDampingRatio:initialVelocity:](<init(dampingratio_initialvelocity_).md>) — Creates a timing parameters object with the specified damping ratio and initial velocity.
- [- initWithCoder:](<init(coder_).md>) — Creates a timing parameters object from data in an unarchiver.
