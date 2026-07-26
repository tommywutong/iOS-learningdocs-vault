---
title: 'accessibilityInputLabels(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/accessibilityinputlabels(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/accessibilityinputlabels(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/accessibilityinputlabels%28_%3A%29.json'
content_hash: 'sha256:c0bfed048d7855be'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# accessibilityInputLabels(_:)

<sub>Instance Method</sub>

Sets alternate input labels with which users identify a view.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func accessibilityInputLabels(_ inputLabelKeys: [LocalizedStringKey]) -> ModifiedContent<Self, AccessibilityAttachmentModifier>
```

## Discussion

Provide labels in descending order of importance. Voice Control and Full Keyboard Access use the input labels.

> [!note] Note
> If you don’t specify any input labels, the user can still refer to the view using the accessibility label that you add with the `accessibilityLabel()` modifier.

## See Also

### Applying labels

- [accessibilityLabel(_:)](<accessibilitylabel(__).md>) — Adds a label to the view that describes its contents.
- [accessibilityLabel(_:isEnabled:)](<accessibilitylabel(__isenabled_).md>) — Adds a label to the view that describes its contents.
- [accessibilityLabel(content:)](<accessibilitylabel(content_).md>) — Adds a label to the view that describes its contents.
- [accessibilityInputLabels(_:isEnabled:)](<accessibilityinputlabels(__isenabled_).md>) — Sets alternate input labels with which users identify a view.
- [accessibilityLabeledPair(role:id:in:)](<accessibilitylabeledpair(role_id_in_).md>) — Pairs an accessibility element representing a label with the element for the matching content.
- [AccessibilityLabeledPairRole](../accessibilitylabeledpairrole.md) — The role of an accessibility element in a label / content pair.
