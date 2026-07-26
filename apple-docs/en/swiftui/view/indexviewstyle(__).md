---
title: 'indexViewStyle(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, tvOS 14.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/indexviewstyle(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/indexviewstyle(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/indexviewstyle%28_%3A%29.json'
content_hash: 'sha256:c0de94dbab85289d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# indexViewStyle(_:)

<sub>Instance Method</sub>

Sets the style for the index view within the current environment.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func indexViewStyle<S>(_ style: S) -> some View where S : IndexViewStyle

```

## Parameters

- `style` — The style to apply to this view.

## See Also

### Styling groups

- [controlGroupStyle(_:)](<controlgroupstyle(__).md>) — Sets the style for control groups within this view.
- [ControlGroupStyle](../controlgroupstyle.md) — Defines the implementation of all control groups within a view hierarchy.
- [ControlGroupStyleConfiguration](../controlgroupstyleconfiguration.md) — The properties of a control group.
- [formStyle(_:)](<formstyle(__).md>) — Sets the style for forms in a view hierarchy.
- [FormStyle](../formstyle.md) — The appearance and behavior of a form.
- [FormStyleConfiguration](../formstyleconfiguration.md) — The properties of a form instance.
- [groupBoxStyle(_:)](<groupboxstyle(__).md>) — Sets the style for group boxes within this view.
- [GroupBoxStyle](../groupboxstyle.md) — A type that specifies the appearance and interaction of all group boxes within a view hierarchy.
- [GroupBoxStyleConfiguration](../groupboxstyleconfiguration.md) — The properties of a group box instance.
- [IndexViewStyle](../indexviewstyle.md) — Defines the implementation of all `IndexView` instances within a view hierarchy.
- [labeledContentStyle(_:)](<labeledcontentstyle(__).md>) — Sets a style for labeled content.
- [LabeledContentStyle](../labeledcontentstyle.md) — The appearance and behavior of a labeled content instance..
- [LabeledContentStyleConfiguration](../labeledcontentstyleconfiguration.md) — The properties of a labeled content instance.
