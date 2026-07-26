---
title: 'defaultSize(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 13.0+, visionOS 1.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/scene/defaultsize(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/scene/defaultsize(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/scene/defaultsize%28_%3A%29.json'
content_hash: 'sha256:d917448e07220edb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Scene](../scene.md)

# defaultSize(_:)

<sub>Instance Method</sub>

Sets a default size for a window.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
nonisolated func defaultSize(_ size: CGSize) -> some Scene

```

## Parameters

- `size` — The default size for new windows created from a scene.

## Return Value

A scene that uses a default size for new windows.

## Discussion

Use this scene modifier to indicate a default initial size for a new window that the system creates from a [Scene](../scene.md) declaration. For example, you can request that new windows that a [WindowGroup](../windowgroup.md) generates occupy 600 points in the x-dimension and 400 points in the y-dimension:

```swift
@main
struct MyApp: App {
    var body: some Scene {
        WindowGroup {
            ContentView()
        }
        .defaultSize(CGSize(width: 600, height: 400))
    }
}
```

The size that you specify acts only as a default for when the window first appears. People can later resize the window using interface controls that the system provides. Also, during state restoration, the system restores windows to their most recent size rather than the default size.

If you specify a default size that’s outside the range of the window’s inherent resizability in one or both dimensions, the system clamps the affected dimension to keep it in range. You can configure the resizability of a scene using the [windowResizability(_:)](<windowresizability(__).md>) modifier.

The default size modifier affects any scene type that creates windows in macOS, namely:

- [WindowGroup](../windowgroup.md)
- [Window](../window.md)
- [DocumentGroup](../documentgroup.md)
- [Settings](../settings.md)

If you want to specify the input directly in terms of width and height, use [defaultSize(width:height:)](<defaultsize(width_height_).md>) instead.

## See Also

### Sizing a window

- [Positioning and sizing windows](../../visionos/positioning-and-sizing-windows.md) — Influence the initial geometry of windows that your app presents.
- [defaultSize(width:height:)](<defaultsize(width_height_).md>) — Sets a default width and height for a window.
- [defaultSize(width:height:depth:)](<defaultsize(width_height_depth_).md>) — Sets a default size for a volumetric window.
- [defaultSize(_:in:)](<defaultsize(__in_).md>) — Sets a default size for a volumetric window.
- [defaultSize(width:height:depth:in:)](<defaultsize(width_height_depth_in_).md>) — Sets a default size for a volumetric window.
- [windowResizability(_:)](<windowresizability(__).md>) — Sets the kind of resizability to use for a window.
- [WindowResizability](../windowresizability.md) — The resizability of a window.
- [windowIdealSize(_:)](<windowidealsize(__).md>) — Specifies how windows derived form this scene should determine their size when zooming.
- [WindowIdealSize](../windowidealsize.md) — A type which defines the size a window should use when zooming.
