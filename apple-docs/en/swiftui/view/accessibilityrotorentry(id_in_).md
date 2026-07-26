---
title: 'accessibilityRotorEntry(id:in:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/accessibilityrotorentry(id:in:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/accessibilityrotorentry(id:in:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/accessibilityrotorentry%28id%3Ain%3A%29.json'
content_hash: 'sha256:12f0f8b7f4251b07'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# accessibilityRotorEntry(id:in:)

<sub>Instance Method</sub>

Defines an explicit identifier tying an Accessibility element for this view to an entry in an Accessibility Rotor.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func accessibilityRotorEntry<ID>(id: ID, in namespace: Namespace.ID) -> some View where ID : Hashable

```

## Parameters

- `id` — An arbitrary hashable identifier. Pass this same value when initializing an AccessibilityRotorEntry.

- `namespace` — A namespace created with `@Namespace()`. Pass this same namespace when initializing an `AccessibilityRotorEntry`.

## Discussion

Use this when creating an AccessibilityRotorEntry without a namespace does not allow SwiftUI to automatically find and reveal the element, or when the Rotor entry should be associated with a sub-element of a complex view generated in a ForEach, for example.

## See Also

### Configuring rotors

- [accessibilityLinkedGroup(id:in:)](<accessibilitylinkedgroup(id_in_).md>) — Links multiple accessibility elements so that the user can quickly navigate from one element to another, even when the elements are not near each other in the accessibility hierarchy.
- [accessibilitySortPriority(_:)](<accessibilitysortpriority(__).md>) — Sets the sort priority order for this view’s accessibility element, relative to other elements at the same level.
