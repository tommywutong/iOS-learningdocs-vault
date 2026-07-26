---
title: 'requestGeometryUpdate(_:errorHandler:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, tvOS 16.0+, visionOS 1.0+]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiwindowscene/requestgeometryupdate(_:errorhandler:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiwindowscene/requestgeometryupdate(_:errorhandler:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiwindowscene/requestgeometryupdate%28_%3Aerrorhandler%3A%29.json'
content_hash: 'sha256:aab93a9fdd1f356e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIWindowScene](../uiwindowscene.md)

# requestGeometryUpdate(_:errorHandler:)

<sub>Instance Method</sub>

Requests an update to the window scene’s geometry using the specified geometry preferences object.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func requestGeometryUpdate(_ geometryPreferences: UIWindowScene.GeometryPreferences, errorHandler: ((any Error) -> Void)? = nil)
```

## Parameters

- `geometryPreferences` — The geometry information to use for the request.

- `errorHandler` — An optional closure to call when an error occurs. The system may call the error handler asynchronously.

## Discussion

Use this method to explicitly request geometry changes to the window scene. The following code shows an example of requesting the window scene to rotate to a landscape orientation in iOS.

```swift
// In a view controller, get the window scene.
guard let windowScene = view.window?.windowScene else { return }

// Request the window scene to rotate to any landscape orientation.
windowScene.requestGeometryUpdate(.iOS(interfaceOrientations: .landscape)) { error in
    // Handle denial of request.
}
```

## See Also

### Working with window geometry

- [effectiveGeometry](effectivegeometry.md) — The current values for the window scene’s geometry in system space.
- [Geometry](geometry.md) — An object that provides geometry information about the window scene.
- [GeometryPreferences](geometrypreferences.md) — An abstract superclass for representing window scene geometry preferences.
- [iOS](geometrypreferences/ios.md) — An object that represents the geometry preferences for a window scene in an iOS app.
- [Mac](geometrypreferences/mac.md) — An object that represents the geometry preferences for a window scene in an app built with Mac Catalyst.
- [Vision](geometrypreferences/vision.md)
- [UIProposedSceneSizeNoPreference](../uiproposedscenesizenopreference.md) — Used as the value for a dimension of a size related preference when wanting to leave it unchanged.
