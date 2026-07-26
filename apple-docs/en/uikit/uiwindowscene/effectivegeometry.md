---
title: effectiveGeometry
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, tvOS 16.0+, visionOS 1.0+]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiwindowscene/effectivegeometry
source_url: 'https://developer.apple.com/documentation/uikit/uiwindowscene/effectivegeometry'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiwindowscene/effectivegeometry.json'
content_hash: 'sha256:b64807bf053a9623'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIWindowScene](../uiwindowscene.md)

# effectiveGeometry

<sub>Instance Property</sub>

The current values for the window scene’s geometry in system space.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var effectiveGeometry: UIWindowScene.Geometry { get }
```

## Discussion

This property is key-value observing (KVO) compliant. Observing [effectiveGeometry](effectivegeometry.md) is the recommended way to receive notifications of changes to the window scene’s geometry. These changes can occur because of user interaction or as a result of the system resolving a geometry request.

## See Also

### Working with window geometry

- [- requestGeometryUpdateWithPreferences:errorHandler:](<requestgeometryupdate(__errorhandler_).md>) — Requests an update to the window scene’s geometry using the specified geometry preferences object.
- [Geometry](geometry.md) — An object that provides geometry information about the window scene.
- [GeometryPreferences](geometrypreferences.md) — An abstract superclass for representing window scene geometry preferences.
- [iOS](geometrypreferences/ios.md) — An object that represents the geometry preferences for a window scene in an iOS app.
- [Mac](geometrypreferences/mac.md) — An object that represents the geometry preferences for a window scene in an app built with Mac Catalyst.
- [Vision](geometrypreferences/vision.md)
- [UIProposedSceneSizeNoPreference](../uiproposedscenesizenopreference.md) — Used as the value for a dimension of a size related preference when wanting to leave it unchanged.
