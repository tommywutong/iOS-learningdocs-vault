---
title: 'accessibilityLabel(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/accessibilitylabel(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/accessibilitylabel(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/accessibilitylabel%28_%3A%29.json'
content_hash: 'sha256:caab659500b8abbc'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# accessibilityLabel(_:)

<sub>Instance Method</sub>

Adds a label to the view that describes its contents.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@export(implementation) nonisolated func accessibilityLabel(_ label: LocalizedStringResource) -> ModifiedContent<Self, AccessibilityAttachmentModifier>
```

## Discussion

Use this method to provide an accessibility label for a view that doesn’t display text, like an icon. For example, you could use this method to label a button that plays music with the text “Play”. Don’t include text in the label that repeats information that users already have. For example, don’t use the label “Play button” because a button already has a trait that identifies it as a button.

## See Also

### Applying labels

- [accessibilityLabel(_:isEnabled:)](<accessibilitylabel(__isenabled_).md>) — Adds a label to the view that describes its contents.
- [accessibilityLabel(content:)](<accessibilitylabel(content_).md>) — Adds a label to the view that describes its contents.
- [accessibilityInputLabels(_:)](<accessibilityinputlabels(__).md>) — Sets alternate input labels with which users identify a view.
- [accessibilityInputLabels(_:isEnabled:)](<accessibilityinputlabels(__isenabled_).md>) — Sets alternate input labels with which users identify a view.
- [accessibilityLabeledPair(role:id:in:)](<accessibilitylabeledpair(role_id_in_).md>) — Pairs an accessibility element representing a label with the element for the matching content.
- [AccessibilityLabeledPairRole](../accessibilitylabeledpairrole.md) — The role of an accessibility element in a label / content pair.
