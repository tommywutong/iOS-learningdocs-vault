---
title: 'init(attribute:relativeTo:attribute:scale:offset:)'
framework: Core Animation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [Mac Catalyst 13.1+, macOS 10.5+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/quartzcore/caconstraint/init(attribute:relativeto:attribute:scale:offset:)'
source_url: 'https://developer.apple.com/documentation/quartzcore/caconstraint/init(attribute:relativeto:attribute:scale:offset:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/caconstraint/init%28attribute%3Arelativeto%3Aattribute%3Ascale%3Aoffset%3A%29.json'
content_hash: 'sha256:35c2b68aca272d12'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Animation](../../quartzcore.md) · [CAConstraint](../caconstraint.md)

# init(attribute:relativeTo:attribute:scale:offset:)

<sub>Initializer</sub>

Returns an `CAConstraint` object with the specified parameters. Designated initializer.

<sub>Mac Catalyst, macOS</sub>

```swift
init(attribute attr: CAConstraintAttribute, relativeTo srcId: String, attribute srcAttr: CAConstraintAttribute, scale m: CGFloat, offset c: CGFloat)
```

## Parameters

- `attr` — The attribute of the layer for which to create a new constraint.

- `srcId` — The name of the layer that this constraint is calculated relative to.

- `srcAttr` — The attribute of `srcLayer` the constraint is calculated relative to.

- `m` — The amount to scale the value of `srcAttr`.

- `c` — The offset added to the value of `srcAttr`.

## Return Value

An initialized constraint object using the specified parameters.

## Discussion

The value for the constraint is calculated as (`srcAttr` * `scale`) + `offset`).

## See Also

### Create a New Constraint

- [+ constraintWithAttribute:relativeTo:attribute:offset:](<init(attribute_relativeto_attribute_offset_).md>) — Creates and returns an `CAConstraint` object with the specified parameters.
- [+ constraintWithAttribute:relativeTo:attribute:](<init(attribute_relativeto_attribute_).md>) — Creates and returns an `CAConstraint` object with the specified parameters.
