---
title: 'accessibilityInputLabels(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/modifiedcontent/accessibilityinputlabels(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/modifiedcontent/accessibilityinputlabels(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/modifiedcontent/accessibilityinputlabels%28_%3A%29.json'
content_hash: 'sha256:7852dfc22296be4b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [ModifiedContent](../modifiedcontent.md)

# accessibilityInputLabels(_:)

<sub>Instance Method</sub>

Sets alternate input labels with which users identify a view.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func accessibilityInputLabels(_ inputLabelKeys: [LocalizedStringKey]) -> ModifiedContent<Content, Modifier>
```

## Discussion

Provide labels in descending order of importance. Voice Control and Full Keyboard Access use the input labels.

> [!note] Note
> If you don’t specify any input labels, the user can still refer to the view using the accessibility label that you add with the `accessibilityLabel()` modifier.
