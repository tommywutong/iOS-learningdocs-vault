---
title: 'accessibilitySortPriority(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/accessibilitysortpriority(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/accessibilitysortpriority(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/accessibilitysortpriority%28_%3A%29.json'
content_hash: 'sha256:46668768512605aa'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# accessibilitySortPriority(_:)

<sub>Instance Method</sub>

Sets the sort priority order for this view’s accessibility element, relative to other elements at the same level.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func accessibilitySortPriority(_ sortPriority: Double) -> ModifiedContent<Self, AccessibilityAttachmentModifier>
```

## Discussion

Higher numbers are sorted first. The default sort priority is zero.

## See Also

### Configuring rotors

- [accessibilityRotorEntry(id:in:)](<accessibilityrotorentry(id_in_).md>) — Defines an explicit identifier tying an Accessibility element for this view to an entry in an Accessibility Rotor.
- [accessibilityLinkedGroup(id:in:)](<accessibilitylinkedgroup(id_in_).md>) — Links multiple accessibility elements so that the user can quickly navigate from one element to another, even when the elements are not near each other in the accessibility hierarchy.
