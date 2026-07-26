---
title: CATransform3D
framework: Core Animation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/quartzcore/catransform3d
source_url: 'https://developer.apple.com/documentation/quartzcore/catransform3d'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/catransform3d.json'
content_hash: 'sha256:d4abe5939a07e7c8'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Animation](../quartzcore.md)

# CATransform3D

<sub>Structure</sub>

The standard transform matrix used throughout Core Animation.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
struct CATransform3D
```

## Overview

The transform matrix is used to rotate, scale, translate, skew, and project the layer content. Functions are provided for creating, concatenating, and modifying CATransform3D data.

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Copyable](../swift/copyable.md), [Escapable](../swift/escapable.md), [Sendable](../swift/sendable.md)

## Topics

### Initializers

- [init()](<catransform3d/init().md>)
- [init(m11:m12:m13:m14:m21:m22:m23:m24:m31:m32:m33:m34:m41:m42:m43:m44:)](<catransform3d/init(m11_m12_m13_m14_m21_m22_m23_m24_m31_m32_m33_m34_m41_m42_m43_m44_).md>)
- [init(_:)](<catransform3d/init(__)-6awvy.md>)
- [init(_:)](<catransform3d/init(__)-6euzs.md>)

### Instance Properties

- [m11](catransform3d/m11.md) — The entry at position 1,1 in the matrix.
- [m12](catransform3d/m12.md) — The entry at position 1,2 in the matrix.
- [m13](catransform3d/m13.md) — The entry at position 1,3 in the matrix.
- [m14](catransform3d/m14.md) — The entry at position 1,4 in the matrix.
- [m21](catransform3d/m21.md) — The entry at position 2,1 in the matrix.
- [m22](catransform3d/m22.md) — The entry at position 2,2 in the matrix.
- [m23](catransform3d/m23.md) — The entry at position 2,3 in the matrix.
- [m24](catransform3d/m24.md) — The entry at position 2,4 in the matrix.
- [m31](catransform3d/m31.md) — The entry at position 3,1 in the matrix.
- [m32](catransform3d/m32.md) — The entry at position 3,2 in the matrix.
- [m33](catransform3d/m33.md) — The entry at position 3,3 in the matrix.
- [m34](catransform3d/m34.md) — The entry at position 3,4 in the matrix.
- [m41](catransform3d/m41.md) — The entry at position 4,1 in the matrix.
- [m42](catransform3d/m42.md) — The entry at position 4,2 in the matrix.
- [m43](catransform3d/m43.md) — The entry at position 4,3 in the matrix.
- [m44](catransform3d/m44.md) — The entry at position 4,4 in the matrix.

## See Also

### Constants

- [CAAutoresizingMask](caautoresizingmask.md) — These constants are used by the [autoresizingMask](calayer/autoresizingmask.md) property.
- [Action Identifiers](action-identifiers.md) — These constants are the predefined action identifiers used by [- actionForKey:](<calayer/action(forkey_).md>), [- addAnimation:forKey:](<calayer/add(__forkey_).md>), [+ defaultActionForKey:](<calayer/defaultaction(forkey_).md>), [- removeAnimationForKey:](<calayer/removeanimation(forkey_).md>), Layer Filters, and the [CAAction](caaction.md) protocol method [- runActionForKey:object:arguments:](<caaction/run(forkey_object_arguments_).md>).
- [CAEdgeAntialiasingMask](caedgeantialiasingmask.md) — This mask is used by the [edgeAntialiasingMask](calayer/edgeantialiasingmask.md) property.
- [Identity Transform](identity-transform.md) — Defines the identity transform matrix used by Core Animation.
- [Scaling Filters](scaling-filters.md) — These constants specify the scaling filters used by [magnificationFilter](calayer/magnificationfilter.md) and [minificationFilter](calayer/minificationfilter.md).
- [DynamicRange](calayer/dynamicrange.md)
