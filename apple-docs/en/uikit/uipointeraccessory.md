---
title: UIPointerAccessory
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uipointeraccessory
source_url: 'https://developer.apple.com/documentation/uikit/uipointeraccessory'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uipointeraccessory.json'
content_hash: 'sha256:4ccd749ea114e10b'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIPointerAccessory

<sub>Class</sub>

Constants that describe accessories to display alongside the primary pointer.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
@MainActor class UIPointerAccessory
```

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCopying](../foundation/nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md)

## Topics

### Creating a pointer accessory

- [init(_:position:)](<uipointeraccessory/init(__position_).md>) — Creates a pointer accessory with the specified shape and position.
- [arrow(_:)](<uipointeraccessory/arrow(__).md>) — Creates a pointer accessory with an arrow shape at the specified position.

### Matching the angle

- [orientationMatchesAngle](uipointeraccessory/orientationmatchesangle.md) — A Boolean value that indicates whether the system rotates the accessory to match its angle.

### Getting the shape

- [shape](uipointeraccessory/shape-8pp0a.md) — The shape of the accessory.

### Getting the position

- [position](uipointeraccessory/position-swift.property.md) — The position of the accessory relative to the primary pointer.
- [Position](uipointeraccessory/position-swift.struct.md) — A structure that specifies the position of the accessory relative to the primary pointer.

## See Also

### Pointer styles

- [UIPointerStyle](uipointerstyle.md) — An object that defines the pointer shape and effect.
- [UIPointerShape](uipointershape-swift.enum.md) — An object that defines the shape of custom pointers.
- [UIPointerEffect](uipointereffect-swift.enum.md) — An effect that alters a view’s appearance when a pointer enters the current region.
