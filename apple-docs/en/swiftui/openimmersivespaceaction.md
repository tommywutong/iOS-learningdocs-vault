---
title: OpenImmersiveSpaceAction
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [macOS 26.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/openimmersivespaceaction
source_url: 'https://developer.apple.com/documentation/swiftui/openimmersivespaceaction'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/openimmersivespaceaction.json'
content_hash: 'sha256:6cce71f37c31ddc0'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# OpenImmersiveSpaceAction

<sub>Structure</sub>

An action that presents an immersive space.

<sub>macOS, visionOS</sub>

```swift
@MainActor struct OpenImmersiveSpaceAction
```

## Overview

Use the [openImmersiveSpace](environmentvalues/openimmersivespace.md) environment value to get the instance of this structure for a given [Environment](environment.md). Then call the instance to present a space. You call the instance directly because it defines `callAsFunction()` methods that Swift calls when you call the instance.

On macOS, this may be used to open a remote immersive space declared with [RemoteImmersiveSpace](remoteimmersivespace.md). When your app opens a remote immersive space, the system may ask the user for a preferred device with which to display the content.

For example, you can define a button that opens a specified planet in an immersive space:

```swift
@main
struct SolarSystemApp: App {
    var body: some Scene {
        ImmersiveSpace(for: Planet.ID.self) { $planetID in
            // ...
        }
    }
}

struct ShowPlanetButton: View {
    var planet: Planet
    @Environment(\.openImmersiveSpace) private var openImmersiveSpace

    var body: some View {
        Button("Show \(planet.name)") {
            Task {
                await openImmersiveSpace(value: planet.ID)
            }
        }
    }
}
```

You indicate which immersive space to open by providing one of the following:

- A string identifier that you pass through the `id` parameter.
- A `value` parameter that has a type that matches the type that you specify in the space’s initializer, as in the above example.
- Both an identifier and a value. This enables you to define multiple spaces that take input values of the same type and distinguish them by their string identifiers.

The call is asynchronous and returns after presenting the space or if an error occurs. You can check for errors by inspecting the call’s return value, which is of type [Result](openimmersivespaceaction/result.md). For example, the call returns an error if you already have an immersive space open, because the system enables only one space to be open at a time.

If you provide a value when you open the space, the scene’s trailing closure receives a binding to the value that you provide. For best performance, use lightweight data for the presentation value. For structured model values that conform to [Identifiable](../swift/identifiable.md), the value’s identifier makes a good presentation value, like the `planet.ID` value in the above code.

## Relationships

- **Conforms To**: [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Calling the action

- [callAsFunction(id:)](<openimmersivespaceaction/callasfunction(id_).md>) — Presents an immersive space for the scene with the specified identifier.
- [callAsFunction(id:value:)](<openimmersivespaceaction/callasfunction(id_value_).md>) — Presents the immersive space that your app defines for the specified identifier and that handles the type of the presented value.
- [callAsFunction(value:)](<openimmersivespaceaction/callasfunction(value_).md>) — Presents the immersive space that handles the type of the presented value.

### Getting the result

- [Result](openimmersivespaceaction/result.md) — The outcome of an attempt to open an immersive space.

### Instance Methods

- [callAsFunction(foveatedStreaming:)](<openimmersivespaceaction/callasfunction(foveatedstreaming_).md>) — Presents the immersive space that your app defines for the specified foveated streaming session.

## See Also

### Opening an immersive space

- [openImmersiveSpace](environmentvalues/openimmersivespace.md) — An action that presents an immersive space.
