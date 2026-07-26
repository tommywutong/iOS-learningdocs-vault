---
title: 'init(dampingRatio:)'
framework: UIKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, tvOS 10.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uispringtimingparameters/init(dampingratio:)'
source_url: 'https://developer.apple.com/documentation/uikit/uispringtimingparameters/init(dampingratio:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uispringtimingparameters/init%28dampingratio%3A%29.json'
content_hash: 'sha256:76b918e19a4cee90'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UISpringTimingParameters](../uispringtimingparameters.md)

# init(dampingRatio:)

<sub>Initializer</sub>

Creates a timing parameters object with the specified damping ratio.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
convenience init(dampingRatio ratio: CGFloat)
```

## Parameters

- `ratio` — The damping ratio for controlling the spring’s behavior. For more damping and less oscillation, specify a value of `1`. For less damping and more oscillation, specify values closer to `0`.

## Return Value

An initialized spring timing parameters object or `nil` if the object could not be created.

## Discussion

This method sets the initial velocity of any animated properties to `0.0`.

## See Also

### Initializing a spring timing parameters object

- [- init](<init().md>) — Creates a default timing parameters object.
- [- initWithDampingRatio:initialVelocity:](<init(dampingratio_initialvelocity_).md>) — Creates a timing parameters object with the specified damping ratio and initial velocity.
- [- initWithMass:stiffness:damping:initialVelocity:](<init(mass_stiffness_damping_initialvelocity_).md>) — Creates a timing parameters object with the specified spring stiffness, mass, damping coefficient, and initial velocity.
- [- initWithCoder:](<init(coder_).md>) — Creates a timing parameters object from data in an unarchiver.
