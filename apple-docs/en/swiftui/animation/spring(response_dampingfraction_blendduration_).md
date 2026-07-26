---
title: 'spring(response:dampingFraction:blendDuration:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/animation/spring(response:dampingfraction:blendduration:)'
source_url: 'https://developer.apple.com/documentation/swiftui/animation/spring(response:dampingfraction:blendduration:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/animation/spring%28response%3Adampingfraction%3Ablendduration%3A%29.json'
content_hash: 'sha256:c83dcdfe81af7431'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Animation](../animation.md)

# spring(response:dampingFraction:blendDuration:)

<sub>Type Method</sub>

A persistent spring animation. When mixed with other `spring()` or `interactiveSpring()` animations on the same property, each animation will be replaced by their successor, preserving velocity from one animation to the next. Optionally blends the response values between springs over a time period.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func spring(response: Double = 0.5, dampingFraction: Double = 0.825, blendDuration: TimeInterval = 0) -> Animation
```

## Parameters

- `response` — The stiffness of the spring, defined as an approximate duration in seconds. A value of zero requests an infinitely-stiff spring, suitable for driving interactive animations.

- `dampingFraction` — The amount of drag applied to the value being animated, as a fraction of an estimate of amount needed to produce critical damping.

- `blendDuration` — The duration in seconds over which to interpolate changes to the response value of the spring.

## Return Value

A spring animation.

## See Also

### Customizing spring animations

- [spring](spring.md) — A persistent spring animation. When mixed with other `spring()` or `interactiveSpring()` animations on the same property, each animation will be replaced by their successor, preserving velocity from one animation to the next. Optionally blends the response values between springs over a time period.
- [spring(_:blendDuration:)](<spring(__blendduration_).md>) — A persistent spring animation.
- [spring(duration:bounce:blendDuration:)](<spring(duration_bounce_blendduration_).md>) — A persistent spring animation. When mixed with other `spring()` or `interactiveSpring()` animations on the same property, each animation will be replaced by their successor, preserving velocity from one animation to the next. Optionally blends the duration values between springs over a time period.
- [interactiveSpring](interactivespring.md) — A convenience for a `spring` animation with a lower `duration` value, intended for driving interactive animations.
- [interactiveSpring(response:dampingFraction:blendDuration:)](<interactivespring(response_dampingfraction_blendduration_).md>) — A convenience for a `spring` animation with a lower `response` value, intended for driving interactive animations.
- [interpolatingSpring](interpolatingspring.md) — An interpolating spring animation that uses a damped spring model to produce values in the range [0, 1] that are then used to interpolate within the [from, to] range of the animated property. Preserves velocity across overlapping animations by adding the effects of each animation.
- [interpolatingSpring(_:initialVelocity:)](<interpolatingspring(__initialvelocity_).md>) — An interpolating spring animation that uses a damped spring model to produce values in the range of one to zero.
- [interpolatingSpring(duration:bounce:initialVelocity:)](<interpolatingspring(duration_bounce_initialvelocity_).md>) — An interpolating spring animation that uses a damped spring model to produce values in the range [0, 1] that are then used to interpolate within the [from, to] range of the animated property. Preserves velocity across overlapping animations by adding the effects of each animation.
- [interpolatingSpring(mass:stiffness:damping:initialVelocity:)](<interpolatingspring(mass_stiffness_damping_initialvelocity_).md>) — An interpolating spring animation that uses a damped spring model to produce values in the range [0, 1] that are then used to interpolate within the [from, to] range of the animated property. Preserves velocity across overlapping animations by adding the effects of each animation.
