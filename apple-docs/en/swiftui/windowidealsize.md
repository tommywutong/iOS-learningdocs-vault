---
title: WindowIdealSize
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [macOS 15.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/windowidealsize
source_url: 'https://developer.apple.com/documentation/swiftui/windowidealsize'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/windowidealsize.json'
content_hash: 'sha256:0443c9c691fdb7a3'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# WindowIdealSize

<sub>Structure</sub>

A type which defines the size a window should use when zooming.

<sub>macOS</sub>

```swift
struct WindowIdealSize
```

## Overview

Use this type in conjunction with the `Scene.windowIdealSize(_:)` modifier to override the default behavior for how windows behave when performing a zoom.

For example, you can define a window group where the window has an ideal width of 800 points and an ideal height of 600 points:

```swift
struct MyApp: App {
    var body: some Scene {
        WindowGroup {
            ContentView()
                .frame(idealWidth: 800, idealHeight: 600)
        }
        .windowIdealSize(.fitToContent)
    }
}
```

## Relationships

- **Conforms To**: [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Type Properties

- [automatic](windowidealsize/automatic.md) — The automatic window ideal size. Windows will use the system behavior when determining the size to use when zooming.
- [fitToContent](windowidealsize/fittocontent.md) — A window ideal size which uses the ideal size of the window’s contents.
- [maximum](windowidealsize/maximum.md) — A window ideal size which uses the maximum size of the window’s contents.

## See Also

### Sizing a window

- [Positioning and sizing windows](../visionos/positioning-and-sizing-windows.md) — Influence the initial geometry of windows that your app presents.
- [defaultSize(_:)](<scene/defaultsize(__).md>) — Sets a default size for a window.
- [defaultSize(width:height:)](<scene/defaultsize(width_height_).md>) — Sets a default width and height for a window.
- [defaultSize(width:height:depth:)](<scene/defaultsize(width_height_depth_).md>) — Sets a default size for a volumetric window.
- [defaultSize(_:in:)](<scene/defaultsize(__in_).md>) — Sets a default size for a volumetric window.
- [defaultSize(width:height:depth:in:)](<scene/defaultsize(width_height_depth_in_).md>) — Sets a default size for a volumetric window.
- [windowResizability(_:)](<scene/windowresizability(__).md>) — Sets the kind of resizability to use for a window.
- [WindowResizability](windowresizability.md) — The resizability of a window.
- [windowIdealSize(_:)](<scene/windowidealsize(__).md>) — Specifies how windows derived form this scene should determine their size when zooming.
