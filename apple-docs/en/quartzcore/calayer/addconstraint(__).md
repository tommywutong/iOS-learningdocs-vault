---
title: 'addConstraint(_:)'
framework: Core Animation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [Mac Catalyst 13.1+, macOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/quartzcore/calayer/addconstraint(_:)'
source_url: 'https://developer.apple.com/documentation/quartzcore/calayer/addconstraint(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/calayer/addconstraint%28_%3A%29.json'
content_hash: 'sha256:ceeef0708819610f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Animation](../../quartzcore.md) · [CALayer](../calayer.md)

# addConstraint(_:)

<sub>Instance Method</sub>

Adds the specified constraint to the layer.

<sub>Mac Catalyst, macOS</sub>

```swift
func addConstraint(_ c: CAConstraint)
```

## Parameters

- `c` — The constraint object to add to the receiver’s array of constraint objects.

## Discussion

In macOS, you typically add constraints to a layer to manage the size and position of that layer’s sublayers. Before constraints can be applied, you must also assign a [CAConstraintLayoutManager](../caconstraintlayoutmanager.md) object to the [layoutManager](layoutmanager.md) property of the layer. For more information about managing layer-based constraints, see [Core Animation Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/CoreAnimation_guide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40004514).

iOS apps do not support layer-based constraints.

## See Also

### Managing layer constraints

- [constraints](constraints.md) — The constraints used to position current layer’s sublayers.
