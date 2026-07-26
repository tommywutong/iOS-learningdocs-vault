---
title: MKAnnotationView.CollisionMode
framework: MapKit
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 11.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/mapkit/mkannotationview/collisionmode-swift.enum
source_url: 'https://developer.apple.com/documentation/mapkit/mkannotationview/collisionmode-swift.enum'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkannotationview/collisionmode-swift.enum.json'
content_hash: 'sha256:37760a8e4cd632b4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKAnnotationView](../mkannotationview.md)

# MKAnnotationView.CollisionMode

<sub>Enumeration</sub>

Constants that indicates how to interpret the collision frame rectangle of an annotation view.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
enum CollisionMode
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Enumeration Cases

- [MKAnnotationViewCollisionModeRectangle](collisionmode-swift.enum/rectangle.md) — A constant that indicates that the annotation view uses the full collision frame rectangle for detecting collisions.
- [MKAnnotationViewCollisionModeCircle](collisionmode-swift.enum/circle.md) — A constant that indicates that the annotation view uses an inscribed circle in the collision frame rectangle to determine collisions.
- [MKAnnotationViewCollisionModeNone](collisionmode-swift.enum/none.md) — A constant indicating that collisions can’t occur.
- [MKAnnotationViewCollisionModeRectangle](collisionmode-swift.enum/rectangle.md) — A constant that indicates that the annotation view uses the full collision frame rectangle for detecting collisions.
- [MKAnnotationViewCollisionModeCircle](collisionmode-swift.enum/circle.md) — A constant that indicates that the annotation view uses an inscribed circle in the collision frame rectangle to determine collisions.
- [MKAnnotationViewCollisionModeNone](collisionmode-swift.enum/none.md) — A constant indicating that collisions can’t occur.

### Initializers

- [init(rawValue:)](<collisionmode-swift.enum/init(rawvalue_).md>)

## See Also

### Managing collisions between annotation views

- [collisionMode](collisionmode-swift.property.md) — The collision mode to use when interpreting the collision frame rectangle.
