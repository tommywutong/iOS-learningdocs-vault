---
title: 'accessibilityElement(children:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/accessibilityelement(children:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/accessibilityelement(children:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/accessibilityelement%28children%3A%29.json'
content_hash: 'sha256:e97ffa7fe5e57a48'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# accessibilityElement(children:)

<sub>Instance Method</sub>

Creates a new accessibility element, or modifies the [AccessibilityChildBehavior](../accessibilitychildbehavior.md) of the existing accessibility element.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func accessibilityElement(children: AccessibilityChildBehavior = .ignore) -> some View

```

## Parameters

- `children` — The behavior to use when creating or transforming an accessibility element. The default is [ignore](../accessibilitychildbehavior/ignore.md)

## Discussion

See also:

- [ignore](../accessibilitychildbehavior/ignore.md)
- [combine](../accessibilitychildbehavior/combine.md)
- [contain](../accessibilitychildbehavior/contain.md)

## See Also

### Creating accessible elements

- [accessibilityChildren(children:)](<accessibilitychildren(children_).md>) — Replaces the existing accessibility element’s children with one or more new synthetic accessibility elements.
- [accessibilityRepresentation(representation:)](<accessibilityrepresentation(representation_).md>) — Replaces one or more accessibility elements for this view with new accessibility elements.
- [AccessibilityChildBehavior](../accessibilitychildbehavior.md) — Defines the behavior for the child elements of the new parent element.
