---
title: 'defaultPosition(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 13.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/scene/defaultposition(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/scene/defaultposition(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/scene/defaultposition%28_%3A%29.json'
content_hash: 'sha256:633aef5e20090972'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Scene](../scene.md)

# defaultPosition(_:)

<sub>Instance Method</sub>

Sets a default position for a window.

<sub>macOS</sub>

```swift
nonisolated func defaultPosition(_ position: UnitPoint) -> some Scene

```

## Parameters

- `position` — A [UnitPoint](../unitpoint.md) that specifies where to place a newly opened window relative to the screen bounds.

## Return Value

A scene that uses a default position for new windows.

## Discussion

The first time your app opens a window from a particular scene declaration, the system places the window at the center of the screen by default. For scene types that support multiple simultaneous windows, the system offsets each additional window by a small amount to avoid completely obscuring existing windows.

You can override the default placement of the first window by applying a scene modifier that indicates where to place the window relative to the screen bounds. For example, you can request that the system place a new window in the bottom trailing corner of the screen:

```swift
@main
struct MyApp: App {
    var body: some Scene {
        WindowGroup {
            ContentView()
        }
        .defaultPosition(.bottomTrailing)
    }
}
```

The system aligns the point in the window that corresponds to the specified [UnitPoint](../unitpoint.md) with the point in the screen that corresponds to the same unit point.

You typically use one of the predefined unit points — like [bottomTrailing](../unitpoint/bottomtrailing.md) in the above example — but you can also use a custom unit point. For example, the following modifier aligns the point that’s one quarter of the way from the leading edge of the window with the point that’s one quarter of the way from the leading edge of the screen, while centering the window in the y-dimension:

```swift
WindowGroup {
    ContentView()
}
.defaultPosition(UnitPoint(x: 0.25, y: 0.5))
```

The modifier affects any scene type that creates windows in macOS, namely:

- [WindowGroup](../windowgroup.md)
- [Window](../window.md)
- [DocumentGroup](../documentgroup.md)
- [Settings](../settings.md)

The value that you provide acts only as an initial default. During state restoration, the system restores the window to the position that it last occupied.

## See Also

### Positioning a window

- [WindowLevel](../windowlevel.md) — The level of a window.
- [windowLevel(_:)](<windowlevel(__).md>) — Sets the window level of this scene.
- [WindowLayoutRoot](../windowlayoutroot.md) — A proxy which represents the root contents of a window.
- [WindowPlacement](../windowplacement.md) — A type which represents a preferred size and position for a window.
- [defaultWindowPlacement(_:)](<defaultwindowplacement(__).md>) — Defines a function used for determining the default placement of windows.
- [windowIdealPlacement(_:)](<windowidealplacement(__).md>) — Provides a function which determines a placement to use when windows of a scene zoom.
- [WindowPlacementContext](../windowplacementcontext.md) — A type which represents contextual information used for sizing and positioning windows.
- [WindowProxy](../windowproxy.md) — The proxy for an open window in the app.
- [DisplayProxy](../displayproxy.md) — A type which provides information about display hardware.
