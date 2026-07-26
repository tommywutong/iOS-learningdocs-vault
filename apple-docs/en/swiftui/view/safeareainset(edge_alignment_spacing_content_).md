---
title: 'safeAreaInset(edge:alignment:spacing:content:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/safeareainset(edge:alignment:spacing:content:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/safeareainset(edge:alignment:spacing:content:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/safeareainset%28edge%3Aalignment%3Aspacing%3Acontent%3A%29.json'
content_hash: 'sha256:10fde9a5f922f43b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# safeAreaInset(edge:alignment:spacing:content:)

<sub>Instance Method</sub>

Shows the specified content beside the modified view.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func safeAreaInset<V>(edge: HorizontalEdge, alignment: VerticalAlignment = .center, spacing: CGFloat? = nil, @ContentBuilder content: () -> V) -> some View where V : View

```

## Parameters

- `edge` — The horizontal edge of the view to inset by the width of `content`, to make space for `content`.

- `alignment` — The alignment guide used to position `content` vertically.

- `spacing` — Extra distance placed between the two views, or nil to use the default amount of spacing.

- `content` — A content builder function providing the view to display in the inset space of the modified view.

## Return Value

A new view that displays `content` beside the modified view, making space for the `content` view by horizontally insetting the modified view.

## Discussion

The `content` view is anchored to the specified horizontal edge in the parent view, aligning its vertical axis to the specified alignment guide. The modified view is inset by the width of `content`, from `edge`, with its safe area increased by the same amount.

```swift
struct ScrollableViewWithSideBar: View {
    var body: some View {
        ScrollView {
            ScrolledContent()
        }
        .safeAreaInset(edge: .leading, spacing: 0) {
            SideBarContent()
        }
    }
}
```

## See Also

### Staying in the safe areas

- [ignoresSafeArea(_:edges:)](<ignoressafearea(__edges_).md>) — Expands the safe area of a view.
- [ignoresSafeArea(_:edges:alignment:)](<ignoressafearea(__edges_alignment_).md>) — Expands the safe area of a view aligning content within the new bounds using the provided alignment. _(beta)_
- [safeAreaPadding(_:)](<safeareapadding(__).md>) — Adds the provided insets into the safe area of this view.
- [safeAreaPadding(_:_:)](<safeareapadding(____).md>) — Adds the provided insets into the safe area of this view.
- [SafeAreaRegions](../safearearegions.md) — A set of symbolic safe area regions.
