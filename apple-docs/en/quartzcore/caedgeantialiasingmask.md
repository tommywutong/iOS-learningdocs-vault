---
title: CAEdgeAntialiasingMask
framework: Core Animation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/quartzcore/caedgeantialiasingmask
source_url: 'https://developer.apple.com/documentation/quartzcore/caedgeantialiasingmask'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/caedgeantialiasingmask.json'
content_hash: 'sha256:c66ece2cb7c8ac97'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Animation](../quartzcore.md)

# CAEdgeAntialiasingMask

<sub>Structure</sub>

This mask is used by the [edgeAntialiasingMask](calayer/edgeantialiasingmask.md) property.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
struct CAEdgeAntialiasingMask
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [ExpressibleByArrayLiteral](../swift/expressiblebyarrayliteral.md), [OptionSet](../swift/optionset.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [SetAlgebra](../swift/setalgebra.md)

## Topics

### Constants

- [init(rawValue:)](<caedgeantialiasingmask/init(rawvalue_).md>)
- [kCALayerLeftEdge](caedgeantialiasingmask/layerleftedge.md)
- [kCALayerRightEdge](caedgeantialiasingmask/layerrightedge.md)
- [kCALayerBottomEdge](caedgeantialiasingmask/layerbottomedge.md)
- [kCALayerTopEdge](caedgeantialiasingmask/layertopedge.md)

## See Also

### Constants

- [CAAutoresizingMask](caautoresizingmask.md) — These constants are used by the [autoresizingMask](calayer/autoresizingmask.md) property.
- [Action Identifiers](action-identifiers.md) — These constants are the predefined action identifiers used by [- actionForKey:](<calayer/action(forkey_).md>), [- addAnimation:forKey:](<calayer/add(__forkey_).md>), [+ defaultActionForKey:](<calayer/defaultaction(forkey_).md>), [- removeAnimationForKey:](<calayer/removeanimation(forkey_).md>), Layer Filters, and the [CAAction](caaction.md) protocol method [- runActionForKey:object:arguments:](<caaction/run(forkey_object_arguments_).md>).
- [Identity Transform](identity-transform.md) — Defines the identity transform matrix used by Core Animation.
- [Scaling Filters](scaling-filters.md) — These constants specify the scaling filters used by [magnificationFilter](calayer/magnificationfilter.md) and [minificationFilter](calayer/minificationfilter.md).
- [CATransform3D](catransform3d.md) — The standard transform matrix used throughout Core Animation.
- [DynamicRange](calayer/dynamicrange.md)
