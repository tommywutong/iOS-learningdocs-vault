---
title: Action Identifiers
framework: Core Animation
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/quartzcore/action-identifiers
source_url: 'https://developer.apple.com/documentation/quartzcore/action-identifiers'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/action-identifiers.json'
content_hash: 'sha256:667b781152ae1672'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Animation](../quartzcore.md) · [CALayer](calayer.md)

# Action Identifiers

<sub>API Collection</sub>

These constants are the predefined action identifiers used by [- actionForKey:](<calayer/action(forkey_).md>), [- addAnimation:forKey:](<calayer/add(__forkey_).md>), [+ defaultActionForKey:](<calayer/defaultaction(forkey_).md>), [- removeAnimationForKey:](<calayer/removeanimation(forkey_).md>), Layer Filters, and the [CAAction](caaction.md) protocol method [- runActionForKey:object:arguments:](<caaction/run(forkey_object_arguments_).md>).

## Topics

### Constants

- [kCAOnOrderIn](kcaonorderin.md) — The identifier that represents the action taken when a layer becomes visible, either as a result being inserted into the visible layer hierarchy or the layer is no longer set as hidden.
- [kCAOnOrderOut](kcaonorderout.md) — The identifier that represents the action taken when the layer is removed from the layer hierarchy or is hidden.
- [kCATransition](kcatransition.md) — The identifier that represents a transition animation.

## See Also

### Constants

- [CAAutoresizingMask](caautoresizingmask.md) — These constants are used by the [autoresizingMask](calayer/autoresizingmask.md) property.
- [CAEdgeAntialiasingMask](caedgeantialiasingmask.md) — This mask is used by the [edgeAntialiasingMask](calayer/edgeantialiasingmask.md) property.
- [Identity Transform](identity-transform.md) — Defines the identity transform matrix used by Core Animation.
- [Scaling Filters](scaling-filters.md) — These constants specify the scaling filters used by [magnificationFilter](calayer/magnificationfilter.md) and [minificationFilter](calayer/minificationfilter.md).
- [CATransform3D](catransform3d.md) — The standard transform matrix used throughout Core Animation.
- [DynamicRange](calayer/dynamicrange.md)
