---
title: WindowResizability
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 13.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/windowresizability
source_url: 'https://developer.apple.com/documentation/swiftui/windowresizability'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/windowresizability.json'
content_hash: 'sha256:b7b942d31cb38933'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# WindowResizability

<sub>Structure</sub>

The resizability of a window.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
struct WindowResizability
```

## Overview

Use the [windowResizability(_:)](<scene/windowresizability(__).md>) scene modifier to apply a value of this type to a [Scene](scene.md) that you define in your [App](app.md) declaration. The value that you specify indicates the strategy the system uses to place minimum and maximum size restrictions on windows that it creates from that scene.

For example, you can create a window group that people can resize to between 100 and 400 points in both dimensions by applying both a frame with those constraints to the scene’s content, and the [contentSize](windowresizability/contentsize.md) resizability to the scene:

```swift
@main
struct MyApp: App {
    var body: some Scene {
        WindowGroup {
            ContentView()
                .frame(
                    minWidth: 100, maxWidth: 400,
                    minHeight: 100, maxHeight: 400)
        }
        .windowResizability(.contentSize)
    }
}
```

The default value for all scenes if you don’t apply the modifier is [automatic](windowresizability/automatic.md). With that strategy, [Settings](settings.md) windows use the [contentSize](windowresizability/contentsize.md) strategy, while all others use [contentMinSize](windowresizability/contentminsize.md). Windows on visionOS with a window style of [volumetric](windowstyle/volumetric.md) also use the [contentSize](windowresizability/contentsize.md) strategy.

## Relationships

- **Conforms To**: [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Getting the resizability

- [automatic](windowresizability/automatic.md) — The automatic window resizability.
- [contentMinSize](windowresizability/contentminsize.md) — A window resizability that’s partially derived from the window’s content.
- [contentSize](windowresizability/contentsize.md) — A window resizability that’s derived from the window’s content.

## See Also

### Sizing a window

- [Positioning and sizing windows](../visionos/positioning-and-sizing-windows.md) — Influence the initial geometry of windows that your app presents.
- [defaultSize(_:)](<scene/defaultsize(__).md>) — Sets a default size for a window.
- [defaultSize(width:height:)](<scene/defaultsize(width_height_).md>) — Sets a default width and height for a window.
- [defaultSize(width:height:depth:)](<scene/defaultsize(width_height_depth_).md>) — Sets a default size for a volumetric window.
- [defaultSize(_:in:)](<scene/defaultsize(__in_).md>) — Sets a default size for a volumetric window.
- [defaultSize(width:height:depth:in:)](<scene/defaultsize(width_height_depth_in_).md>) — Sets a default size for a volumetric window.
- [windowResizability(_:)](<scene/windowresizability(__).md>) — Sets the kind of resizability to use for a window.
- [windowIdealSize(_:)](<scene/windowidealsize(__).md>) — Specifies how windows derived form this scene should determine their size when zooming.
- [WindowIdealSize](windowidealsize.md) — A type which defines the size a window should use when zooming.
