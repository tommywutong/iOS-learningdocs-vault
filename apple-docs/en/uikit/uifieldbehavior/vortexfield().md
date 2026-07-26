---
title: vortexField()
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uifieldbehavior/vortexfield()
source_url: 'https://developer.apple.com/documentation/uikit/uifieldbehavior/vortexfield()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uifieldbehavior/vortexfield%28%29.json'
content_hash: 'sha256:e6001d32808f25f1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIFieldBehavior](../uifieldbehavior.md)

# vortexField()

<sub>Type Method</sub>

Creates and returns a field behavior object that applies a rotational force relative to the field’s position.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
class func vortexField() -> Self
```

## Return Value

A field behavior object that applies a rotational force around the field’s origin.

## Discussion

This forces created by this field rotate in a circle around the center point of the field. Items entering the field are pushed perpendicular to the imaginary line between the item and the center of the field. Combine this field with a radial gravity field to create a field that pulls items into a spinning vortex.

When setting the [strength](strength.md) of the vortex field, positive values create a counter-clockwise rotation and negative values create a clockwise rotation. The amount of force is proportional to the item’s mass and the item’s distance from the field’s origin.

## See Also

### Getting the field behaviors

- [+ dragField](<dragfield().md>) — Creates and returns a field behavior for slowing an object’s velocity.
- [+ springField](<springfield().md>) — Creates and returns a spring field behavior.
- [+ velocityFieldWithVector:](<velocityfield(direction_).md>) — Creates and returns a field behavior object that applies a directional velocity to items.
- [+ electricField](<electricfield().md>) — Creates and returns a field behavior object that interacts with charged items.
- [+ magneticField](<magneticfield().md>) — Creates and returns a field behavior that interacts with charged items.
- [+ radialGravityFieldWithPosition:](<radialgravityfield(position_).md>) — Creates and returns a field behavior object that models a radial gravitational force.
- [+ linearGravityFieldWithVector:](<lineargravityfield(direction_).md>) — Creates and returns a field behavior object that models a linear gravitational force.
- [+ noiseFieldWithSmoothness:animationSpeed:](<noisefield(smoothness_animationspeed_).md>) — Creates and returns a field behavior object that applies random noise to other forces.
- [+ turbulenceFieldWithSmoothness:animationSpeed:](<turbulencefield(smoothness_animationspeed_).md>) — Creates and returns a field behavior object that applies noise to an item in motion.
- [+ fieldWithEvaluationBlock:](<field(evaluationblock_).md>) — Creates and returns a field behavior object that applies an app-specified field to items.
