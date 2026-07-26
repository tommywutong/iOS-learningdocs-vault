---
title: AccessibilityChildBehavior
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/accessibilitychildbehavior
source_url: 'https://developer.apple.com/documentation/swiftui/accessibilitychildbehavior'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/accessibilitychildbehavior.json'
content_hash: 'sha256:142be0726372a634'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# AccessibilityChildBehavior

<sub>Structure</sub>

Defines the behavior for the child elements of the new parent element.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct AccessibilityChildBehavior
```

## Relationships

- **Conforms To**: [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md)

## Topics

### Getting behaviors

- [combine](accessibilitychildbehavior/combine.md) — Any child accessibility element’s properties are merged into the new accessibility element.
- [contain](accessibilitychildbehavior/contain.md) — Any child accessibility elements become children of the new accessibility element.
- [ignore](accessibilitychildbehavior/ignore.md) — Any child accessibility elements become hidden.

## See Also

### Creating accessible elements

- [accessibilityElement(children:)](<view/accessibilityelement(children_).md>) — Creates a new accessibility element, or modifies the [AccessibilityChildBehavior](accessibilitychildbehavior.md) of the existing accessibility element.
- [accessibilityChildren(children:)](<view/accessibilitychildren(children_).md>) — Replaces the existing accessibility element’s children with one or more new synthetic accessibility elements.
- [accessibilityRepresentation(representation:)](<view/accessibilityrepresentation(representation_).md>) — Replaces one or more accessibility elements for this view with new accessibility elements.
