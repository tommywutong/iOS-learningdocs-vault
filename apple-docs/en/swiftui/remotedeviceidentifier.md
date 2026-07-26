---
title: RemoteDeviceIdentifier
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [macOS 26.0+, visionOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/remotedeviceidentifier
source_url: 'https://developer.apple.com/documentation/swiftui/remotedeviceidentifier'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/remotedeviceidentifier.json'
content_hash: 'sha256:1771e70471a869d7'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# RemoteDeviceIdentifier

<sub>Structure</sub>

An opaque type that identifies a remote device displaying scene content in a [RemoteImmersiveSpace](remoteimmersivespace.md).

<sub>macOS, visionOS</sub>

```swift
struct RemoteDeviceIdentifier
```

## Overview

Access this from the [remoteDeviceIdentifier](environmentvalues/remotedeviceidentifier.md) environment property in a remote scene to get the identifier for that scene’s device.

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

## Relationships

- **Conforms To**: [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Instance Properties

- [cDevice](remotedeviceidentifier/cdevice.md) — Returns the `ar_device` associated with this device.

## See Also

### Handling remote immersive spaces

- [RemoteImmersiveSpace](remoteimmersivespace.md) — A scene that presents its content in an unbounded space on a remote device.
