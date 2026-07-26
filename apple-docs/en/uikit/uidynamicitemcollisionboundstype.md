---
title: UIDynamicItemCollisionBoundsType
framework: UIKit
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uidynamicitemcollisionboundstype
source_url: 'https://developer.apple.com/documentation/uikit/uidynamicitemcollisionboundstype'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uidynamicitemcollisionboundstype.json'
content_hash: 'sha256:bc454f4400f21c33'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIDynamicItemCollisionBoundsType

<sub>Enumeration</sub>

Constants that indicate the shape of the item’s collision bounds.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
enum UIDynamicItemCollisionBoundsType
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Constants

- [UIDynamicItemCollisionBoundsTypeRectangle](uidynamicitemcollisionboundstype/rectangle.md) — Rectangular collision bounds.
- [UIDynamicItemCollisionBoundsTypeEllipse](uidynamicitemcollisionboundstype/ellipse.md) — Elliptical collision bounds. The shape of the ellipse is determined by the width and height of the item’s [bounds](uidynamicitem/bounds.md) property.
- [UIDynamicItemCollisionBoundsTypePath](uidynamicitemcollisionboundstype/path.md) — Path-based collision bounds. For this type, the shape is a [UIBezierPath](uibezierpath.md) object stored in the item’s [collisionBoundingPath](uidynamicitem/collisionboundingpath.md) property. See the description of that property for information about how to configure the path itself.

### Initializers

- [init(rawValue:)](<uidynamicitemcollisionboundstype/init(rawvalue_).md>)
