---
title: 'windowIdealSize(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 15.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/scene/windowidealsize(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/scene/windowidealsize(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/scene/windowidealsize%28_%3A%29.json'
content_hash: 'sha256:95e1efa961e7cf0f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Scene](../scene.md)

# windowIdealSize(_:)

<sub>Instance Method</sub>

Specifies how windows derived form this scene should determine their size when zooming.

<sub>macOS</sub>

```swift
nonisolated func windowIdealSize(_ idealSize: WindowIdealSize) -> some Scene

```

## Parameters

- `idealSize` — A value which determines how windows derived from this scene should size themselves when zooming.

## Discussion

The default behavior will size the window to its maximum size, or the bounds of the display, whichever is smaller. By overriding this behavior, you can provide a size that is appropriate for the contents of your window.

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

## See Also

### Sizing a window

- [Positioning and sizing windows](../../visionos/positioning-and-sizing-windows.md) — Influence the initial geometry of windows that your app presents.
- [defaultSize(_:)](<defaultsize(__).md>) — Sets a default size for a window.
- [defaultSize(width:height:)](<defaultsize(width_height_).md>) — Sets a default width and height for a window.
- [defaultSize(width:height:depth:)](<defaultsize(width_height_depth_).md>) — Sets a default size for a volumetric window.
- [defaultSize(_:in:)](<defaultsize(__in_).md>) — Sets a default size for a volumetric window.
- [defaultSize(width:height:depth:in:)](<defaultsize(width_height_depth_in_).md>) — Sets a default size for a volumetric window.
- [windowResizability(_:)](<windowresizability(__).md>) — Sets the kind of resizability to use for a window.
- [WindowResizability](../windowresizability.md) — The resizability of a window.
- [WindowIdealSize](../windowidealsize.md) — A type which defines the size a window should use when zooming.
