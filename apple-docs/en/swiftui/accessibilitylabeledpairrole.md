---
title: AccessibilityLabeledPairRole
framework: SwiftUI
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/accessibilitylabeledpairrole
source_url: 'https://developer.apple.com/documentation/swiftui/accessibilitylabeledpairrole'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/accessibilitylabeledpairrole.json'
content_hash: 'sha256:8b51ce6b1195bd8b'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# AccessibilityLabeledPairRole

<sub>Enumeration</sub>

The role of an accessibility element in a label / content pair.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@frozen enum AccessibilityLabeledPairRole
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Copyable](../swift/copyable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Getting roles

- [AccessibilityLabeledPairRole.content](accessibilitylabeledpairrole/content.md) — This element represents the content part of the label / content pair.
- [AccessibilityLabeledPairRole.label](accessibilitylabeledpairrole/label.md) — This element represents the label part of the label / content pair.

## See Also

### Applying labels

- [accessibilityLabel(_:)](<view/accessibilitylabel(__).md>) — Adds a label to the view that describes its contents.
- [accessibilityLabel(_:isEnabled:)](<view/accessibilitylabel(__isenabled_).md>) — Adds a label to the view that describes its contents.
- [accessibilityLabel(content:)](<view/accessibilitylabel(content_).md>) — Adds a label to the view that describes its contents.
- [accessibilityInputLabels(_:)](<view/accessibilityinputlabels(__).md>) — Sets alternate input labels with which users identify a view.
- [accessibilityInputLabels(_:isEnabled:)](<view/accessibilityinputlabels(__isenabled_).md>) — Sets alternate input labels with which users identify a view.
- [accessibilityLabeledPair(role:id:in:)](<view/accessibilitylabeledpair(role_id_in_).md>) — Pairs an accessibility element representing a label with the element for the matching content.
