---
title: UIWindowScene.GeometryPreferences.Vision
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [visionOS 1.0+]
languages: [swift, swift, swift, swift, swift, swift, occ, occ, occ, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiwindowscene/geometrypreferences/vision
source_url: 'https://developer.apple.com/documentation/uikit/uiwindowscene/geometrypreferences/vision'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiwindowscene/geometrypreferences/vision.json'
content_hash: 'sha256:12310a15cc7e294d'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [UIKit](../../../uikit.md) · [UIWindowScene](../../uiwindowscene.md) · [GeometryPreferences](../geometrypreferences.md)

# UIWindowScene.GeometryPreferences.Vision

<sub>Class</sub>

<sub>visionOS</sub>

```swift
class Vision
```

## Relationships

- **Inherits From**: [GeometryPreferences](../geometrypreferences.md)

- **Conforms To**: [CVarArg](../../../swift/cvararg.md), [CustomDebugStringConvertible](../../../swift/customdebugstringconvertible.md), [CustomStringConvertible](../../../swift/customstringconvertible.md), [Equatable](../../../swift/equatable.md), [Hashable](../../../swift/hashable.md), [NSObjectProtocol](../../../objectivec/nsobjectprotocol.md), [Sendable](../../../swift/sendable.md), [SendableMetatype](../../../swift/sendablemetatype.md)

## Topics

### Initializers

- [- init](<vision/init().md>) — Creates a geometry preference with no changes. Update the properties who’s preference should change
- [init(size:minimumSize:maximumSize:resizingRestrictions:)](<vision/init(size_minimumsize_maximumsize_resizingrestrictions_).md>)

### Instance Properties

- [maximumSize](vision/maximumsize.md)
- [minimumSize](vision/minimumsize.md)
- [resizingRestrictions](vision/resizingrestrictions.md)
- [size](vision/size.md)

## See Also

### Working with window geometry

- [effectiveGeometry](../effectivegeometry.md) — The current values for the window scene’s geometry in system space.
- [- requestGeometryUpdateWithPreferences:errorHandler:](<../requestgeometryupdate(__errorhandler_).md>) — Requests an update to the window scene’s geometry using the specified geometry preferences object.
- [Geometry](../geometry.md) — An object that provides geometry information about the window scene.
- [GeometryPreferences](../geometrypreferences.md) — An abstract superclass for representing window scene geometry preferences.
- [iOS](ios.md) — An object that represents the geometry preferences for a window scene in an iOS app.
- [Mac](mac.md) — An object that represents the geometry preferences for a window scene in an app built with Mac Catalyst.
- [UIProposedSceneSizeNoPreference](../../uiproposedscenesizenopreference.md) — Used as the value for a dimension of a size related preference when wanting to leave it unchanged.
