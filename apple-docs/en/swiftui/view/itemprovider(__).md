---
title: 'itemProvider(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/itemprovider(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/itemprovider(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/itemprovider%28_%3A%29.json'
content_hash: 'sha256:466de836db58ecaa'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# itemProvider(_:)

<sub>Instance Method</sub>

Provides a closure that vends the drag representation to be used for a particular data element.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func itemProvider(_ action: Optional<() -> NSItemProvider?>) -> some View

```

## See Also

### Moving items using item providers

- [onDrag(_:preview:)](<ondrag(__preview_).md>) — Activates this view as the source of a drag and drop operation.
- [onDrag(_:)](<ondrag(__).md>) — Activates this view as the source of a drag and drop operation.
- [onDrop(of:isTargeted:perform:)](<ondrop(of_istargeted_perform_).md>) — Defines the destination of a drag-and-drop operation that handles the dropped content with a closure that you specify.
- [onDrop(of:delegate:)](<ondrop(of_delegate_).md>) — Defines the destination of a drag and drop operation using behavior controlled by the delegate that you provide.
- [DropDelegate](../dropdelegate.md) — An interface that you implement to interact with a drop operation in a view modified to accept drops.
- [DropProposal](../dropproposal.md) — The behavior of a drop.
- [DropOperation](../dropoperation.md) — Operation types that determine how a drag and drop session resolves when the user drops a drag item.
- [DropInfo](../dropinfo.md) — The current state of a drop.
