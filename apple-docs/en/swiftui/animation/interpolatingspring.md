---
title: interpolatingSpring
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/animation/interpolatingspring
source_url: 'https://developer.apple.com/documentation/swiftui/animation/interpolatingspring'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/animation/interpolatingspring.json'
content_hash: 'sha256:919d12be18ba4393'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Animation](../animation.md)

# interpolatingSpring

<sub>Type Property</sub>

An interpolating spring animation that uses a damped spring model to produce values in the range [0, 1] that are then used to interpolate within the [from, to] range of the animated property. Preserves velocity across overlapping animations by adding the effects of each animation.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@export(implementation) static var interpolatingSpring: Animation { get }
```

## Discussion

This uses the default parameter values.

## See Also

### Customizing spring animations

- [spring](spring.md) — A persistent spring animation. When mixed with other `spring()` or `interactiveSpring()` animations on the same property, each animation will be replaced by their successor, preserving velocity from one animation to the next. Optionally blends the response values between springs over a time period.
- [spring(_:blendDuration:)](<spring(__blendduration_).md>) — A persistent spring animation.
- [spring(duration:bounce:blendDuration:)](<spring(duration_bounce_blendduration_).md>) — A persistent spring animation. When mixed with other `spring()` or `interactiveSpring()` animations on the same property, each animation will be replaced by their successor, preserving velocity from one animation to the next. Optionally blends the duration values between springs over a time period.
- [spring(response:dampingFraction:blendDuration:)](<spring(response_dampingfraction_blendduration_).md>) — A persistent spring animation. When mixed with other `spring()` or `interactiveSpring()` animations on the same property, each animation will be replaced by their successor, preserving velocity from one animation to the next. Optionally blends the response values between springs over a time period.
- [interactiveSpring](interactivespring.md) — A convenience for a `spring` animation with a lower `duration` value, intended for driving interactive animations.
- [interactiveSpring(response:dampingFraction:blendDuration:)](<interactivespring(response_dampingfraction_blendduration_).md>) — A convenience for a `spring` animation with a lower `response` value, intended for driving interactive animations.
- [interpolatingSpring(_:initialVelocity:)](<interpolatingspring(__initialvelocity_).md>) — An interpolating spring animation that uses a damped spring model to produce values in the range of one to zero.
- [interpolatingSpring(duration:bounce:initialVelocity:)](<interpolatingspring(duration_bounce_initialvelocity_).md>) — An interpolating spring animation that uses a damped spring model to produce values in the range [0, 1] that are then used to interpolate within the [from, to] range of the animated property. Preserves velocity across overlapping animations by adding the effects of each animation.
- [interpolatingSpring(mass:stiffness:damping:initialVelocity:)](<interpolatingspring(mass_stiffness_damping_initialvelocity_).md>) — An interpolating spring animation that uses a damped spring model to produce values in the range [0, 1] that are then used to interpolate within the [from, to] range of the animated property. Preserves velocity across overlapping animations by adding the effects of each animation.
