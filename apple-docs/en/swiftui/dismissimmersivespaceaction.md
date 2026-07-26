---
title: DismissImmersiveSpaceAction
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [macOS 26.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/dismissimmersivespaceaction
source_url: 'https://developer.apple.com/documentation/swiftui/dismissimmersivespaceaction'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/dismissimmersivespaceaction.json'
content_hash: 'sha256:07ab2696002067fa'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# DismissImmersiveSpaceAction

<sub>Structure</sub>

An action that dismisses an immersive space.

<sub>macOS, visionOS</sub>

```swift
@MainActor struct DismissImmersiveSpaceAction
```

## Overview

Use the [dismissImmersiveSpace](environmentvalues/dismissimmersivespace.md) environment value to get an instance of this type for a given [Environment](environment.md). Then call the instance to dismiss a space. You call the instance directly because it defines a [callAsFunction()](<dismissimmersivespaceaction/callasfunction().md>) method that Swift calls when you call the instance.

On macOS, this may be used to dismiss a remote immersive space declared with [RemoteImmersiveSpace](remoteimmersivespace.md).

For example, you can define a button that dismisses an immersive space:

```swift
@main
struct MyApp: App {
    var body: some Scene {
        WindowGroup {
            DismissImmersiveSpaceButton()
        }
        ImmersiveSpace(id: "solarSystem") {
            SolarSystemView()
        }
    }
}

struct DismissImmersiveSpaceButton: View {
    @Environment(\.dismissImmersiveSpace) private var dismissImmersiveSpace

    var body: some View {
        Button("Dismiss") {
            Task {
                await dismissImmersiveSpace()
            }
        }
    }
}
```

The asynchronous call returns after the system finishes dismissing the space. Unlike the call to [openImmersiveSpace](environmentvalues/openimmersivespace.md) that you use to open the space — which requires an identifier, a value, or both to specify which space to open — the dismiss action requires no parameters because there can be only one immersive space open at a time. The call closes the space that is currently open, if any.

## Relationships

- **Conforms To**: [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Calling the action

- [callAsFunction()](<dismissimmersivespaceaction/callasfunction().md>) — Dismisses the currently opened immersive space.

## See Also

### Closing the immersive space

- [dismissImmersiveSpace](environmentvalues/dismissimmersivespace.md) — An immersive space dismissal action stored in a view’s environment.
