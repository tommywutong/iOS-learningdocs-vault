---
title: CAAutoresizingMask
framework: Core Animation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [Mac Catalyst 13.1+, macOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/quartzcore/caautoresizingmask
source_url: 'https://developer.apple.com/documentation/quartzcore/caautoresizingmask'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/caautoresizingmask.json'
content_hash: 'sha256:1dfde178769d4b34'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Animation](../quartzcore.md)

# CAAutoresizingMask

<sub>Structure</sub>

These constants are used by the [autoresizingMask](calayer/autoresizingmask.md) property.

<sub>Mac Catalyst, macOS</sub>

```swift
struct CAAutoresizingMask
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [ExpressibleByArrayLiteral](../swift/expressiblebyarrayliteral.md), [OptionSet](../swift/optionset.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [SetAlgebra](../swift/setalgebra.md)

## Topics

### Constants

- [init(rawValue:)](<caautoresizingmask/init(rawvalue_).md>)
- [kCALayerMinXMargin](caautoresizingmask/layerminxmargin.md) — The left margin between the receiver and its superview is flexible.
- [kCALayerWidthSizable](caautoresizingmask/layerwidthsizable.md) — The receiver’s width is flexible.
- [kCALayerMaxXMargin](caautoresizingmask/layermaxxmargin.md) — The right margin between the receiver and its superview is flexible.
- [kCALayerMinYMargin](caautoresizingmask/layerminymargin.md) — The bottom margin between the receiver and its superview is flexible.
- [kCALayerHeightSizable](caautoresizingmask/layerheightsizable.md) — The receiver’s height is flexible.
- [kCALayerMaxYMargin](caautoresizingmask/layermaxymargin.md) — The top margin between the receiver and its superview is flexible.

## See Also

### Constants

- [Action Identifiers](action-identifiers.md) — These constants are the predefined action identifiers used by [- actionForKey:](<calayer/action(forkey_).md>), [- addAnimation:forKey:](<calayer/add(__forkey_).md>), [+ defaultActionForKey:](<calayer/defaultaction(forkey_).md>), [- removeAnimationForKey:](<calayer/removeanimation(forkey_).md>), Layer Filters, and the [CAAction](caaction.md) protocol method [- runActionForKey:object:arguments:](<caaction/run(forkey_object_arguments_).md>).
- [CAEdgeAntialiasingMask](caedgeantialiasingmask.md) — This mask is used by the [edgeAntialiasingMask](calayer/edgeantialiasingmask.md) property.
- [Identity Transform](identity-transform.md) — Defines the identity transform matrix used by Core Animation.
- [Scaling Filters](scaling-filters.md) — These constants specify the scaling filters used by [magnificationFilter](calayer/magnificationfilter.md) and [minificationFilter](calayer/minificationfilter.md).
- [CATransform3D](catransform3d.md) — The standard transform matrix used throughout Core Animation.
- [DynamicRange](calayer/dynamicrange.md)
