---
title: UIPointerRegionRequest
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 13.4+, iPadOS 13.4+, Mac Catalyst 13.4+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uipointerregionrequest
source_url: 'https://developer.apple.com/documentation/uikit/uipointerregionrequest'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uipointerregionrequest.json'
content_hash: 'sha256:1878628789d65f9f'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIPointerRegionRequest

<sub>Class</sub>

An object to describe the pointer’s location in the interaction’s view.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
@MainActor class UIPointerRegionRequest
```

## Overview

The `UIPointerRegionRequest` is given to the `UIPointerInteractionDelegate` to allow for changes to the pointer interaction.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md)

## Topics

### Inspecting the region request

- [location](uipointerregionrequest/location.md) — The location of the pointer in the interaction’s view’s coordinate space.
- [modifiers](uipointerregionrequest/modifiers.md) — Key modifier flags representing keyboard keys pressed by the user at the time of this request.

## See Also

### Pointer region

- [UIPointerRegion](uipointerregion.md) — A rectangular region that interacts with pointer movements.
