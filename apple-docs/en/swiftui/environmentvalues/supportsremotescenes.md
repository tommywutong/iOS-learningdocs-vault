---
title: supportsRemoteScenes
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/environmentvalues/supportsremotescenes
source_url: 'https://developer.apple.com/documentation/swiftui/environmentvalues/supportsremotescenes'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/environmentvalues/supportsremotescenes.json'
content_hash: 'sha256:f3d21719b76dd297'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [EnvironmentValues](../environmentvalues.md)

# supportsRemoteScenes

<sub>Instance Property</sub>

Indicates if the current device supports presenting a [RemoteImmersiveSpace](../remoteimmersivespace.md) on a remote device.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var supportsRemoteScenes: Bool { get }
```

## Discussion

Use this to provide affordances for displaying your app’s content on a remote device.

```swift
struct NewSolarSystemImmersiveSpaceButton: View {
    @Environment(\.openImmersiveSpace) private var openImmersiveSpace
    @Environment(\.supportsRemoteScenes) private var supportsRemoteScenes

    var body: some View {
        Button("Present Solar System") {
            Task {
                await openImmersiveSpace(id: "solarSystem")
            }
        }
        .disabled(!supportsRemoteScenes)
        .help(!supportsRemoteScenes
            ? "Presenting remote scenes is not supported on this device."
            : "")
    }
}
```
