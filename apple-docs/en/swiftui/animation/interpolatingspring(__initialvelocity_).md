---
title: 'interpolatingSpring(_:initialVelocity:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/animation/interpolatingspring(_:initialvelocity:)'
source_url: 'https://developer.apple.com/documentation/swiftui/animation/interpolatingspring(_:initialvelocity:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/animation/interpolatingspring%28_%3Ainitialvelocity%3A%29.json'
content_hash: 'sha256:50913f3d4afd2c4c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Animation](../animation.md)

# interpolatingSpring(_:initialVelocity:)

<sub>Type Method</sub>

An interpolating spring animation that uses a damped spring model to produce values in the range of one to zero.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func interpolatingSpring(_ spring: Spring, initialVelocity: Double = 0.0) -> Animation
```

## Discussion

These vales are used to interpolate within the `[from, to]` range of the animated property. Preserves velocity across overlapping animations by adding the effects of each animation.

## See Also

### Customizing spring animations

- [spring](spring.md) — A persistent spring animation. When mixed with other `spring()` or `interactiveSpring()` animations on the same property, each animation will be replaced by their successor, preserving velocity from one animation to the next. Optionally blends the response values between springs over a time period.
- [spring(_:blendDuration:)](<spring(__blendduration_).md>) — A persistent spring animation.
- [spring(duration:bounce:blendDuration:)](<spring(duration_bounce_blendduration_).md>) — A persistent spring animation. When mixed with other `spring()` or `interactiveSpring()` animations on the same property, each animation will be replaced by their successor, preserving velocity from one animation to the next. Optionally blends the duration values between springs over a time period.
- [spring(response:dampingFraction:blendDuration:)](<spring(response_dampingfraction_blendduration_).md>) — A persistent spring animation. When mixed with other `spring()` or `interactiveSpring()` animations on the same property, each animation will be replaced by their successor, preserving velocity from one animation to the next. Optionally blends the response values between springs over a time period.
- [interactiveSpring](interactivespring.md) — A convenience for a `spring` animation with a lower `duration` value, intended for driving interactive animations.
- [interactiveSpring(response:dampingFraction:blendDuration:)](<interactivespring(response_dampingfraction_blendduration_).md>) — A convenience for a `spring` animation with a lower `response` value, intended for driving interactive animations.
- [interpolatingSpring](interpolatingspring.md) — An interpolating spring animation that uses a damped spring model to produce values in the range [0, 1] that are then used to interpolate within the [from, to] range of the animated property. Preserves velocity across overlapping animations by adding the effects of each animation.
- [interpolatingSpring(duration:bounce:initialVelocity:)](<interpolatingspring(duration_bounce_initialvelocity_).md>) — An interpolating spring animation that uses a damped spring model to produce values in the range [0, 1] that are then used to interpolate within the [from, to] range of the animated property. Preserves velocity across overlapping animations by adding the effects of each animation.
- [interpolatingSpring(mass:stiffness:damping:initialVelocity:)](<interpolatingspring(mass_stiffness_damping_initialvelocity_).md>) — An interpolating spring animation that uses a damped spring model to produce values in the range [0, 1] that are then used to interpolate within the [from, to] range of the animated property. Preserves velocity across overlapping animations by adding the effects of each animation.
