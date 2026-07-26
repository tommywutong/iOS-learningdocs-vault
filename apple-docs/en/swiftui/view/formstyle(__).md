---
title: 'formStyle(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift, swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/formstyle(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/formstyle(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/formstyle%28_%3A%29.json'
content_hash: 'sha256:54d8ea4d9daf491d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# formStyle(_:)

<sub>Instance Method</sub>

Sets the style for forms in a view hierarchy.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func formStyle<S>(_ style: S) -> some View where S : FormStyle

```

## Parameters

- `style` — The form style to set.

## Return Value

A view that uses the specified form style for itself and its child views.

## See Also

### Grouping inputs

- [Form](../form.md) — A container for grouping controls used for data entry, such as in settings or inspectors.
- [LabeledContent](../labeledcontent.md) — A container for attaching a label to a value-bearing view.
- [labeledContentStyle(_:)](<labeledcontentstyle(__).md>) — Sets a style for labeled content.
