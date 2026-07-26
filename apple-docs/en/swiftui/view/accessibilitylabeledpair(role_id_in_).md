---
title: 'accessibilityLabeledPair(role:id:in:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/accessibilitylabeledpair(role:id:in:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/accessibilitylabeledpair(role:id:in:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/accessibilitylabeledpair%28role%3Aid%3Ain%3A%29.json'
content_hash: 'sha256:7f68ab18202e66b8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# accessibilityLabeledPair(role:id:in:)

<sub>Instance Method</sub>

Pairs an accessibility element representing a label with the element for the matching content.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func accessibilityLabeledPair<ID>(role: AccessibilityLabeledPairRole, id: ID, in namespace: Namespace.ID) -> some View where ID : Hashable

```

## Parameters

- `role` — Determines whether this element should be used as the label in the pair, or the content in the pair.

- `id` — The identifier for the label / content pair. Elements with matching identifiers within the same namespace will be paired together.

- `namespace` — The namespace used to organize label and content. Label and content under the same namespace with matching identifiers will be paired together.

## Discussion

Use `accessibilityLabeledPair` with a role of `AccessibilityLabeledPairRole.label` to identify the label, and a role of `AccessibilityLabeledPairRole.content` to identify the content. This improves the behavior of accessibility features such as VoiceOver when navigating such elements, allowing users to better understand the relationship between them.

## See Also

### Applying labels

- [accessibilityLabel(_:)](<accessibilitylabel(__).md>) — Adds a label to the view that describes its contents.
- [accessibilityLabel(_:isEnabled:)](<accessibilitylabel(__isenabled_).md>) — Adds a label to the view that describes its contents.
- [accessibilityLabel(content:)](<accessibilitylabel(content_).md>) — Adds a label to the view that describes its contents.
- [accessibilityInputLabels(_:)](<accessibilityinputlabels(__).md>) — Sets alternate input labels with which users identify a view.
- [accessibilityInputLabels(_:isEnabled:)](<accessibilityinputlabels(__isenabled_).md>) — Sets alternate input labels with which users identify a view.
- [AccessibilityLabeledPairRole](../accessibilitylabeledpairrole.md) — The role of an accessibility element in a label / content pair.
