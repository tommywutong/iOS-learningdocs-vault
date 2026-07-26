---
title: magneticField()
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uifieldbehavior/magneticfield()
source_url: 'https://developer.apple.com/documentation/uikit/uifieldbehavior/magneticfield()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uifieldbehavior/magneticfield%28%29.json'
content_hash: 'sha256:5dfaade59048c571'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIFieldBehavior](../uifieldbehavior.md)

# magneticField()

<sub>Type Method</sub>

Creates and returns a field behavior that interacts with charged items.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
class func magneticField() -> Self
```

## Return Value

A field behavior object that applies a magnetic field to charged items.

## Discussion

The magnetic field behavior models a uniform magnetic field in the positive-z direction—that is, coming out of the screen. The amount of force applied by the field is modeled after the second part of the Lorentz equation (`F = qvB`). When the velocity of a charged item is perpendicular to the uniform magnetic field, the item feels a force normal to both the velocity and the field, resulting in a counter-clockwise rotation. Specifying a negative value for the [strength](strength.md) of the field results in a clockwise rotation.

You can use magnetic fields as a way to apply forces to an object that are based on charge instead of mass.

## See Also

### Getting the field behaviors

- [+ dragField](<dragfield().md>) — Creates and returns a field behavior for slowing an object’s velocity.
- [+ springField](<springfield().md>) — Creates and returns a spring field behavior.
- [+ velocityFieldWithVector:](<velocityfield(direction_).md>) — Creates and returns a field behavior object that applies a directional velocity to items.
- [+ electricField](<electricfield().md>) — Creates and returns a field behavior object that interacts with charged items.
- [+ radialGravityFieldWithPosition:](<radialgravityfield(position_).md>) — Creates and returns a field behavior object that models a radial gravitational force.
- [+ linearGravityFieldWithVector:](<lineargravityfield(direction_).md>) — Creates and returns a field behavior object that models a linear gravitational force.
- [+ vortexField](<vortexfield().md>) — Creates and returns a field behavior object that applies a rotational force relative to the field’s position.
- [+ noiseFieldWithSmoothness:animationSpeed:](<noisefield(smoothness_animationspeed_).md>) — Creates and returns a field behavior object that applies random noise to other forces.
- [+ turbulenceFieldWithSmoothness:animationSpeed:](<turbulencefield(smoothness_animationspeed_).md>) — Creates and returns a field behavior object that applies noise to an item in motion.
- [+ fieldWithEvaluationBlock:](<field(evaluationblock_).md>) — Creates and returns a field behavior object that applies an app-specified field to items.
