---
title: UIWindowScene.GeometryPreferences
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, tvOS 16.0+, visionOS 1.0+]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiwindowscene/geometrypreferences
source_url: 'https://developer.apple.com/documentation/uikit/uiwindowscene/geometrypreferences'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiwindowscene/geometrypreferences.json'
content_hash: 'sha256:618429f38aacc5f2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIWindowScene](../uiwindowscene.md)

# UIWindowScene.GeometryPreferences

<sub>Class</sub>

An abstract superclass for representing window scene geometry preferences.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
class GeometryPreferences
```

## Relationships

- **Inherits From**: [NSObject](../../objectivec/nsobject-swift.class.md)

- **Inherited By**: [Mac](geometrypreferences/mac.md), [Vision](geometrypreferences/vision.md), [iOS](geometrypreferences/ios.md)

- **Conforms To**: [CVarArg](../../swift/cvararg.md), [CustomDebugStringConvertible](../../swift/customdebugstringconvertible.md), [CustomStringConvertible](../../swift/customstringconvertible.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [NSObjectProtocol](../../objectivec/nsobjectprotocol.md)

## Topics

### Geometry preferences

- [Mac](geometrypreferences/mac.md) — An object that represents the geometry preferences for a window scene in an app built with Mac Catalyst.
- [iOS](geometrypreferences/ios.md) — An object that represents the geometry preferences for a window scene in an iOS app.

### Classes

- [Vision](geometrypreferences/vision.md)

## See Also

### Working with window geometry

- [effectiveGeometry](effectivegeometry.md) — The current values for the window scene’s geometry in system space.
- [- requestGeometryUpdateWithPreferences:errorHandler:](<requestgeometryupdate(__errorhandler_).md>) — Requests an update to the window scene’s geometry using the specified geometry preferences object.
- [Geometry](geometry.md) — An object that provides geometry information about the window scene.
- [iOS](geometrypreferences/ios.md) — An object that represents the geometry preferences for a window scene in an iOS app.
- [Mac](geometrypreferences/mac.md) — An object that represents the geometry preferences for a window scene in an app built with Mac Catalyst.
- [Vision](geometrypreferences/vision.md)
- [UIProposedSceneSizeNoPreference](../uiproposedscenesizenopreference.md) — Used as the value for a dimension of a size related preference when wanting to leave it unchanged.
