---
title: 'scrollContentBackground(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/scrollcontentbackground(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/scrollcontentbackground(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/scrollcontentbackground%28_%3A%29.json'
content_hash: 'sha256:c722b6e7065566da'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# scrollContentBackground(_:)

<sub>Instance Method</sub>

Specifies the visibility of the background for scrollable views within this view.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
nonisolated func scrollContentBackground(_ visibility: Visibility) -> some View

```

## Parameters

- `visibility` — The visibility to use for the background.

## Discussion

The following example hides the standard system background of the List.

```swift
List {
    Text("One")
    Text("Two")
    Text("Three")
}
.scrollContentBackground(.hidden)
```

On macOS 15.0 and later, the visibility of the scroll background helps achieve the seamless window/titlebar appearance for scroll views that fill the window’s content view, or a pane’s full width and height. `List` and `Form` have the seamless appearance by default, configurable by hiding the scroll background. `ScrollView` can become seamless by making the background visible.

## See Also

### Managing content visibility

- [scrollClipDisabled(_:)](<scrollclipdisabled(__).md>) — Sets whether a scroll view clips its content to its bounds.
- [ScrollContentOffsetAdjustmentBehavior](../scrollcontentoffsetadjustmentbehavior.md) — A type that defines the different kinds of content offset adjusting behaviors a scroll view can have.
