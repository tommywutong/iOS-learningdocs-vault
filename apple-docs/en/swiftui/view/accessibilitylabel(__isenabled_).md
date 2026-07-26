---
title: 'accessibilityLabel(_:isEnabled:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/accessibilitylabel(_:isenabled:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/accessibilitylabel(_:isenabled:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/accessibilitylabel%28_%3Aisenabled%3A%29.json'
content_hash: 'sha256:386dc17a72ef6d80'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# accessibilityLabel(_:isEnabled:)

<sub>Instance Method</sub>

Adds a label to the view that describes its contents.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@export(implementation) nonisolated func accessibilityLabel(_ label: LocalizedStringResource, isEnabled: Bool) -> ModifiedContent<Self, AccessibilityAttachmentModifier>
```

## Parameters

- `label` — The accessibility label to apply.

- `isEnabled` — If true the accessibility label is applied; otherwise the accessibility label is unchanged.

## Discussion

Use this method to provide an accessibility label for a view that doesn’t display text, like an icon. For example, you could use this method to label a button that plays music with the text “Play”. Don’t include text in the label that repeats information that users already have. For example, don’t use the label “Play button” because a button already has a trait that identifies it as a button.

## See Also

### Applying labels

- [accessibilityLabel(_:)](<accessibilitylabel(__).md>) — Adds a label to the view that describes its contents.
- [accessibilityLabel(content:)](<accessibilitylabel(content_).md>) — Adds a label to the view that describes its contents.
- [accessibilityInputLabels(_:)](<accessibilityinputlabels(__).md>) — Sets alternate input labels with which users identify a view.
- [accessibilityInputLabels(_:isEnabled:)](<accessibilityinputlabels(__isenabled_).md>) — Sets alternate input labels with which users identify a view.
- [accessibilityLabeledPair(role:id:in:)](<accessibilitylabeledpair(role_id_in_).md>) — Pairs an accessibility element representing a label with the element for the matching content.
- [AccessibilityLabeledPairRole](../accessibilitylabeledpairrole.md) — The role of an accessibility element in a label / content pair.
