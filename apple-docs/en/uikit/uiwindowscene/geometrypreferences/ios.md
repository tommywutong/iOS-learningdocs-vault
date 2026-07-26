---
title: UIWindowScene.GeometryPreferences.iOS
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, visionOS 1.0+]
languages: [swift, swift, swift, swift, swift, swift, occ, occ, occ, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiwindowscene/geometrypreferences/ios
source_url: 'https://developer.apple.com/documentation/uikit/uiwindowscene/geometrypreferences/ios'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiwindowscene/geometrypreferences/ios.json'
content_hash: 'sha256:1af08a720530ef0a'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [UIKit](../../../uikit.md) · [UIWindowScene](../../uiwindowscene.md) · [GeometryPreferences](../geometrypreferences.md)

# UIWindowScene.GeometryPreferences.iOS

<sub>Class</sub>

An object that represents the geometry preferences for a window scene in an iOS app.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
class iOS
```

## Overview

Use this class to express iOS-specific geometry preferences when you call [- requestGeometryUpdateWithPreferences:errorHandler:](<../requestgeometryupdate(__errorhandler_).md>).

## Relationships

- **Inherits From**: [GeometryPreferences](../geometrypreferences.md)

- **Conforms To**: [CVarArg](../../../swift/cvararg.md), [CustomDebugStringConvertible](../../../swift/customdebugstringconvertible.md), [CustomStringConvertible](../../../swift/customstringconvertible.md), [Equatable](../../../swift/equatable.md), [Hashable](../../../swift/hashable.md), [NSObjectProtocol](../../../objectivec/nsobjectprotocol.md), [Sendable](../../../swift/sendable.md), [SendableMetatype](../../../swift/sendablemetatype.md)

## Topics

### Creating a geometry preferences object

- [- initWithInterfaceOrientations:](<ios/init(interfaceorientations_).md>) — Initializes a new window scene geometry preferences object with the specified interface orientations.
- [- init](<ios/init().md>) — Initializes a new window scene geometry preferences object.

### Requesting preferred interface orientations

- [interfaceOrientations](ios/interfaceorientations.md) — The preferred interface orientations for the scene.

## See Also

### Related Documentation

- [effectiveGeometry](../effectivegeometry.md) — The current values for the window scene’s geometry in system space.
- [- requestGeometryUpdateWithPreferences:errorHandler:](<../requestgeometryupdate(__errorhandler_).md>) — Requests an update to the window scene’s geometry using the specified geometry preferences object.

### Working with window geometry

- [effectiveGeometry](../effectivegeometry.md) — The current values for the window scene’s geometry in system space.
- [- requestGeometryUpdateWithPreferences:errorHandler:](<../requestgeometryupdate(__errorhandler_).md>) — Requests an update to the window scene’s geometry using the specified geometry preferences object.
- [Geometry](../geometry.md) — An object that provides geometry information about the window scene.
- [GeometryPreferences](../geometrypreferences.md) — An abstract superclass for representing window scene geometry preferences.
- [Mac](mac.md) — An object that represents the geometry preferences for a window scene in an app built with Mac Catalyst.
- [Vision](vision.md)
- [UIProposedSceneSizeNoPreference](../../uiproposedscenesizenopreference.md) — Used as the value for a dimension of a size related preference when wanting to leave it unchanged.
