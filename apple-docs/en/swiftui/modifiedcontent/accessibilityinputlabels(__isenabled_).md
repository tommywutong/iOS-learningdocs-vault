---
title: 'accessibilityInputLabels(_:isEnabled:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/modifiedcontent/accessibilityinputlabels(_:isenabled:)'
source_url: 'https://developer.apple.com/documentation/swiftui/modifiedcontent/accessibilityinputlabels(_:isenabled:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/modifiedcontent/accessibilityinputlabels%28_%3Aisenabled%3A%29.json'
content_hash: 'sha256:4c632030ffd2fbe9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [ModifiedContent](../modifiedcontent.md)

# accessibilityInputLabels(_:isEnabled:)

<sub>Instance Method</sub>

Sets alternate input labels with which users identify a view.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func accessibilityInputLabels(_ inputLabelKeys: [LocalizedStringKey], isEnabled: Bool) -> ModifiedContent<Content, Modifier>
```

## Parameters

- `inputLabelKeys` — The accessibility input labels to apply.

- `isEnabled` — If true the accessibility input labels are applied; otherwise the accessibility input labels are unchanged.

## Discussion

Provide labels in descending order of importance. Voice Control and Full Keyboard Access use the input labels.

> [!note] Note
> If you don’t specify any input labels, the user can still refer to the view using the accessibility label that you add with the `accessibilityLabel()` modifier.
