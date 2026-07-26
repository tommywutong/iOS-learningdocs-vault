---
title: 'accessibilityDefaultFocus(_:_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/accessibilitydefaultfocus(_:_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/accessibilitydefaultfocus(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/accessibilitydefaultfocus%28_%3A_%3A%29.json'
content_hash: 'sha256:bf19a6e020805cb7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# accessibilityDefaultFocus(_:_:)

<sub>Instance Method</sub>

Defines a region in which default accessibility focus is evaluated by assigning a value to a given accessibility focus state binding.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func accessibilityDefaultFocus<Value>(_ binding: AccessibilityFocusState<Value>.Binding, _ value: Value) -> some View where Value : Hashable

```

## Parameters

- `binding` — An accessibility focus state binding to update when evaluating default accessibility focus.

- `value` — The value to set the binding to during evaluation.

## Discussion

Accessibility default focus is evaluated when a scene appears and an accessibility technology like VoiceOver focuses on its content, when an accessibility focus state binding update moves focus automatically, and when the layout of a scene changes and the accessibility technology must refocus on new content.

In the following example, an accessibility technology, like VoiceOver, automatically lands on the title of the playlist as the most important view to initially have focus on, rather than navigating through all controls to understand what the primary content of the view is.

```swift
var body: some View {
    VStack {
        PlayerControls(currentSong: $currentSong)
        Text(playlist.title)
            .font(.title)
            .accessibilityFocused($focusedField, equals: .title)
        PlaylistEntries(entries: playlist.entries)
    }
    .accessibilityDefaultFocus($focusedField, .title)
}
```

## See Also

### Focus

- [accessibilityFocused(_:)](<accessibilityfocused(__).md>) — Modifies this view by binding its accessibility element’s focus state to the given boolean state value.
- [accessibilityFocused(_:equals:)](<accessibilityfocused(__equals_).md>) — Modifies this view by binding its accessibility element’s focus state to the given state value.
