---
title: remoteDeviceIdentifier
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [macOS 26.0+, visionOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/environmentvalues/remotedeviceidentifier
source_url: 'https://developer.apple.com/documentation/swiftui/environmentvalues/remotedeviceidentifier'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/environmentvalues/remotedeviceidentifier.json'
content_hash: 'sha256:5f12ac5b989edd61'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [EnvironmentValues](../environmentvalues.md)

# remoteDeviceIdentifier

<sub>Instance Property</sub>

An opaque object that identifies the device on which the scene (from which this value is accessed from) is being presented on.

<sub>macOS, visionOS</sub>

```swift
var remoteDeviceIdentifier: RemoteDeviceIdentifier? { get }
```

## Discussion

When accessed in a context that is being presented on the local device, this value will be `nil`.

This identifier can also be used to initialize an `ARKitSession` associated with the remote device.

```swift
struct SolarSystem: CompositorContent {
    @Environment(\.remoteDeviceIdentifier) private var deviceID

    var body: some CompositorContent {
        RemoteImmersiveSpace {
            CompositorLayer { layerRenderer in
                // Create an ARSession for the device
                let arSession = ARKitSession(deviceID)

                // Set up and run the Metal render loop.
                let renderThread = Thread {
                    let engine = solar_engine_create(
                        layerRenderer, arSession)
                    solar_engine_render_loop(engine)
                }
                renderThread.name = "Render Thread"
                renderThread.start()
            }
        }
    }
}
```

> [!note] Note
> This identifier is not stable across app launches.
