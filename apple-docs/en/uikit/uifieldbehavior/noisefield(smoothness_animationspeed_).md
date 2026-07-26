---
title: 'noiseField(smoothness:animationSpeed:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uifieldbehavior/noisefield(smoothness:animationspeed:)'
source_url: 'https://developer.apple.com/documentation/uikit/uifieldbehavior/noisefield(smoothness:animationspeed:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uifieldbehavior/noisefield%28smoothness%3Aanimationspeed%3A%29.json'
content_hash: 'sha256:942d5b62ee40ec28'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIFieldBehavior](../uifieldbehavior.md)

# noiseField(smoothness:animationSpeed:)

<sub>Type Method</sub>

Creates and returns a field behavior object that applies random noise to other forces.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
class func noiseField(smoothness: CGFloat, animationSpeed speed: CGFloat) -> Self
```

## Parameters

- `smoothness` — The smoothness of the field. Specify a value between `0.0` and `1.0`, where `0.0` indicates the maximum amount of randomness in the generated field and `1.0` indicates the least amount of randomness.

- `speed` — The frequency at which the noise field changes, measured in Hertz (Hz). Specify `0.0` to create a noise field that does not change over time.

## Return Value

A field behavior object that applies noise to other fields in the same area.

## Discussion

A noise field creates a differentiable Perlin simplex noise field that varies over time. You can combine a noise field with other fields to add some variability to the behavior of those fields. The smoothness of the field defines how random the changes are from one point to the next point. A smooth field still adds noise but does so in a more predictable way. This field ignores the mass of the item.

## See Also

### Getting the field behaviors

- [+ dragField](<dragfield().md>) — Creates and returns a field behavior for slowing an object’s velocity.
- [+ springField](<springfield().md>) — Creates and returns a spring field behavior.
- [+ velocityFieldWithVector:](<velocityfield(direction_).md>) — Creates and returns a field behavior object that applies a directional velocity to items.
- [+ electricField](<electricfield().md>) — Creates and returns a field behavior object that interacts with charged items.
- [+ magneticField](<magneticfield().md>) — Creates and returns a field behavior that interacts with charged items.
- [+ radialGravityFieldWithPosition:](<radialgravityfield(position_).md>) — Creates and returns a field behavior object that models a radial gravitational force.
- [+ linearGravityFieldWithVector:](<lineargravityfield(direction_).md>) — Creates and returns a field behavior object that models a linear gravitational force.
- [+ vortexField](<vortexfield().md>) — Creates and returns a field behavior object that applies a rotational force relative to the field’s position.
- [+ turbulenceFieldWithSmoothness:animationSpeed:](<turbulencefield(smoothness_animationspeed_).md>) — Creates and returns a field behavior object that applies noise to an item in motion.
- [+ fieldWithEvaluationBlock:](<field(evaluationblock_).md>) — Creates and returns a field behavior object that applies an app-specified field to items.
