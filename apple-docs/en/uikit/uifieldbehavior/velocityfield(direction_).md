---
title: 'velocityField(direction:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uifieldbehavior/velocityfield(direction:)'
source_url: 'https://developer.apple.com/documentation/uikit/uifieldbehavior/velocityfield(direction:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uifieldbehavior/velocityfield%28direction%3A%29.json'
content_hash: 'sha256:46b762d8ddb88cc2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIFieldBehavior](../uifieldbehavior.md)

# velocityField(direction:)

<sub>Type Method</sub>

Creates and returns a field behavior object that applies a directional velocity to items.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
class func velocityField(direction: CGVector) -> Self
```

## Parameters

- `direction` — The vector indicating the direction of the velocity force. You can change this value later by modifying the [direction](direction.md) property.

## Return Value

A field behavior object that applies a velocity to items.

## Discussion

Velocity fields apply their velocity to the item, overriding any other acceleration forces currently on the item. The vector in the `direction` parameter is combined with the field [strength](strength.md) to determine the velocity of items in the field.

## See Also

### Getting the field behaviors

- [+ dragField](<dragfield().md>) — Creates and returns a field behavior for slowing an object’s velocity.
- [+ springField](<springfield().md>) — Creates and returns a spring field behavior.
- [+ electricField](<electricfield().md>) — Creates and returns a field behavior object that interacts with charged items.
- [+ magneticField](<magneticfield().md>) — Creates and returns a field behavior that interacts with charged items.
- [+ radialGravityFieldWithPosition:](<radialgravityfield(position_).md>) — Creates and returns a field behavior object that models a radial gravitational force.
- [+ linearGravityFieldWithVector:](<lineargravityfield(direction_).md>) — Creates and returns a field behavior object that models a linear gravitational force.
- [+ vortexField](<vortexfield().md>) — Creates and returns a field behavior object that applies a rotational force relative to the field’s position.
- [+ noiseFieldWithSmoothness:animationSpeed:](<noisefield(smoothness_animationspeed_).md>) — Creates and returns a field behavior object that applies random noise to other forces.
- [+ turbulenceFieldWithSmoothness:animationSpeed:](<turbulencefield(smoothness_animationspeed_).md>) — Creates and returns a field behavior object that applies noise to an item in motion.
- [+ fieldWithEvaluationBlock:](<field(evaluationblock_).md>) — Creates and returns a field behavior object that applies an app-specified field to items.
