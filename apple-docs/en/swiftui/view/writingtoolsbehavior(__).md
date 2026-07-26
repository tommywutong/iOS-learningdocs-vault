---
title: 'writingToolsBehavior(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, visionOS 2.4+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/writingtoolsbehavior(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/writingtoolsbehavior(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/writingtoolsbehavior%28_%3A%29.json'
content_hash: 'sha256:7fe56498bdee6260'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# writingToolsBehavior(_:)

<sub>Instance Method</sub>

Specifies the Writing Tools behavior for text and text input in the environment.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
nonisolated func writingToolsBehavior(_ behavior: WritingToolsBehavior) -> some View

```

## Parameters

- `behavior` — The Writing Tools behavior for text and text input in the environment.

## Return Value

A view preferring the specified Writing Tools behavior.

## Discussion

Use this view modifier to customize or disable the Writing Tools editing experience for [Text](../text.md) (when selectable), [TextField](../textfield.md), and [TextEditor](../texteditor.md) views.

## See Also

### Configuring the Writing Tools behavior

- [WritingToolsBehavior](../writingtoolsbehavior.md) — The Writing Tools editing experience for text and text input.
- [writingToolsAffordanceVisibility(_:)](<writingtoolsaffordancevisibility(__).md>) — Specifies whether the system should show the Writing Tools affordance for text input views affected by the environment.
