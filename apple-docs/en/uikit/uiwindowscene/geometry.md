---
title: UIWindowScene.Geometry
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, tvOS 16.0+, visionOS 1.0+]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiwindowscene/geometry
source_url: 'https://developer.apple.com/documentation/uikit/uiwindowscene/geometry'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiwindowscene/geometry.json'
content_hash: 'sha256:57b47a8a0be70b26'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIWindowScene](../uiwindowscene.md)

# UIWindowScene.Geometry

<sub>Class</sub>

An object that provides geometry information about the window scene.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
class Geometry
```

## Relationships

- **Inherits From**: [NSObject](../../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../../swift/cvararg.md), [CustomDebugStringConvertible](../../swift/customdebugstringconvertible.md), [CustomStringConvertible](../../swift/customstringconvertible.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [NSCopying](../../foundation/nscopying.md), [NSObjectProtocol](../../objectivec/nsobjectprotocol.md)

## Topics

### Accessing scene geometry

- [systemFrame](geometry/systemframe.md) — The current frame of the scene, in system coordinates.
- [coordinateSpace](geometry/coordinatespace.md) — The coordinate space of the scene
- [interfaceOrientation](geometry/interfaceorientation.md) — The current interface orientation for the scene.
- [interfaceOrientationLocked](geometry/isinterfaceorientationlocked.md) — If the scene’s interface orientation is locked and preventing changes. To express a preference for this value, override  `UIViewController`’s `prefersInterfaceOrientationLocked`.

### Instance Properties

- [interactivelyResizing](geometry/isinteractivelyresizing.md) — Returns true when the scene is being resized interactively, otherwise false.
- [maximumSize](geometry/maximumsize.md) — The current app specified maximumSize. A value of CGFLOAT_MAX,CGFLOAT_MAX is returned if a maximum is not set by the application
- [minimumSize](geometry/minimumsize.md) — The current app specified minimumSize. A value of 0,0 is returned if a minimum is not set by the application
- [resizingRestrictions](geometry/resizingrestrictions.md) — The current app specified resizingRestriction. Default value UIWindowSceneResizingRestrictionsUnspecified

## See Also

### Working with window geometry

- [effectiveGeometry](effectivegeometry.md) — The current values for the window scene’s geometry in system space.
- [- requestGeometryUpdateWithPreferences:errorHandler:](<requestgeometryupdate(__errorhandler_).md>) — Requests an update to the window scene’s geometry using the specified geometry preferences object.
- [GeometryPreferences](geometrypreferences.md) — An abstract superclass for representing window scene geometry preferences.
- [iOS](geometrypreferences/ios.md) — An object that represents the geometry preferences for a window scene in an iOS app.
- [Mac](geometrypreferences/mac.md) — An object that represents the geometry preferences for a window scene in an app built with Mac Catalyst.
- [Vision](geometrypreferences/vision.md)
- [UIProposedSceneSizeNoPreference](../uiproposedscenesizenopreference.md) — Used as the value for a dimension of a size related preference when wanting to leave it unchanged.
