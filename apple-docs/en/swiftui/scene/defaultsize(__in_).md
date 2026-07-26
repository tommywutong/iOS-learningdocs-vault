---
title: 'defaultSize(_:in:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [visionOS 1.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/scene/defaultsize(_:in:)'
source_url: 'https://developer.apple.com/documentation/swiftui/scene/defaultsize(_:in:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/scene/defaultsize%28_%3Ain%3A%29.json'
content_hash: 'sha256:990a76c49716a8ac'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Scene](../scene.md)

# defaultSize(_:in:)

<sub>Instance Method</sub>

Sets a default size for a volumetric window.

<sub>visionOS</sub>

```swift
nonisolated func defaultSize(_ size: Size3D, in unit: UnitLength) -> some Scene

```

## Parameters

- `unit` — The unit of length the dimensions of the window are specified in.

## Return Value

A scene that uses a default size for new windows.

## Discussion

Use this modifier to indicate the default initial size for a new 3D window created from a [Scene](../scene.md) using [VolumetricWindowStyle](../volumetricwindowstyle.md):

```swift
WindowGroup {
    ContentView()
}
.windowStyle(.volumetric)
.defaultSize(Size3D(width: 1, height: 1, depth: 0.5), in: .meters)
```

Each parameter is specified in the unit you provide. The size of a volumetric scene is immutable after creation.

This modifier affects only windows that have the volumetric style in visionOS.

## See Also

### Sizing a window

- [Positioning and sizing windows](../../visionos/positioning-and-sizing-windows.md) — Influence the initial geometry of windows that your app presents.
- [defaultSize(_:)](<defaultsize(__).md>) — Sets a default size for a window.
- [defaultSize(width:height:)](<defaultsize(width_height_).md>) — Sets a default width and height for a window.
- [defaultSize(width:height:depth:)](<defaultsize(width_height_depth_).md>) — Sets a default size for a volumetric window.
- [defaultSize(width:height:depth:in:)](<defaultsize(width_height_depth_in_).md>) — Sets a default size for a volumetric window.
- [windowResizability(_:)](<windowresizability(__).md>) — Sets the kind of resizability to use for a window.
- [WindowResizability](../windowresizability.md) — The resizability of a window.
- [windowIdealSize(_:)](<windowidealsize(__).md>) — Specifies how windows derived form this scene should determine their size when zooming.
- [WindowIdealSize](../windowidealsize.md) — A type which defines the size a window should use when zooming.
