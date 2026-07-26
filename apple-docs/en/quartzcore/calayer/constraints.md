---
title: constraints
framework: Core Animation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [Mac Catalyst 13.1+, macOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/quartzcore/calayer/constraints
source_url: 'https://developer.apple.com/documentation/quartzcore/calayer/constraints'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/calayer/constraints.json'
content_hash: 'sha256:428aae54ec4ad8ed'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Animation](../../quartzcore.md) · [CALayer](../calayer.md)

# constraints

<sub>Instance Property</sub>

The constraints used to position current layer’s sublayers.

<sub>Mac Catalyst, macOS</sub>

```swift
var constraints: [CAConstraint]? { get set }
```

## Discussion

macOS apps can use this property to access their layer-based constraints. Before constraints can be applied, you must also assign a [CAConstraintLayoutManager](../caconstraintlayoutmanager.md) object to the [layoutManager](layoutmanager.md) property of the layer.

iOS apps do not support layer-based constraints.

## See Also

### Managing layer constraints

- [- addConstraint:](<addconstraint(__).md>) — Adds the specified constraint to the layer.
