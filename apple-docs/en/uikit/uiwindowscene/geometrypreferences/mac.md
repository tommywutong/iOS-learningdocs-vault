---
title: UIWindowScene.GeometryPreferences.Mac
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS, iPadOS, Mac Catalyst 16.0+, tvOS, visionOS]
languages: [swift, swift, swift, swift, swift, swift, occ, occ, occ, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiwindowscene/geometrypreferences/mac
source_url: 'https://developer.apple.com/documentation/uikit/uiwindowscene/geometrypreferences/mac'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiwindowscene/geometrypreferences/mac.json'
content_hash: 'sha256:1d26421764b4574f'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [UIKit](../../../uikit.md) · [UIWindowScene](../../uiwindowscene.md) · [GeometryPreferences](../geometrypreferences.md)

# UIWindowScene.GeometryPreferences.Mac

<sub>Class</sub>

An object that represents the geometry preferences for a window scene in an app built with Mac Catalyst.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
class Mac
```

## Overview

Use this class to express macOS-specific geometry preferences when you call [- requestGeometryUpdateWithPreferences:errorHandler:](<../requestgeometryupdate(__errorhandler_).md>).

## Relationships

- **Inherits From**: [GeometryPreferences](../geometrypreferences.md)

- **Conforms To**: [CVarArg](../../../swift/cvararg.md), [CustomDebugStringConvertible](../../../swift/customdebugstringconvertible.md), [CustomStringConvertible](../../../swift/customstringconvertible.md), [Equatable](../../../swift/equatable.md), [Hashable](../../../swift/hashable.md), [NSObjectProtocol](../../../objectivec/nsobjectprotocol.md), [Sendable](../../../swift/sendable.md), [SendableMetatype](../../../swift/sendablemetatype.md)

## Topics

### Creating a geometry preferences object

- [- initWithSystemFrame:](<mac/init(systemframe_).md>) — Initializes a new window scene geometry preferences object with the specified window frame.
- [- init](<mac/init().md>) — Initializes a new window scene geometry preferences object.

### Accessing geometry information

- [systemFrame](mac/systemframe.md) — The preferred frame of the scene, in system coordinates.

## See Also

### Related Documentation

- [effectiveGeometry](../effectivegeometry.md) — The current values for the window scene’s geometry in system space.
- [- requestGeometryUpdateWithPreferences:errorHandler:](<../requestgeometryupdate(__errorhandler_).md>) — Requests an update to the window scene’s geometry using the specified geometry preferences object.

### Working with window geometry

- [effectiveGeometry](../effectivegeometry.md) — The current values for the window scene’s geometry in system space.
- [- requestGeometryUpdateWithPreferences:errorHandler:](<../requestgeometryupdate(__errorhandler_).md>) — Requests an update to the window scene’s geometry using the specified geometry preferences object.
- [Geometry](../geometry.md) — An object that provides geometry information about the window scene.
- [GeometryPreferences](../geometrypreferences.md) — An abstract superclass for representing window scene geometry preferences.
- [iOS](ios.md) — An object that represents the geometry preferences for a window scene in an iOS app.
- [Vision](vision.md)
- [UIProposedSceneSizeNoPreference](../../uiproposedscenesizenopreference.md) — Used as the value for a dimension of a size related preference when wanting to leave it unchanged.
