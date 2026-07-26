---
title: 'constraintWithAttribute:relativeTo:attribute:scale:offset:'
framework: Core Animation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [Mac Catalyst 13.1+, macOS 10.5+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/quartzcore/caconstraint/constraintwithattribute:relativeto:attribute:scale:offset:'
source_url: 'https://developer.apple.com/documentation/quartzcore/caconstraint/constraintwithattribute:relativeto:attribute:scale:offset:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/caconstraint/constraintwithattribute%3Arelativeto%3Aattribute%3Ascale%3Aoffset%3A.json'
content_hash: 'sha256:e2001727afbdc64a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Animation](../../quartzcore.md) · [CAConstraint](../caconstraint.md)

# constraintWithAttribute:relativeTo:attribute:scale:offset:

<sub>Type Method</sub>

Creates and returns an `CAConstraint` object with the specified parameters.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
+ (instancetype) constraintWithAttribute:(CAConstraintAttribute) attr relativeTo:(NSString *) srcId attribute:(CAConstraintAttribute) srcAttr scale:(CGFloat) m offset:(CGFloat) c;
```

## Parameters

- `attr` — The attribute of the layer for which to create a new constraint.

- `srcId` — The name of the layer that this constraint is calculated relative to.

- `srcAttr` — The attribute of `srcLayer` the constraint is calculated relative to.

- `m` — The amount to scale the value of `srcAttr`.

- `c` — The offset from the `srcAttr`.

## Return Value

A new `CAConstraint` object with the specified parameters.

## Discussion

The value for the constraint is calculated as ((`srcAttr` * scale) + offset).

## See Also

### Related Documentation

- [Core Animation Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/CoreAnimation_guide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40004514)

### Create a New Constraint

- [+ constraintWithAttribute:relativeTo:attribute:offset:](<init(attribute_relativeto_attribute_offset_).md>) — Creates and returns an `CAConstraint` object with the specified parameters.
- [+ constraintWithAttribute:relativeTo:attribute:](<init(attribute_relativeto_attribute_).md>) — Creates and returns an `CAConstraint` object with the specified parameters.
- [- initWithAttribute:relativeTo:attribute:scale:offset:](<init(attribute_relativeto_attribute_scale_offset_).md>) — Returns an `CAConstraint` object with the specified parameters. Designated initializer.
