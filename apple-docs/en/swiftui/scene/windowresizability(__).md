---
title: 'windowResizability(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 13.0+, visionOS 1.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/scene/windowresizability(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/scene/windowresizability(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/scene/windowresizability%28_%3A%29.json'
content_hash: 'sha256:e0dfe7f50ef1ec13'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Scene](../scene.md)

# windowResizability(_:)

<sub>Instance Method</sub>

Sets the kind of resizability to use for a window.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
nonisolated func windowResizability(_ resizability: WindowResizability) -> some Scene

```

## Parameters

- `resizability` — The resizability to use for windows created by this scene.

## Return Value

A scene that uses the specified resizability strategy.

## Discussion

Use this scene modifier to apply a value of type [WindowResizability](../windowresizability.md) to a [Scene](../scene.md) that you define in your [App](../app.md) declaration. The value that you specify indicates the strategy the system uses to place minimum and maximum size restrictions on windows that it creates from that scene.

For example, you can create a window group that people can resize to between 100 and 400 points in both dimensions by applying both a frame with those constraints to the scene’s content, and the [contentSize](../windowresizability/contentsize.md) resizability to the scene:

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

The default value for all scenes if you don’t apply the modifier is [automatic](../windowresizability/automatic.md). With that strategy, [Settings](../settings.md) windows use the [contentSize](../windowresizability/contentsize.md) strategy, while all others use [contentMinSize](../windowresizability/contentminsize.md).

## See Also

### Sizing a window

- [Positioning and sizing windows](../../visionos/positioning-and-sizing-windows.md) — Influence the initial geometry of windows that your app presents.
- [defaultSize(_:)](<defaultsize(__).md>) — Sets a default size for a window.
- [defaultSize(width:height:)](<defaultsize(width_height_).md>) — Sets a default width and height for a window.
- [defaultSize(width:height:depth:)](<defaultsize(width_height_depth_).md>) — Sets a default size for a volumetric window.
- [defaultSize(_:in:)](<defaultsize(__in_).md>) — Sets a default size for a volumetric window.
- [defaultSize(width:height:depth:in:)](<defaultsize(width_height_depth_in_).md>) — Sets a default size for a volumetric window.
- [WindowResizability](../windowresizability.md) — The resizability of a window.
- [windowIdealSize(_:)](<windowidealsize(__).md>) — Specifies how windows derived form this scene should determine their size when zooming.
- [WindowIdealSize](../windowidealsize.md) — A type which defines the size a window should use when zooming.
