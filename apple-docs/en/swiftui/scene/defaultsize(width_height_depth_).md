---
title: 'defaultSize(width:height:depth:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [visionOS 1.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/scene/defaultsize(width:height:depth:)'
source_url: 'https://developer.apple.com/documentation/swiftui/scene/defaultsize(width:height:depth:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/scene/defaultsize%28width%3Aheight%3Adepth%3A%29.json'
content_hash: 'sha256:19e526bccea1cd3e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Scene](../scene.md)

# defaultSize(width:height:depth:)

<sub>Instance Method</sub>

Sets a default size for a volumetric window.

<sub>visionOS</sub>

```swift
nonisolated func defaultSize(width: CGFloat, height: CGFloat, depth: CGFloat) -> some Scene

```

## Parameters

- `width` — The default width for the created window.

- `height` — The default height for the created window.

- `depth` — The default depth for the created volumetric window.

## Return Value

A scene that uses a default size for new windows.

## Discussion

Use this modifier to indicate the default initial size for a new 3D window created from a [Scene](../scene.md) using [VolumetricWindowStyle](../volumetricwindowstyle.md):

```swift
WindowGroup {
    ContentView()
}
.windowStyle(.volumetric)
.defaultSize(width: 600, height: 400, depth: 600)
```

Each parameter is specified in points. The size of a volumetric scene is immutable after creation.

This modifier affects only windows that have the volumetric style in visionOS.

## See Also

### Sizing a window

- [Positioning and sizing windows](../../visionos/positioning-and-sizing-windows.md) — Influence the initial geometry of windows that your app presents.
- [defaultSize(_:)](<defaultsize(__).md>) — Sets a default size for a window.
- [defaultSize(width:height:)](<defaultsize(width_height_).md>) — Sets a default width and height for a window.
- [defaultSize(_:in:)](<defaultsize(__in_).md>) — Sets a default size for a volumetric window.
- [defaultSize(width:height:depth:in:)](<defaultsize(width_height_depth_in_).md>) — Sets a default size for a volumetric window.
- [windowResizability(_:)](<windowresizability(__).md>) — Sets the kind of resizability to use for a window.
- [WindowResizability](../windowresizability.md) — The resizability of a window.
- [windowIdealSize(_:)](<windowidealsize(__).md>) — Specifies how windows derived form this scene should determine their size when zooming.
- [WindowIdealSize](../windowidealsize.md) — A type which defines the size a window should use when zooming.
