---
title: 'inspectorColumnWidth(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/inspectorcolumnwidth(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/inspectorcolumnwidth(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/inspectorcolumnwidth%28_%3A%29.json'
content_hash: 'sha256:9b0b85845dcf80a9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# inspectorColumnWidth(_:)

<sub>Instance Method</sub>

Sets a fixed, preferred width for the inspector containing this view when presented as a trailing column.

<sub>iOS, iPadOS, Mac Catalyst, macOS</sub>

```swift
nonisolated func inspectorColumnWidth(_ width: CGFloat) -> some View

```

## Parameters

- `width` — The preferred fixed width for the inspector if presented as a trailing column.

## Discussion

Apply this modifier on the content of a [inspector(isPresented:content:)](<inspector(ispresented_content_).md>) to specify a fixed preferred width for the trailing column. Use [inspectorColumnWidth(min:ideal:max:)](<inspectorcolumnwidth(min_ideal_max_).md>) if you need to specify a flexible width.

The following example shows an editor interface with an inspector, which when presented as a trailing-column, has a fixed width of 225 points. The example also uses [interactiveDismissDisabled(_:)](<interactivedismissdisabled(__).md>) to prevent the inspector from being collapsed by user action like dragging a divider.

```swift
MyEditorView()
    .inspector {
        TextTraitsInspectorView()
            .inspectorColumnWidth(225)
            .interactiveDismissDisabled()
    }
```

> [!note] Note
> A fixed width does not prevent the user collapsing the inspector on macOS. See [interactiveDismissDisabled(_:)](<interactivedismissdisabled(__).md>).

## See Also

### Presenting an inspector

- [inspector(isPresented:content:)](<inspector(ispresented_content_).md>) — Inserts an inspector at the applied position in the view hierarchy.
- [inspectorColumnWidth(min:ideal:max:)](<inspectorcolumnwidth(min_ideal_max_).md>) — Sets a flexible, preferred width for the inspector in a trailing-column presentation.
