---
title: UISheetPresentationController.Detent
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uisheetpresentationcontroller/detent
source_url: 'https://developer.apple.com/documentation/uikit/uisheetpresentationcontroller/detent'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uisheetpresentationcontroller/detent.json'
content_hash: 'sha256:d9ce5ce2a7d64147'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UISheetPresentationController](../uisheetpresentationcontroller.md)

# UISheetPresentationController.Detent

<sub>Class</sub>

An object that represents a height where a sheet naturally rests.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
@MainActor class Detent
```

## Relationships

- **Inherits From**: [NSObject](../../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../../swift/cvararg.md), [CustomDebugStringConvertible](../../swift/customdebugstringconvertible.md), [CustomStringConvertible](../../swift/customstringconvertible.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [NSObjectProtocol](../../objectivec/nsobjectprotocol.md), [Sendable](../../swift/sendable.md)

## Topics

### Creating a system detent

- [+ largeDetent](<detent/large().md>) — Creates a system detent for a sheet at full height.
- [+ mediumDetent](<detent/medium().md>) — Creates a system detent for a sheet that’s approximately half the height of the screen, and is inactive in compact height.

### Creating a custom detent

- [custom(identifier:resolver:)](<detent/custom(identifier_resolver_).md>) — Creates a custom detent for a sheet by computing its value according to the properties of the provided context.
- [resolvedValue(in:)](<detent/resolvedvalue(in_).md>) — Resolves a detent to its value.
- [UISheetPresentationControllerDetentResolutionContext](../uisheetpresentationcontrollerdetentresolutioncontext.md) — A context for resolving custom detent values.

### Identifying a detent

- [identifier](detent/identifier-swift.property.md) — The identifier of the detent.
- [Identifier](detent/identifier-swift.struct.md) — Constants that identify system detent sizes.

### Instance Properties

- [backgroundEffect](detent/backgroundeffect.md)

## See Also

### Specifying the height

- [detents](detents.md) — The array of heights where a sheet can rest.
- [selectedDetentIdentifier](selecteddetentidentifier.md) — The identifier of the most recently selected detent.
