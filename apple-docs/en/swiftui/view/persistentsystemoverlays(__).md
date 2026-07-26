---
title: 'persistentSystemOverlays(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/persistentsystemoverlays(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/persistentsystemoverlays(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/persistentsystemoverlays%28_%3A%29.json'
content_hash: 'sha256:5b78655464d8a0d9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# persistentSystemOverlays(_:)

<sub>Instance Method</sub>

Sets the preferred visibility of the non-transient system views overlaying the app.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func persistentSystemOverlays(_ visibility: Visibility) -> some View

```

## Parameters

- `visibility` — A value that indicates the visibility of the non-transient system views overlaying the app.

## Discussion

Use this modifier to influence the appearance of system overlays in your app. The behavior varies by platform.

In iOS, the following example hides every persistent system overlay. In visionOS 2 and later, the SharePlay Indicator hides if the scene is shared through SharePlay, or not shared at all. During screen sharing, the indicator always remains visible. The Home indicator doesn’t appear without specific user intent when you set visibility to `hidden`. For a [WindowGroup](../windowgroup.md), the modifier affects the visibility of the window chrome. For an [ImmersiveSpace](../immersivespace.md), it affects the Home indicator.

```swift
struct ImmersiveView: View {
    var body: some View {
        Text("Maximum immersion")
            .persistentSystemOverlays(.hidden)
    }
}
```

> [!note] Note
> You can indicate a preference with this modifier, but the system might or might not be able to honor that preference.

Affected non-transient system views can include, but are not limited to:

- The Home indicator.
- The SharePlay indicator.
- The Multitasking Controls button and Picture in Picture on iPad.

## See Also

### Hiding system elements

- [labelsHidden()](<labelshidden().md>) — Hides the labels of any controls contained within this view.
- [labelsVisibility(_:)](<labelsvisibility(__).md>) — Controls the visibility of labels of any controls contained within this view.
- [labelsVisibility](../environmentvalues/labelsvisibility.md) — The labels visibility set by [labelsVisibility(_:)](<labelsvisibility(__).md>).
- [menuIndicator(_:)](<menuindicator(__).md>) — Sets the menu indicator visibility for controls within this view.
- [statusBarHidden(_:)](<statusbarhidden(__).md>) — Sets the visibility of the status bar. _(deprecated)_
- [Visibility](../visibility.md) — The visibility of a UI element, chosen automatically based on the platform, current context, and other factors.
