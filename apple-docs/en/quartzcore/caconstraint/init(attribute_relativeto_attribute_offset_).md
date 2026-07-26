---
title: 'init(attribute:relativeTo:attribute:offset:)'
framework: Core Animation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [Mac Catalyst 13.1+, macOS 10.5+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/quartzcore/caconstraint/init(attribute:relativeto:attribute:offset:)'
source_url: 'https://developer.apple.com/documentation/quartzcore/caconstraint/init(attribute:relativeto:attribute:offset:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/caconstraint/init%28attribute%3Arelativeto%3Aattribute%3Aoffset%3A%29.json'
content_hash: 'sha256:8d2d03af5d4d80db'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Animation](../../quartzcore.md) · [CAConstraint](../caconstraint.md)

# init(attribute:relativeTo:attribute:offset:)

<sub>Initializer</sub>

Creates and returns an `CAConstraint` object with the specified parameters.

<sub>Mac Catalyst, macOS</sub>

```swift
convenience init(attribute attr: CAConstraintAttribute, relativeTo srcId: String, attribute srcAttr: CAConstraintAttribute, offset c: CGFloat)
```

## Parameters

- `attr` — The attribute of the layer for which to create a new constraint.

- `srcId` — The name of the layer that this constraint is calculated relative to.

- `srcAttr` — The attribute of `srcLayer` the constraint is calculated relative to.

- `c` — The offset added to the value of `srcAttr`.

## Return Value

A new `CAConstraint` object with the specified parameters. The scale of the constraint is set to 1.0.

## Discussion

The value for the constraint is calculated as (`srcAttr` + `offset`).

## See Also

### Create a New Constraint

- [+ constraintWithAttribute:relativeTo:attribute:](<init(attribute_relativeto_attribute_).md>) — Creates and returns an `CAConstraint` object with the specified parameters.
- [- initWithAttribute:relativeTo:attribute:scale:offset:](<init(attribute_relativeto_attribute_scale_offset_).md>) — Returns an `CAConstraint` object with the specified parameters. Designated initializer.
