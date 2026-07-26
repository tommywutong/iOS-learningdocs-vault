---
title: 'swipeActions(edge:allowsFullSwipe:content:onPresentationChanged:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, visionOS 27.0+ beta, watchOS 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: '/documentation/swiftui/view/swipeactions(edge:allowsfullswipe:content:onpresentationchanged:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/swipeactions(edge:allowsfullswipe:content:onpresentationchanged:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/swipeactions%28edge%3Aallowsfullswipe%3Acontent%3Aonpresentationchanged%3A%29.json'
content_hash: 'sha256:6b2acd556b518085'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# swipeActions(edge:allowsFullSwipe:content:onPresentationChanged:)

<sub>Instance Method</sub>

Adds custom swipe actions to a row in a list or container, notifying you when the actions are revealed or dismissed.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
nonisolated func swipeActions(edge: HorizontalEdge = .trailing, allowsFullSwipe: Bool = true, @ContentBuilder content: () -> some View, onPresentationChanged: @escaping (Bool) -> Void) -> some View

```

## Parameters

- `edge` — The edge of the view to associate the swipe actions with. The default is [HorizontalEdge.trailing](../horizontaledge/trailing.md).

- `allowsFullSwipe` — A Boolean value that indicates whether a full swipe automatically performs the first action. The default is `true`.

- `content` — The content of the swipe actions.

- `onPresentationChanged` — A closure called when the swipe actions are revealed or dismissed.

## Discussion

Use this overload when you need to react to the swipe actions’s visibility — for example, to dim the row or update surrounding chrome while actions are showing.

```swift
@State private var isSwiped = false

MessageRow(message)
    .opacity(isSwiped ? 0.5 : 1.0)
    .swipeActions(edge: .trailing) {
        Button(role: .destructive) {
            store.delete(message)
        } label: {
            Label("Delete", systemImage: "trash")
        }
    } onPresentationChanged: {
        isSwiped = $0
    }
```

The closure is called with `true` when the row’s swipe actions become visible and `false` when they are dismissed.

## See Also

### Container controls

- [swipeActionsContainer()](<swipeactionscontainer().md>) — Coordinates swipe action dismissal and mutual exclusion across rows in a container. _(beta)_
