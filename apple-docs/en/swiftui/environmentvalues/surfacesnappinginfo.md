---
title: surfaceSnappingInfo
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [visionOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/environmentvalues/surfacesnappinginfo
source_url: 'https://developer.apple.com/documentation/swiftui/environmentvalues/surfacesnappinginfo'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/environmentvalues/surfacesnappinginfo.json'
content_hash: 'sha256:d037b739bd55164f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [EnvironmentValues](../environmentvalues.md)

# surfaceSnappingInfo

<sub>Instance Property</sub>

Provides information about the current snap state of the scene.

<sub>visionOS</sub>

```swift
var surfaceSnappingInfo: SurfaceSnappingInfo { get }
```

## Discussion

Use the provided [SurfaceSnappingInfo](../surfacesnappinginfo.md) from the environment to modify the content of your view

```swift
struct LightFixtureView: View {
    @Environment(\.surfaceSnappingInfo)
    var snappingInfo: SurfaceSnappingInfo

    var body: some View {
        if snappingInfo.isSnapped {
            switch SurfaceSnappingInfo.authorizationStatus {
                case .authorized:
                    switch snappingInfo.classification {
                        case .table:
                            LampView()
                        case .floor:
                            FloorLampView()
                        default:
                            DefaultLampView()
                    }
                default:
                    DefaultLampView()
            }
        } else {
            FloatingOrbLampView()
        }
    }
}
```

This environment value should be accessed inside a view of your app, not at the app or scene level. If you try to access this value at the scene or app level it will always return the default value.

If you would like access to the classification of the surface a scene is snapped to, the user must allow the app to access information about their surroundings. In your app’s `Info.plist` you should set `UIWantsDetailedSurfaceInfo` to `YES` and set `NSWorldSensingUsageDescription` to provide a description of why your app is requesting this information. The description will be displayed to the user when they first snap a scene from your app.
