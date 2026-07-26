---
title: 'accessibilityShowsLargeContentViewer(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/accessibilityshowslargecontentviewer(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/accessibilityshowslargecontentviewer(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/accessibilityshowslargecontentviewer%28_%3A%29.json'
content_hash: 'sha256:a5647adcab077882'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# accessibilityShowsLargeContentViewer(_:)

<sub>Instance Method</sub>

Adds a custom large content view to be shown by the large content viewer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func accessibilityShowsLargeContentViewer<V>(@ContentBuilder _ largeContentView: () -> V) -> some View where V : View

```

## Discussion

Rely on the large content viewer only in situations where items must remain small due to unavoidable design constraints. For example, buttons in a tab bar remain small to leave more room for the main app content.

The following example shows how to add a custom large content view:

```swift
var body: some View {
    Button(action: newMessage) {
        Image(systemName: "plus")
    }
    .accessibilityShowsLargeContentViewer {
        Label("New Message", systemImage: "plus")
    }
}
```

Don’t use the large content viewer as a replacement for proper Dynamic Type support. For example, Dynamic Type allows items in a list to grow or shrink vertically to accommodate the user’s preferred font size. Rely on the large content viewer only in situations where items must remain small due to unavoidable design constraints.

For example, views that have their Dynamic Type size constrained with [dynamicTypeSize(_:)](<dynamictypesize(__).md>) may require a large content view.

## See Also

### Enlarging content

- [accessibilityShowsLargeContentViewer()](<accessibilityshowslargecontentviewer().md>) — Adds a default large content view to be shown by the large content viewer.
- [accessibilityLargeContentViewerEnabled](../environmentvalues/accessibilitylargecontentviewerenabled.md) — Whether the Large Content Viewer is enabled.
