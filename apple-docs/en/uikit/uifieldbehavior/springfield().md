---
title: springField()
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uifieldbehavior/springfield()
source_url: 'https://developer.apple.com/documentation/uikit/uifieldbehavior/springfield()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uifieldbehavior/springfield%28%29.json'
content_hash: 'sha256:3e1f5b30e4ffa9b1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIFieldBehavior](../uifieldbehavior.md)

# springField()

<sub>Type Method</sub>

Creates and returns a spring field behavior.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
class func springField() -> Self
```

## Return Value

A field behavior object that applies spring effects to items.

## Discussion

A spring field behavior object uses Hooke’s law to calculate the force applied to objects in the field. With this law, the amount of force is linearly proportional to the distance from the center of the field. An item entering this field oscillates with a period proportional to the inverse of its density. You can use this field behavior to keep items confined to a particular region. Use the item’s resistance to reduce its linear velocity (and thus the amount of oscillation) over time.

An item in a spring field oscillates continuously unless the spring forces are damped by friction or the item is affected by other fields.

## See Also

### Getting the field behaviors

- [+ dragField](<dragfield().md>) — Creates and returns a field behavior for slowing an object’s velocity.
- [+ velocityFieldWithVector:](<velocityfield(direction_).md>) — Creates and returns a field behavior object that applies a directional velocity to items.
- [+ electricField](<electricfield().md>) — Creates and returns a field behavior object that interacts with charged items.
- [+ magneticField](<magneticfield().md>) — Creates and returns a field behavior that interacts with charged items.
- [+ radialGravityFieldWithPosition:](<radialgravityfield(position_).md>) — Creates and returns a field behavior object that models a radial gravitational force.
- [+ linearGravityFieldWithVector:](<lineargravityfield(direction_).md>) — Creates and returns a field behavior object that models a linear gravitational force.
- [+ vortexField](<vortexfield().md>) — Creates and returns a field behavior object that applies a rotational force relative to the field’s position.
- [+ noiseFieldWithSmoothness:animationSpeed:](<noisefield(smoothness_animationspeed_).md>) — Creates and returns a field behavior object that applies random noise to other forces.
- [+ turbulenceFieldWithSmoothness:animationSpeed:](<turbulencefield(smoothness_animationspeed_).md>) — Creates and returns a field behavior object that applies noise to an item in motion.
- [+ fieldWithEvaluationBlock:](<field(evaluationblock_).md>) — Creates and returns a field behavior object that applies an app-specified field to items.
