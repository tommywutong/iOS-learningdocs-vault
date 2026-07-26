---
title: 'init(attribute:relativeTo:attribute:)'
framework: Core Animation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [Mac Catalyst 13.1+, macOS 10.5+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/quartzcore/caconstraint/init(attribute:relativeto:attribute:)'
source_url: 'https://developer.apple.com/documentation/quartzcore/caconstraint/init(attribute:relativeto:attribute:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/caconstraint/init%28attribute%3Arelativeto%3Aattribute%3A%29.json'
content_hash: 'sha256:ef9a70b23fc8816e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Animation](../../quartzcore.md) · [CAConstraint](../caconstraint.md)

# init(attribute:relativeTo:attribute:)

<sub>Initializer</sub>

Creates and returns an `CAConstraint` object with the specified parameters.

<sub>Mac Catalyst, macOS</sub>

```swift
convenience init(attribute attr: CAConstraintAttribute, relativeTo srcId: String, attribute srcAttr: CAConstraintAttribute)
```

## Parameters

- `attr` — The attribute of the layer for which to create a new constraint.

- `srcId` — The name of the layer that this constraint is calculated relative to.

- `srcAttr` — The attribute of `srcLayer` the constraint is calculated relative to.

## Return Value

A new `CAConstraint` object with the specified parameters. The scale of the constraint is set to 1.0. The offset of the constraint is set to 0.0.

## Discussion

The value for the constraint is calculated is `srcAttr`.

## See Also

### Create a New Constraint

- [+ constraintWithAttribute:relativeTo:attribute:offset:](<init(attribute_relativeto_attribute_offset_).md>) — Creates and returns an `CAConstraint` object with the specified parameters.
- [- initWithAttribute:relativeTo:attribute:scale:offset:](<init(attribute_relativeto_attribute_scale_offset_).md>) — Returns an `CAConstraint` object with the specified parameters. Designated initializer.
