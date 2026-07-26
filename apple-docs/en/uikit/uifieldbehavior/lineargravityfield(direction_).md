---
title: 'linearGravityField(direction:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uifieldbehavior/lineargravityfield(direction:)'
source_url: 'https://developer.apple.com/documentation/uikit/uifieldbehavior/lineargravityfield(direction:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uifieldbehavior/lineargravityfield%28direction%3A%29.json'
content_hash: 'sha256:b0473698497090f1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIFieldBehavior](../uifieldbehavior.md)

# linearGravityField(direction:)

<sub>Type Method</sub>

Creates and returns a field behavior object that models a linear gravitational force.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
class func linearGravityField(direction: CGVector) -> Self
```

## Parameters

- `direction` — The vector indicating the direction of the gravitational force. You can change this value later by modifying the [direction](direction.md) property.

## Return Value

A field behavior object that applies a directional gravitation force to items with mass.

## Discussion

This field creates a directional gravitational force that applies uniformly to all dynamic items with mass. When setting the [strength](strength.md) of the field, positive values attract items in the direction of the vector and negative values repel items. The force on a given item can be determined by the equation `F = ma`, where force equals the mass of the item multiplied by the acceleration imposed by the gravitational field, which with this type of field is constant.

## See Also

### Getting the field behaviors

- [+ dragField](<dragfield().md>) — Creates and returns a field behavior for slowing an object’s velocity.
- [+ springField](<springfield().md>) — Creates and returns a spring field behavior.
- [+ velocityFieldWithVector:](<velocityfield(direction_).md>) — Creates and returns a field behavior object that applies a directional velocity to items.
- [+ electricField](<electricfield().md>) — Creates and returns a field behavior object that interacts with charged items.
- [+ magneticField](<magneticfield().md>) — Creates and returns a field behavior that interacts with charged items.
- [+ radialGravityFieldWithPosition:](<radialgravityfield(position_).md>) — Creates and returns a field behavior object that models a radial gravitational force.
- [+ vortexField](<vortexfield().md>) — Creates and returns a field behavior object that applies a rotational force relative to the field’s position.
- [+ noiseFieldWithSmoothness:animationSpeed:](<noisefield(smoothness_animationspeed_).md>) — Creates and returns a field behavior object that applies random noise to other forces.
- [+ turbulenceFieldWithSmoothness:animationSpeed:](<turbulencefield(smoothness_animationspeed_).md>) — Creates and returns a field behavior object that applies noise to an item in motion.
- [+ fieldWithEvaluationBlock:](<field(evaluationblock_).md>) — Creates and returns a field behavior object that applies an app-specified field to items.
