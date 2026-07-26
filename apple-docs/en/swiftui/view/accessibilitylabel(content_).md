---
title: 'accessibilityLabel(content:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/accessibilitylabel(content:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/accessibilitylabel(content:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/accessibilitylabel%28content%3A%29.json'
content_hash: 'sha256:05260eaf55a5795e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# accessibilityLabel(content:)

<sub>Instance Method</sub>

Adds a label to the view that describes its contents.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func accessibilityLabel<V>(@ContentBuilder content: (PlaceholderContentView<Self>) -> V) -> some View where V : View

```

## Parameters

- `content` — A content builder closure that takes a proxy value representing the modified view. You can combine the modified view with other content to create a new accessibility label for the original view.

## Discussion

Use this method to append content to the accessibility label for a view. For example, you could use this method to label a badge or alert that is custom drawn without removing the existing accessibility label.

## See Also

### Applying labels

- [accessibilityLabel(_:)](<accessibilitylabel(__).md>) — Adds a label to the view that describes its contents.
- [accessibilityLabel(_:isEnabled:)](<accessibilitylabel(__isenabled_).md>) — Adds a label to the view that describes its contents.
- [accessibilityInputLabels(_:)](<accessibilityinputlabels(__).md>) — Sets alternate input labels with which users identify a view.
- [accessibilityInputLabels(_:isEnabled:)](<accessibilityinputlabels(__isenabled_).md>) — Sets alternate input labels with which users identify a view.
- [accessibilityLabeledPair(role:id:in:)](<accessibilitylabeledpair(role_id_in_).md>) — Pairs an accessibility element representing a label with the element for the matching content.
- [AccessibilityLabeledPairRole](../accessibilitylabeledpairrole.md) — The role of an accessibility element in a label / content pair.
