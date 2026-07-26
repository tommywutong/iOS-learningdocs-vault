---
title: swipeActionsContainer()
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, visionOS 27.0+ beta, watchOS 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: /documentation/swiftui/view/swipeactionscontainer()
source_url: 'https://developer.apple.com/documentation/swiftui/view/swipeactionscontainer()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/swipeactionscontainer%28%29.json'
content_hash: 'sha256:33fc8606acb7355e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# swipeActionsContainer()

<sub>Instance Method</sub>

Coordinates swipe action dismissal and mutual exclusion across rows in a container.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
nonisolated func swipeActionsContainer() -> some View

```

## Discussion

Apply this modifier to a `ScrollView` or other container that holds rows using the [swipeActions(edge:allowsFullSwipe:content:)](<swipeactions(edge_allowsfullswipe_content_).md>) modifier. The container ensures that:

- Only one row’s swipe actions are revealed at a time.
- Scrolling the container dismisses any open actions.
- Tapping outside the active row dismisses its actions.

`List` provides this coordination automatically. Use `swipeActionsContainer()` when building custom row-based layouts that use `ScrollView`, `LazyVStack`, or similar containers.

```swift
ScrollView {
    LazyVStack {
        ForEach(items) { item in
            ItemRow(item)
                .swipeActions {
                    Button("Delete", role: .destructive) {
                        delete(item)
                    }
                }
        }
    }
}
.swipeActionsContainer()
```

Applying this modifier to a `List` is a no-op, since `List` already provides this coordination.

## See Also

### Container controls

- [swipeActions(edge:allowsFullSwipe:content:onPresentationChanged:)](<swipeactions(edge_allowsfullswipe_content_onpresentationchanged_).md>) — Adds custom swipe actions to a row in a list or container, notifying you when the actions are revealed or dismissed. _(beta)_
