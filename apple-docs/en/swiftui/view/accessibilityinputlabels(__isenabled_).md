---
title: 'accessibilityInputLabels(_:isEnabled:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/accessibilityinputlabels(_:isenabled:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/accessibilityinputlabels(_:isenabled:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/accessibilityinputlabels%28_%3Aisenabled%3A%29.json'
content_hash: 'sha256:306c4c459ee50c39'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# accessibilityInputLabels(_:isEnabled:)

<sub>Instance Method</sub>

Sets alternate input labels with which users identify a view.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func accessibilityInputLabels(_ inputLabelKeys: [LocalizedStringKey], isEnabled: Bool) -> ModifiedContent<Self, AccessibilityAttachmentModifier>
```

## Parameters

- `inputLabelKeys` — The accessibility input labels to apply.

- `isEnabled` — If true the accessibility input labels are applied; otherwise the accessibility input labels are unchanged.

## Discussion

Provide labels in descending order of importance. Voice Control and Full Keyboard Access use the input labels.

> [!note] Note
> If you don’t specify any input labels, the user can still refer to the view using the accessibility label that you add with the `accessibilityLabel()` modifier.

## See Also

### Applying labels

- [accessibilityLabel(_:)](<accessibilitylabel(__).md>) — Adds a label to the view that describes its contents.
- [accessibilityLabel(_:isEnabled:)](<accessibilitylabel(__isenabled_).md>) — Adds a label to the view that describes its contents.
- [accessibilityLabel(content:)](<accessibilitylabel(content_).md>) — Adds a label to the view that describes its contents.
- [accessibilityInputLabels(_:)](<accessibilityinputlabels(__).md>) — Sets alternate input labels with which users identify a view.
- [accessibilityLabeledPair(role:id:in:)](<accessibilitylabeledpair(role_id_in_).md>) — Pairs an accessibility element representing a label with the element for the matching content.
- [AccessibilityLabeledPairRole](../accessibilitylabeledpairrole.md) — The role of an accessibility element in a label / content pair.
