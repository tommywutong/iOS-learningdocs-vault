---
title: UIPointerRegion
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 13.4+, iPadOS 13.4+, Mac Catalyst 13.4+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uipointerregion
source_url: 'https://developer.apple.com/documentation/uikit/uipointerregion'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uipointerregion.json'
content_hash: 'sha256:5e173e4dcbab8c89'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIPointerRegion

<sub>Class</sub>

A rectangular region that interacts with pointer movements.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
@MainActor class UIPointerRegion
```

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCopying](../foundation/nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md)

## Topics

### Creating a region

- [init(rect:identifier:)](<uipointerregion/init(rect_identifier_).md>) — Creates a pointer region with the specified rectangle and optional identifier.

### Configuring a region

- [rect](uipointerregion/rect.md) — The rectangle bounds of the region.
- [identifier](uipointerregion/identifier-1tw1m.md) — An optional identifier for the region.
- [latchingAxes](uipointerregion/latchingaxes.md) — Axes along which the region latches after a primary click.

## See Also

### Pointer region

- [UIPointerRegionRequest](uipointerregionrequest.md) — An object to describe the pointer’s location in the interaction’s view.
