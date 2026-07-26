---
title: 'writingToolsAffordanceVisibility(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.4+, iPadOS 18.4+, Mac Catalyst 18.4+, macOS 15.4+, tvOS 18.4+, visionOS 2.4+, watchOS 11.4+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/writingtoolsaffordancevisibility(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/writingtoolsaffordancevisibility(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/writingtoolsaffordancevisibility%28_%3A%29.json'
content_hash: 'sha256:fe24e5358bada252'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# writingToolsAffordanceVisibility(_:)

<sub>Instance Method</sub>

Specifies whether the system should show the Writing Tools affordance for text input views affected by the environment.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func writingToolsAffordanceVisibility(_ visibility: Visibility) -> some View

```

## Parameters

- `visibility` — Whether the affordance may be shown for text input views.

## Return Value

A view with the specified Writing Tools affordance visibility.

## Discussion

Use this view modifier to disable the Writing Tools affordance for [TextField](../textfield.md) views when running on macOS or Mac Catalyst.

## See Also

### Configuring the Writing Tools behavior

- [writingToolsBehavior(_:)](<writingtoolsbehavior(__).md>) — Specifies the Writing Tools behavior for text and text input in the environment.
- [WritingToolsBehavior](../writingtoolsbehavior.md) — The Writing Tools editing experience for text and text input.
