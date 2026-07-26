---
title: UICollectionLayoutSectionOrthogonalScrollingProperties
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, tvOS 17.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uicollectionlayoutsectionorthogonalscrollingproperties
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionlayoutsectionorthogonalscrollingproperties'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionlayoutsectionorthogonalscrollingproperties.json'
content_hash: 'sha256:b4fbfa7f9d7e5354'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UICollectionLayoutSectionOrthogonalScrollingProperties

<sub>Class</sub>

An object that specifies properties for a layout section that scrolls orthogonally in relation to the main layout axis.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor class UICollectionLayoutSectionOrthogonalScrollingProperties
```

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCopying](../foundation/nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md)

## Topics

### Specifying the bounce behavior

- [bounce](uicollectionlayoutsectionorthogonalscrollingproperties/bounce-swift.property.md) — A value that specifies whether the orthogonal scrolling section bounces past the edge of content and back again.
- [Bounce](uicollectionlayoutsectionorthogonalscrollingproperties/bounce-swift.enum.md) — Constants that specify whether the orthogonal scrolling section bounces past the edge of content and back again.

### Specifying the rate of deceleration

- [decelerationRate](uicollectionlayoutsectionorthogonalscrollingproperties/decelerationrate-swift.property.md) — A value that specifies the rate of deceleration in the orthogonal scrolling section after the scrolling pan gesture ends.
- [DecelerationRate](uicollectionlayoutsectionorthogonalscrollingproperties/decelerationrate-swift.struct.md) — Constants that specify the rate of deceleration in the orthogonal scrolling section after the scrolling pan gesture ends.

## See Also

### Specifying scrolling behavior

- [orthogonalScrollingBehavior](nscollectionlayoutsection/orthogonalscrollingbehavior.md) — The section’s scrolling behavior in relation to the main layout axis.
- [orthogonalScrollingProperties](nscollectionlayoutsection/orthogonalscrollingproperties.md) — The section’s orthogonal scrolling properties.
